import time
from playwright.sync_api import sync_playwright

SCREENSHOT_PATH = "./out/results.png"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://duckduckgo.com")

    search_selector = 'input[name="q"]'
    page.fill(search_selector, "test")

    page.press(search_selector, "Enter")

    time.sleep(1)

    page.screenshot(path=SCREENSHOT_PATH)

    browser.close()
