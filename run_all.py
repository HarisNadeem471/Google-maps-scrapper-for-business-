import subprocess

print("🌀 Running CSV to JSON conversion...")
subprocess.run(["python", "convert_csv_to_json.py"], check=True)

print("\n🌀 Running fallback scraper...")
subprocess.run(["python", "fallback_playwright_scraper.py"], check=True)

print("\n✅ All steps completed.")
