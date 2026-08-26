# import tkinter as tk
# from tkinter import scrolledtext
#
#
# # Main application class
# class MainApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Chatbot Selector")
#
#         # Main interface: label and buttons to select chatbot
#         self.label = tk.Label(root, text="Choose a Chatbot to Start:")
#         self.label.pack(pady=20)
#
#         self.python_button = tk.Button(root, text="Python Chatbot", command=self.open_python_chatbot)
#         self.python_button.pack(pady=10)
#
#         self.webtech_button = tk.Button(root, text="Web Technologies Chatbot", command=self.open_webtech_chatbot)
#         self.webtech_button.pack(pady=10)
#
#
#     # Open Python chatbot window
#     def open_python_chatbot(self):
#         self.new_window = tk.Toplevel(self.root)
#         self.python_chatbot = PythonChatbot(self.new_window)
#
#     # Open Web Technologies chatbot window
#     def open_webtech_chatbot(self):
#         self.new_window = tk.Toplevel(self.root)
#         self.webtech_chatbot = WebTechChatbot(self.new_window)
#
#
# # Python chatbot class
# class PythonChatbot:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Python Chatbot")
#
#         # Chat display area
#         self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD)
#         self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
#
#         # Input field for user messages
#         self.entry = tk.Entry(root)
#         self.entry.pack(padx=10, pady=(0, 10), fill=tk.X)
#         self.entry.bind("<Return>", self.send_message)  # Bind Enter key to send message
#
#         # Send button
#         self.send_button = tk.Button(root, text="Send", command=self.send_message)
#         self.send_button.pack(pady=(0, 10))
#
#         # Initial bot greeting
#         self.chat_display.insert(tk.END, "Bot: Hello! Ask me anything about Python programming. Give me the word e.g loops,functions and etc.\n")
#
#         # Dictionary of responses
#         self.responses = {
#             "loops": "Python supports for and while loops. For example, while(i<5): print(i); i++; for i in range(5): print(i) will print numbers from 0 to 4.",
#             "functions": "Functions in Python are defined using the def keyword, e.g., def my_function(): print('Hello').",
#             "classes": "Python is an object-oriented programming language. You can define classes using the class keyword."
#         }
#
#     # Handle sending user message
#     def send_message(self, event=None):
#         user_message = self.entry.get()
#         if user_message:
#             # Display user message
#             self.chat_display.insert(tk.END, f"You: {user_message}\n")
#             self.entry.delete(0, tk.END)  # Clear entry field
#             self.respond(user_message)
#
#     # Generate bot response
#     def respond(self, user_message):
#         user_message = user_message.lower()  # Convert to lowercase for matching
#         bot_response = "I'm a Python chatbot. I can help with Python programming."
#
#         # Check for keywords in user message
#         for keyword, response in self.responses.items():
#             if keyword in user_message:
#                 bot_response = response
#                 break
#
#         # Display bot response
#         self.chat_display.insert(tk.END, f"Bot: {bot_response}\n")
#
#
# # Web Technologies chatbot class
# class WebTechChatbot:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Web Technologies Chatbot")
#
#         # Chat display area
#         self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD)
#         self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
#
#         # Input field for user messages
#         self.entry = tk.Entry(root)
#         self.entry.pack(padx=10, pady=(0, 10), fill=tk.X)
#         self.entry.bind("<Return>", self.send_message)  # Bind Enter key to send message
#
#         # Send button
#         self.send_button = tk.Button(root, text="Send", command=self.send_message)
#         self.send_button.pack(pady=(0, 10))
#
#         # Initial bot greeting
#         self.chat_display.insert(tk.END, "Bot: Hello! Ask me anything about HTML, CSS, JavaScript, or PHP.\n")
#
#         # Dictionary of responses
#         self.responses = {
#             "html": "HTML (HyperText Markup Language) is the standard language for creating web pages. It describes the structure of a webpage using markup.",
#             "css": "CSS (Cascading Style Sheets) is used to style and layout web pages. For example, you can change the color, font, and spacing of your content.",
#             "javascript": "JavaScript is a programming language that allows you to implement complex features on web pages, such as interactive content and dynamic updates.",
#             "php": "PHP (Hypertext Preprocessor) is a server-side scripting language designed for web development but also used as a general-purpose programming language."
#         }
#
#     # Handle sending user message
#     def send_message(self, event=None):
#         user_message = self.entry.get()
#         if user_message:
#             # Display user message
#             self.chat_display.insert(tk.END, f"You: {user_message}\n")
#             self.entry.delete(0, tk.END)  # Clear entry field
#             self.respond(user_message)
#
#     # Generate bot response
#     def respond(self, user_message):
#         user_message = user_message.lower()  # Convert to lowercase for matching
#         bot_response = "I'm a Web Technologies chatbot. I can help with HTML, CSS, JavaScript, and PHP."
#
#         # Check for keywords in user message
#         for keyword, response in self.responses.items():
#             if keyword in user_message:
#                 bot_response = response
#                 break
#
#         # Display bot response
#         self.chat_display.insert(tk.END, f"Bot: {bot_response}\n")
#
#
# # Main application entry point
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = MainApp(root)
#     root.geometry("300x200")
#     root.mainloop()
#

