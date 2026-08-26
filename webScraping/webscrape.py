# import requests
# from bs4 import BeautifulSoup
# import time
# import csv
#
#
# def scrape_saflii(court_name):
#     search_url = f"https://www.saflii.org.za/za/cases/{court_name}/"
#
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
#     }
#
#     # Send GET request to the search URL
#     response = requests.get(search_url, headers=headers)
#
#     # Check if the request was successful
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#
#         # Adjust the following line if the class name for case listings is different
#         cases = soup.find_all('li', class_='case-item')  # Update the class as necessary
#
#         results = []
#
#         for case in cases:
#             title_tag = case.find('a')  # The title is typically in an <a> tag
#             if title_tag:
#                 title = title_tag.text.strip()
#                 link = title_tag['href']
#                 results.append((title, link))
#
#         return results
#     else:
#         print("Failed to retrieve results.")
#         return []
#
#
# def save_to_csv(data, court_name):
#     file_name = f'saflii_cases_{court_name}.csv'
#     with open(file_name, 'w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Title', 'Link'])
#         writer.writerows(data)
#     print(f"Data has been successfully saved to {file_name}.")
#
#
# if __name__ == "__main__":
#     print("Welcome to the SAFLII Scraper!")
#     court_name = input("Please enter the court name you want to search cases from: ")
#
#     print(f"\nSearching for cases from the court: {court_name}")
#     results = scrape_saflii(court_name)
#
#     if results:
#         save_to_csv(results, court_name)
#     else:
#         print(f"No results found for the court: {court_name}.")
#
# #It must find the information from the website such as the supreme and constitutional court and give everything it can about it.

import requests
from bs4 import BeautifulSoup
import csv


def scrape_saflii(court_code):
    base_url = "https://www.saflii.org.za"
    search_url = f"{base_url}/za/cases/{court_code}/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    print(f"\nRequesting URL: {search_url}")

    try:
        response = requests.get(search_url, headers=headers, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to SAFLII: {e}")
        return []

    print(f"Status Code: {response.status_code}")

    if response.status_code != 200:
        print("Failed to retrieve data. Check court selection.")
        return []

    soup = BeautifulSoup(response.content, "html.parser")

    results = []

    # Find all links inside list items
    case_links = soup.select("li a")

    for link in case_links:
        title = link.get_text(strip=True)
        href = link.get("href")

        # Only keep actual case pages
        if href and href.endswith(".html"):
            full_link = base_url + href
            results.append((title, full_link))

    return results


def save_to_csv(data, court_code):
    filename = f"saflii_cases_{court_code}.csv"

    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Link"])
            writer.writerows(data)

        print(f"\n✅ Data successfully saved to {filename}")

    except Exception as e:
        print(f"Error saving file: {e}")


def main():
    print("===================================")
    print("   SAFLII CASE SCRAPER TOOL")
    print("===================================")

    print("\nSelect a court:")
    print("1. Constitutional Court")
    print("2. Supreme Court of Appeal")
    print("3. High Court (Gauteng Johannesburg)")
    print("4. High Court (KwaZulu-Natal Durban)")

    choice = input("\nEnter your choice (1-4): ").strip()

    court_map = {
        "1": "ZACC",   # Constitutional Court
        "2": "ZASCA",  # Supreme Court of Appeal
        "3": "ZAGPJ",  # Gauteng High Court (Johannesburg)
        "4": "ZAKZD"   # KZN High Court (Durban)
    }

    court_code = court_map.get(choice)

    if not court_code:
        print("❌ Invalid choice. Please run the program again.")
        return

    print(f"\nFetching cases for {court_code}...")

    results = scrape_saflii(court_code)

    if results:
        print(f"\n✅ Found {len(results)} cases.")

        # Show preview (first 5 results)
        print("\nSample Results:")
        for i, (title, link) in enumerate(results[:5], start=1):
            print(f"{i}. {title}")
            print(f"   {link}")

        save_to_csv(results, court_code)

    else:
        print("❌ No cases found.")


if __name__ == "__main__":
    main()