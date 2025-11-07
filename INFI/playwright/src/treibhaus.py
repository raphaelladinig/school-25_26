import pandas as pd
from playwright.sync_api import sync_playwright
from io import StringIO  #

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    page.goto("https://treibhaus.at/programm")

    events_data = []

    event_titles = page.locator('span[itemprop="name"]').all()

    for title_element in event_titles:
        title = title_element.inner_text().strip()

        event_container = title_element.locator(
            'xpath=./ancestor::div[contains(@class, "item")]'
        ).first

        link_date_anchor = event_container.locator('a[itemprop="url"]').first

        link = link_date_anchor.get_attribute("href")

        events_data.append({"Veranstaltung": title, "Link": link})

    browser.close()

df = pd.DataFrame(events_data)
csv_buffer = StringIO()
df.to_csv(csv_buffer, index=False, sep=";", encoding="utf-8")
csv_output = csv_buffer.getvalue()

print("CSV-Inhalt:\n" + csv_output)
