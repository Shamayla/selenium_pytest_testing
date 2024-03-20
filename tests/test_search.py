"""
These tests covers DuckDuckGo search
"""
from pages.search import SearchPage
from pages.result import ResultPage
import pytest

@pytest.mark.basic
@pytest.mark.parametrize('phrase',['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser, phrase):
    
    searchpage = SearchPage(browser)
    resultpage = ResultPage(browser)

    #PHRASE = 'panda'
    ## Given the DuckDuckGo home page is displayed - ARRANGE
    searchpage.load()

    ## When the user searched for "panda" - ACT
    searchpage.search_with_return_key(phrase)

    ## Then the search result query contains "panda" - ASSERT
    assert phrase in resultpage.search_input_value()
    
    ## And the search result links pretain to "panda" - ASSERT
    titles = resultpage.result_link_titles()
    matches  = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    ## And the search result title contains "panda" - ASSERT
    assert phrase in resultpage.title()

@pytest.mark.basic
@pytest.mark.parametrize('phrase',['panda'])
def test_basic_duckduckgo_search_with_button_click(browser, phrase):
    
    searchpage = SearchPage(browser)
    resultpage = ResultPage(browser)

    ## Given the DuckDuckGo home page is displayed - ARRANGE
    searchpage.load()

    ## When the user searches for "panda" by clicking search button - ACT
    searchpage.search_with_button_click(phrase)

    ## Then the search result query is "panda" - ASSERT
    assert phrase in resultpage.search_input_value()

@pytest.mark.click
@pytest.mark.parametrize('query',['panda'])
def test_click_a_search_result(browser, query):

    resultpage = ResultPage(browser)

    ##Given the DuckDuckGo result page is displayed with search results for "panda" - ARRANGE
    resultpage.load_result_page(query)

    ##When the user clicks a search result link - ACT 
    resultpage.click_result_link()

    ##Then the new page is opened with title having phrase "panda" - ASSERT
    assert query in resultpage.title().lower()

    ##And the new page link contains phrase "panda" - ASSERT
    assert query in resultpage.page_url()

@pytest.mark.click
@pytest.mark.parametrize('query',['panda'])
def test_more_results(browser, query):

    resultpage = ResultPage(browser)
    # Given the DuckDuckGo result page is displayed with search results for "panda"
    resultpage.load_result_page(query)
    # When the user click More Results button
    resultpage.click_more_result()
    # Then the additional search result links are displayed # count > 0
    titles = resultpage.more_result_link_titles()
    assert len(titles) > 0
    # And these search result links pertain to "panda"
    matches = [t for t in titles if query in t.lower()]
    print(matches)
    assert len(matches) > 0