# import tkinter as tk
# from tkinter import scrolledtext
# import requests
# from bs4 import BeautifulSoup
#
# # Main application class
# class MainApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Chatbot Selector")
#
#         # Main interface: label and buttons to select chatbot
#         self.label = tk.Label(root, text="Choose a Chatbot to Start:")
#         self.label.pack(pady=20)
#
#         self.python_button = tk.Button(root, text="Python Chatbot", command=self.open_python_chatbot)
#         self.python_button.pack(pady=10)
#
#         self.webtech_button = tk.Button(root, text="Web Technologies Chatbot", command=self.open_webtech_chatbot)
#         self.webtech_button.pack(pady=10)
#
#     # Open Python chatbot window
#     def open_python_chatbot(self):
#         self.new_window = tk.Toplevel(self.root)
#         self.python_chatbot = PythonChatbot(self.new_window)
#
#     # Open Web Technologies chatbot window
#     def open_webtech_chatbot(self):
#         self.new_window = tk.Toplevel(self.root)
#         self.webtech_chatbot = WebTechChatbot(self.new_window)
#
# # Python chatbot class
# class PythonChatbot:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Python Chatbot")
#
#         # Chat display area
#         self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
#         self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
#
#         # Input field for user messages
#         self.entry = tk.Entry(root)
#         self.entry.pack(padx=10, pady=(0, 10), fill=tk.X)
#         self.entry.bind("<Return>", self.send_message)  # Bind Enter key to send message
#
#         # Send button
#         self.send_button = tk.Button(root, text="Send", command=self.send_message)
#         self.send_button.pack(pady=(0, 10))
#
#         # Initial bot greeting
#         self.chat_display.config(state='normal')
#         self.chat_display.insert(tk.END, "Bot: Hello! Ask me anything about Python programming. Give me the word e.g loops, functions, etc.\n")
#         self.chat_display.config(state='disabled')
#
#         # ScrolledText to display scraped results
#         self.results_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
#         self.results_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
#
#     # Handle sending user message
#     def send_message(self, event=None):
#         user_message = self.entry.get()
#         if user_message:
#             # Display user message
#             self.chat_display.config(state='normal')
#             self.chat_display.insert(tk.END, f"You: {user_message}\n")
#             self.chat_display.config(state='disabled')
#             self.entry.delete(0, tk.END)  # Clear entry field
#             self.respond(user_message)
#
#     # Generate bot response
#     def respond(self, user_message):
#         self.results_display.config(state='normal')
#         self.results_display.delete(1.0, tk.END)  # Clear previous results
#         self.results_display.insert(tk.END, "Bot: Searching the web for information...\n")
#         self.results_display.config(state='disabled')
#
#         # Perform web scraping
#         self.scrape_web(user_message)
#
#     # Web scraping function
#     def scrape_web(self, query):
#         search_url = f"https://www.google.com/search?q={query}+python"
#         headers = {"User-Agent": "Mozilla/5.0"}
#         response = requests.get(search_url, headers=headers)
#
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, "html.parser")
#             results = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')  # Assuming the results are in div tags with these classes
#
#             self.results_display.config(state='normal')
#             for result in results[:5]:  # Display top 5 relevant results
#                 self.results_display.insert(tk.END, result.text + "\n\n")
#             self.results_display.config(state='disabled')
#
# # Web Technologies chatbot class
# class WebTechChatbot:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Web Technologies Chatbot")
#
#         # Chat display area
#         self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
#         self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
#
#         # Input field for user messages
#         self.entry = tk.Entry(root)
#         self.entry.pack(padx=10, pady=(0, 10), fill=tk.X)
#         self.entry.bind("<Return>", self.send_message)  # Bind Enter key to send message
#
#         # Send button
#         self.send_button = tk.Button(root, text="Send", command=self.send_message)
#         self.send_button.pack(pady=(0, 10))
#
#         # Initial bot greeting
#         self.chat_display.config(state='normal')
#         self.chat_display.insert(tk.END, "Bot: Hello! Ask me anything about HTML, CSS, JavaScript, or PHP.\n")
#         self.chat_display.config(state='disabled')
#
#         # ScrolledText to display scraped results
#         self.results_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
#         self.results_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
#
#     # Handle sending user message
#     def send_message(self, event=None):
#         user_message = self.entry.get()
#         if user_message:
#             # Display user message
#             self.chat_display.config(state='normal')
#             self.chat_display.insert(tk.END, f"You: {user_message}\n")
#             self.chat_display.config(state='disabled')
#             self.entry.delete(0, tk.END)  # Clear entry field
#             self.respond(user_message)
#
#     # Generate bot response
#     def respond(self, user_message):
#         self.results_display.config(state='normal')
#         self.results_display.delete(1.0, tk.END)  # Clear previous results
#         self.results_display.insert(tk.END, "Bot: Searching the web for information...\n")
#         self.results_display.config(state='disabled')
#
#         # Perform web scraping
#         self.scrape_web(user_message)
#
#     # Web scraping function
#     def scrape_web(self, query):
#         search_url = f"https://www.google.com/search?q={query}+web+technologies"
#         headers = {"User-Agent": "Mozilla/5.0"}
#         response = requests.get(search_url, headers=headers)
#
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, "html.parser")
#             results = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')  # Assuming the results are in div tags with these classes
#
#             self.results_display.config(state='normal')
#             for result in results[:5]:  # Display top 5 relevant results
#                 self.results_display.insert(tk.END, result.text + "\n\n")
#             self.results_display.config(state='disabled')
#
# # Main application entry point
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = MainApp(root)
#     root.geometry("300x200")
#     root.mainloop()

