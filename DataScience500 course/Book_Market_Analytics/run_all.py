# Data Science 500 - Book Market Analytics
# Run the full pipeline in order (PyCharm: right-click -> Run)
# Skip scrape if books_raw.csv already exists (saves ~10-15 min)

import os
import runpy

# set working directory to this file's folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

steps = [
    ("01_scrape.py", "Scrape Books to Scrape (optional if books_raw.csv exists)"),
    ("02_clean.py", "Clean data -> books_clean.csv"),
    ("03_visualise.py", "Charts -> charts/"),
    ("04_model.py", "Linear regression on price"),
]

print("Book Market Analytics - full pipeline")
print("=" * 50)

for script, label in steps:
    if script == "01_scrape.py" and os.path.exists("books_raw.csv"):
        print("SKIP", script, "- books_raw.csv already present")
        continue
    print("RUN ", script, "-", label)
    runpy.run_path(script, run_name="__main__")
    print()

print("Done. Check books_clean.csv and charts/")
