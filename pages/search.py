"""
This is page object model of DuckDuckGo Search Page
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SearchPage:

    # URL
    URL = "https://duckduckgo.com/"

    #Locators
    SEARCH_INPUT = (By.ID, "searchbox_input")
    SEARCH_BUTTON = (By.XPATH, "//button[@aria-label='Search']")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def load(self):
        self.browser.get(self.URL)

    def search_with_return_key(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT) # Python Thing - Expand Tuples into the positional arguments
        search_input.send_keys(phrase, Keys.RETURN)

    def search_with_button_click(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT) # Python Thing - Expand Tuples into the positional arguments
        search_input.send_keys(phrase)
        search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        search_button.click()
