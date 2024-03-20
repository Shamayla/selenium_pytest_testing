"""
This is page object model of DuckDuckGo Result page
"""
from selenium.webdriver.common.by import By

class ResultPage:
    # URL
    URL = "https://duckduckgo.com/"

    # Locators
    #RESULT_LINKS = ("//a[@data-testid='result-title-a']/span")
    RESULT_LINKS = (By.CSS_SELECTOR ,"a[data-testid='result-title-a']")
    ORGANIC_RESULT_LINKS = (By.CSS_SELECTOR, "li[data-layout='organic'] a[data-testid='result-title-a']")
    SEARCH_INPUT = (By.ID, "search_form_input")
    MORE_RESULTS = (By.CSS_SELECTOR, "#more-results")
    MORE_RESULTS_LINKS = (By.XPATH, "//div[@aria-label='Page 2']//following::a[@data-testid='result-title-a']")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def title(self):
        return self.browser.title

    def search_input_value(self):
        search_input_value = self.browser.find_element(*self.SEARCH_INPUT).get_attribute('value')
        return search_input_value

    def result_link_titles(self):
        result_links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in result_links]
        return titles
    
    def load_result_page(self, query):
        self.URL = self.URL + "?q=" + query
        self.browser.get(self.URL)
    
    def click_result_link(self):
        result_links = self.browser.find_elements(*self.ORGANIC_RESULT_LINKS)
        result_links[0].click()

    def page_url(self):
        return self.browser.current_url
    
    def click_more_result(self):
        self.browser.find_element(*self.MORE_RESULTS).click()
        pass

    def more_result_link_titles(self):
        more_result_links = self.browser.find_elements(*self.MORE_RESULTS_LINKS)
        more_result_titles = [titles.text for titles in more_result_links]
        return more_result_titles
