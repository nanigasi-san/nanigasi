"""Example usage of MechanicalSoup to get the results from
DuckDuckGo."""

import mechanicalsoup

# Connect to duckduckgo
browser = mechanicalsoup.StatefulBrowser()
browser.open("https://github.com")

button_list = browser.get_current_page().find_all("button")
for button in button_list:
    print(button)
    print("="*30)
