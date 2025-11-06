import asyncio
import pandas as pd
from playwright.async_api import async_playwright

URL = "https://treibhaus.at/programm"
OUTPUT_FILE = "treibhaus_veranstaltungen.csv"

async def main():
    print(f"Starte Scraping: {URL}")
    async with async_playwright() as p:
        # Fügt das Argument '--no-sandbox' hinzu, um Probleme in manchen Linux-Umgebungen (wie Nix) zu umgehen.
        # WICHTIG: Nutzt 'channel' um eine bereits auf dem System installierte Chromium/Chrome Version zu verwenden, 
        # anstatt sich auf die versionsspezifischen Nix-Pfade zu verlassen, die Playwright intern sucht (z.B. 1187 statt 1181).
        try:
            # Versuche, den System-Chrome zu verwenden
            browser = await p.chromium.launch(args=['--no-sandbox'], channel='chrome')
        except Exception:
            # Wenn Chrome fehlschlägt, versuche den System-Chromium
            browser = await p.chromium.launch(args=['--no-sandbox'], channel='chromium')

        
        page = await browser.new_page()
        await page.goto(URL, wait_until="domcontentloaded")
        print("Navigiert.")
        
        event_data = []
        # Selektor für die einzelnen Event-Container
        event_elements = await page.locator('.event-item').all()
        print(f"Finde {len(event_elements)} Veranstaltungen.")

        for element in event_elements:
            # Daten-Extraktion
            link_element = element.locator('a[itemprop="url"]')
            link = await link_element.get_attribute('href')
            name_element = element.locator('span[itemprop="name"]')
            description_text = await name_element.inner_text()
            full_link = f"https://treibhaus.at{link}" if link and link.startswith('/') else link
            datetime_span = element.locator('span[itemprop="startDate"]')
            datetime_str = await datetime_span.get_attribute('datetime')
            event_date = "N/A"
            start_time = "N/A"

            if datetime_str:
                # Konvertiert den datetime-String in Datum und Zeit
                dt_obj = pd.to_datetime(datetime_str)
                event_date = dt_obj.strftime('%d.%m.%Y')
                start_time = dt_obj.strftime('%H:%M')

            event_data.append({
                "Datum": event_date,
                "Beginnzeit": start_time,
                "Link": full_link,
                "Beschreibungstext": description_text.strip()
            })

        await browser.close()
        print("Browser geschlossen.")
        
        # Speichert die Daten in CSV
        df = pd.DataFrame(event_data)
        df.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')
        print(f"Daten in '{OUTPUT_FILE}' gespeichert. {len(df)} Zeilen.")

if __name__ == "__main__":
    asyncio.run(main())