# import tkinter as tk
# from tkinter import scrolledtext
# import requests
# from bs4 import BeautifulSoup
#
#
# # Main application class
# class MainApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Chatbot Selector")
#
#         # Main interface: label and buttons to select chatbot
#         self.label = tk.Label(root, text="Choose a Chatbot to Start:")
#         self.label.pack(pady=20)
#
#         self.python_button = tk.Button(root, text="Python Chatbot", command=self.open_python_chatbot)
#         self.python_button.pack(pady=10)
#
#         self.webtech_button = tk.Button(root, text="Web Technologies Chatbot", command=self.open_webtech_chatbot)
#         self.webtech_button.pack(pady=10)
#
#     # Open Python chatbot window
#     def open_python_chatbot(self):
#         self.new_window = tk.Toplevel(self.root)
#         self.python_chatbot = PythonChatbot(self.new_window)
#
#     # Open Web Technologies chatbot window
#     def open_webtech_chatbot(self):
#         self.new_window = tk.Toplevel(self.root)
#         self.webtech_chatbot = WebTechChatbot(self.new_window)
#
#
# # Python chatbot class
# class PythonChatbot:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Python Chatbot")
#
#         # Chat display area
#         self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
#         self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
#
#         # Input field for user messages
#         self.entry = tk.Entry(root)
#         self.entry.pack(padx=10, pady=(0, 10), fill=tk.X)
#         self.entry.bind("<Return>", self.send_message)  # Bind Enter key to send message
#
#         # Send button
#         self.send_button = tk.Button(root, text="Send", command=self.send_message)
#         self.send_button.pack(pady=(0, 10))
#
#         # Initial bot greeting
#         self.chat_display.config(state='normal')
#         self.chat_display.insert(tk.END,
#                                  "Bot: Hello! Ask me anything about Python programming. Give me the word e.g loops, functions, etc.\n")
#         self.chat_display.config(state='disabled')
#
#     # Handle sending user message
#     def send_message(self, event=None):
#         user_message = self.entry.get()
#         if user_message:
#             # Display user message
#             self.chat_display.config(state='normal')
#             self.chat_display.insert(tk.END, f"You: {user_message}\n")
#             self.chat_display.config(state='disabled')
#             self.entry.delete(0, tk.END)  # Clear entry field
#             self.respond(user_message)
#
#     # Generate bot response
#     def respond(self, user_message):
#         self.chat_display.config(state='normal')
#         self.chat_display.insert(tk.END, "Bot: Searching the web for information...\n")
#         self.chat_display.config(state='disabled')
#
#         # Perform web scraping
#         self.scrape_web(user_message)
#
#     # Web scraping function
#     def scrape_web(self, query):
#         self.chat_display.config(state='normal')
#         self.chat_display.delete(1.0, tk.END)  # Clear previous results
#         self.chat_display.config(state='disabled')
#
#         search_url = f"https://www.google.com/search?q={query}+python"
#         headers = {"User-Agent": "Mozilla/5.0"}
#
#         try:
#             response = requests.get(search_url, headers=headers)
#             response.raise_for_status()  # Check for request errors
#
#             soup = BeautifulSoup(response.text, "html.parser")
#             results = soup.find_all('div',
#                                     class_='BNeawe s3v9rd AP7Wnd')  # Assuming the results are in div tags with these classes
#
#             self.chat_display.config(state='normal')
#             for result in results[:5]:  # Display top 5 relevant results
#                 self.chat_display.insert(tk.END, result.text + "\n\n")
#             self.chat_display.config(state='disabled')
#         except requests.exceptions.RequestException as e:
#             self.chat_display.config(state='normal')
#             self.chat_display.insert(tk.END, f"Error: {str(e)}\n")
#             self.chat_display.config(state='disabled')
#
#
# # Web Technologies chatbot class
# class WebTechChatbot:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Web Technologies Chatbot")
#
#         # Chat display area
#         self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
#         self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
#
#         # Input field for user messages
#         self.entry = tk.Entry(root)
#         self.entry.pack(padx=10, pady=(0, 10), fill=tk.X)
#         self.entry.bind("<Return>", self.send_message)  # Bind Enter key to send message
#
#         # Send button
#         self.send_button = tk.Button(root, text="Send", command=self.send_message)
#         self.send_button.pack(pady=(0, 10))
#
#         # Initial bot greeting
#         self.chat_display.config(state='normal')
#         self.chat_display.insert(tk.END, "Bot: Hello! Ask me anything about HTML, CSS, JavaScript, or PHP.\n")
#         self.chat_display.config(state='disabled')
#
#     # Handle sending user message
#     def send_message(self, event=None):
#         user_message = self.entry.get()
#         if user_message:
#             # Display user message
#             self.chat_display.config(state='normal')
#             self.chat_display.insert(tk.END, f"You: {user_message}\n")
#             self.chat_display.config(state='disabled')
#             self.entry.delete(0, tk.END)  # Clear entry field
#             self.respond(user_message)
#
#     # Generate bot response
#     def respond(self, user_message):
#         self.chat_display.config(state='normal')
#         self.chat_display.insert(tk.END, "Bot: Searching the web for information...\n")
#         self.chat_display.config(state='disabled')
#
#         # Perform web scraping
#         self.scrape_web(user_message)
#
#     # Web scraping function
#     def scrape_web(self, query):
#         self.chat_display.config(state='normal')
#         self.chat_display.delete(1.0, tk.END)  # Clear previous results
#         self.chat_display.config(state='disabled')
#
#         search_url = f"https://www.google.com/search?q={query}+web+technologies"
#         headers = {"User-Agent": "Mozilla/5.0"}
#
#         try:
#             response = requests.get(search_url, headers=headers)
#             response.raise_for_status()  # Check for request errors
#
#             soup = BeautifulSoup(response.text, "html.parser")
#             results = soup.find_all('div',
#                                     class_='BNeawe s3v9rd AP7Wnd')  # Assuming the results are in div tags with these classes
#
#             self.chat_display.config(state='normal')
#             for result in results[:5]:  # Display top 5 relevant results
#                 self.chat_display.insert(tk.END, result.text + "\n\n")
#             self.chat_display.config(state='disabled')
#         except requests.exceptions.RequestException as e:
#             self.chat_display.config(state='normal')
#             self.chat_display.insert(tk.END, f"Error: {str(e)}\n")
#             self.chat_display.config(state='disabled')
#
#
# # Main application entry point
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = MainApp(root)
#     root.geometry("400x400")
#     root.mainloop()


