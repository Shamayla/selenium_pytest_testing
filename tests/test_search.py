"""
These tests covers DuckDuckGo search
"""
from pages.search import SearchPage
from pages.result import ResultPage

def test_basic_duckduckgo_search(browser):
    
    searchpage = SearchPage(browser)
    resultpage = ResultPage(browser)

    PHRASE = 'panda'
    ## Given the DuckDuckGo home page is displayed - ARRANGE
    searchpage.load()

    ## When the user searched for "panda" - ACT
    searchpage.search(PHRASE)

    ## Then the search result title contains "panda" - ASSERT
    assert PHRASE in resultpage.title()

    ## And the search result query contains "panda" - ASSERT
    assert PHRASE in resultpage.search_input_value()
    
    ## And the search result links pretain to "panda" - ASSERT
    titles = resultpage.result_link_titles()
    matches  = [t for t in titles if PHRASE.lower() in t.lower()]
    assert len(matches) > 0
