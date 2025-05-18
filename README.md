# Google Maps Business Scraper

This project contains two scripts to automate the process of extracting business data from Google Maps URLs.

## 📂 Overview

1. `convert_csv_to_json.py`: Converts a CSV file with URL columns into a JSON array.
2. `fallback_playwright_scraper.py`: Uses Playwright to scrape business data from the URLs in `links.json`.

---

## 🛠️ Requirements

- Python 3.7+
- Google Chrome or Chromium (Playwright downloads its own headless version)
- pip (Python package manager)

---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/google-maps-scraper.git
   cd google-maps-scraper


### Install the Python dependencies:
pip install -r requirements.txt
playwright install


🚀 Usage
Run both scripts using the run_all.py script:
python run_all.py


Or run them individually:
1. Convert CSV to JSON:
  python convert_csv_to_json.py
2. Scrape the data:
  python fallback_playwright_scraper.py



📁 Outputs
links.json: List of cleaned Google Maps URLs (generated from the CSV).

output_results.csv: Final scraped results.

failed_links.csv: Any URLs that failed during scraping.