import tkinter as tk
from tkinter import scrolledtext
import requests
from bs4 import BeautifulSoup


# Main application class
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot Selector")

        # Main interface: label and buttons to select chatbot
        self.label = tk.Label(root, text="Choose a Chatbot to Start:")
        self.label.pack(pady=20)

        self.python_button = tk.Button(root, text="Python Chatbot", command=self.open_python_chatbot)
        self.python_button.pack(pady=10)

        self.webtech_button = tk.Button(root, text="Web Technologies Chatbot", command=self.open_webtech_chatbot)
        self.webtech_button.pack(pady=10)

    # Open Python chatbot window
    def open_python_chatbot(self):
        self.new_window = tk.Toplevel(self.root)
        self.python_chatbot = PythonChatbot(self.new_window)

    # Open Web Technologies chatbot window
    def open_webtech_chatbot(self):
        self.new_window = tk.Toplevel(self.root)
        self.webtech_chatbot = WebTechChatbot(self.new_window)


# Python chatbot class
class PythonChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Chatbot")

        # Chat display area
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Input field for user messages
        self.entry = tk.Entry(root)
        self.entry.pack(padx=10, pady=(0, 10), fill=tk.X)
        self.entry.bind("<Return>", self.send_message)  # Bind Enter key to send message

        # Send button
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(pady=(0, 10))

        # Initial bot greeting
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END,
                                 "Bot: Hello! Ask me anything about Python programming. Give me the word e.g loops, functions, etc.\n")
        self.chat_display.config(state='disabled')

    # Handle sending user message
    def send_message(self, event=None):
        user_message = self.entry.get()
        if user_message:
            # Display user message
            self.chat_display.config(state='normal')
            self.chat_display.insert(tk.END, f"You: {user_message}\n")
            self.chat_display.config(state='disabled')
            self.entry.delete(0, tk.END)  # Clear entry field
            self.respond(user_message)

    # Generate bot response
    def respond(self, user_message):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, "Bot: Searching the web for information...\n")
        self.chat_display.config(state='disabled')

        # Perform web scraping
        self.scrape_web(user_message)

    # Web scraping function
    def scrape_web(self, query):
        self.chat_display.config(state='normal')
        self.chat_display.delete(1.0, tk.END)  # Clear previous results
        self.chat_display.config(state='disabled')

        search_url = f"https://www.google.com/search?q={query}+python"
        headers = {"User-Agent": "Mozilla/5.0"}

        try:
            response = requests.get(search_url, headers=headers)
            response.raise_for_status()  # Check for request errors

            soup = BeautifulSoup(response.text, "html.parser")
            results = soup.find_all('div',
                                    class_='BNeawe s3v9rd AP7Wnd')  # Assuming the results are in div tags with these classes

            self.chat_display.config(state='normal')
            for result in results[:5]:  # Display top 5 relevant results
                self.chat_display.insert(tk.END, result.text + "\n\n")
            self.chat_display.config(state='disabled')
        except requests.exceptions.RequestException as e:
            self.chat_display.config(state='normal')
            self.chat_display.insert(tk.END, f"Error: {str(e)}\n")
            self.chat_display.config(state='disabled')


