"""
These tests covers DuckDuckGo search
"""
from pages.search import SearchPage
from pages.result import ResultPage
import pytest

@pytest.mark.parametrize('phrase',['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser, phrase):
    
    searchpage = SearchPage(browser)
    resultpage = ResultPage(browser)

    #PHRASE = 'panda'
    ## Given the DuckDuckGo home page is displayed - ARRANGE
    searchpage.load()

    ## When the user searched for "panda" - ACT
    searchpage.search(phrase)

    ## Then the search result query contains "panda" - ASSERT
    assert phrase in resultpage.search_input_value()
    
    ## And the search result links pretain to "panda" - ASSERT
    titles = resultpage.result_link_titles()
    matches  = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    ## And the search result title contains "panda" - ASSERT
    assert phrase in resultpage.title()