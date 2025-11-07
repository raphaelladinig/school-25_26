from playwright.sync_api import sync_playwright
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()


def scrape_moodle_courses(username: str, password: str, moodle_url: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        login_url = f"{moodle_url.rstrip('/')}/login/index.php"
        page.goto(login_url, wait_until="domcontentloaded")

        page.fill("#username", username)
        page.fill("#password", password)
        page.click("#loginbtn")

        termin_selector = "#inst52638 .event[data-region='event-item']"
        
        termine = []
        
        for event_div in page.locator(termin_selector).all():
            titel = event_div.locator("h4 a").inner_text().strip()
            
            datum = event_div.locator(".date.small").inner_text().strip()
            
            termine.append({
                "Titel": titel,
                "Datum": datum
            })

        df = pd.DataFrame(termine)
        print(df.head())

        df.to_csv("./out/moodle_termine.csv", index=False, encoding="utf-8-sig")



if __name__ == "__main__":
    scrape_moodle_courses(
        username=os.getenv("MOODLE_USER"),  # type: ignore
        password=os.getenv("MOODLE_PASS"),  # type: ignore
        moodle_url=os.getenv("MOODLE_URL"),  # type: ignore
    )