# Web Technologies chatbot class
class WebTechChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Technologies Chatbot")

        # Chat display area
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Input field for user messages
        self.entry = tk.Entry(root)
        self.entry.pack(padx=10, pady=(0, 10), fill=tk.X)
        self.entry.bind("<Return>", self.send_message)  # Bind Enter key to send message

        # Send button
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(pady=(0, 10))

        # Initial bot greeting
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, "Bot: Hello! Ask me anything about HTML, CSS, JavaScript, or PHP.\n")
        self.chat_display.config(state='disabled')

    # Handle sending user message
    def send_message(self, event=None):
        user_message = self.entry.get()
        if user_message:
            # Display user message
            self.chat_display.config(state='normal')
            self.chat_display.insert(tk.END, f"You: {user_message}\n")
            self.chat_display.config(state='disabled')
            self.entry.delete(0, tk.END)  # Clear entry field
            self.respond(user_message)

    # Generate bot response
    def respond(self, user_message):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, "Bot: Searching the web for information...\n")
        self.chat_display.config(state='disabled')

        # Perform web scraping
        self.scrape_web(user_message)

    # Web scraping function
    def scrape_web(self, query):
        self.chat_display.config(state='normal')
        self.chat_display.delete(1.0, tk.END)  # Clear previous results
        self.chat_display.config(state='disabled')

        search_url = f"https://www.google.com/search?q={query}+web+technologies"
        headers = {"User-Agent": "Mozilla/5.0"}

        try:
            response = requests.get(search_url, headers=headers)
            response.raise_for_status()  # Check for request errors

            soup = BeautifulSoup(response.text, "html.parser")
            results = soup.find_all('div',
                                    class_='BNeawe s3v9rd AP7Wnd')  # Assuming the results are in div tags with these classes

            self.chat_display.config(state='normal')
            for result in results[:5]:  # Display top 5 relevant results
                self.chat_display.insert(tk.END, result.text + "\n\n")
            self.chat_display.config(state='disabled')
        except requests.exceptions.RequestException as e:
            self.chat_display.config(state='normal')
            self.chat_display.insert(tk.END, f"Error: {str(e)}\n")
            self.chat_display.config(state='disabled')


# Main application entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.geometry("400x400")
    root.mainloop()

