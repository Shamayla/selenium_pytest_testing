"""
These tests covers DuckDuckGo search
"""
from pages.search import SearchPage
from pages.result import ResultPage

def test_basic_duckduckgo_search(browser):
    
    searchpage = SearchPage(browser)
    resultpage = ResultPage(browser)

    PHRASE = 'panda'
    ## Given the DuckDuckGo home page is displayed
    #Arrange
    searchpage.load()

    ## When the user searched for "panda"
    searchpage.search(PHRASE)

    ## Then the search result title contains "panda"
    assert PHRASE in resultpage.title()

    ## And the search result query contains "panda"
    assert PHRASE in resultpage.search_input_value()
    
    ## And the search result links pretain to "panda"
    titles = resultpage.result_link_titles()
    matches  = [t for t in titles if PHRASE.lower() in t.lower()]
    assert len(matches) > 0