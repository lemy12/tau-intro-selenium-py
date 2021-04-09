"""
These tests cover DuckDuckGo searches.
"""
import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


@pytest.mark.basic_duckduckgo_search
@pytest.mark.parametrize('phrase', ['panda'])
def test_basic_duckduckgo_search(browser, phrase):

    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "panda"
    search_page.search(phrase)

    # Then the search result query is "panda"
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to "panda"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    # And the search result title contains "panda"
    assert phrase in result_page.title()


@pytest.mark.click_first_result
def test_click_first_result(browser, phrase='panda'):

    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Load duckduckgo.com page
    search_page.load()

    # Search for phrase and click first result
    search_page.search(phrase)
    result_page.check_first_result()

    # Check if first result contains logo
    keywords = result_page.search_for_keywords().get_attribute("content").lower()
    assert phrase in keywords


@pytest.mark.more_results
def test_more_results(browser, phrase='panda'):

    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Load duckduckgo.com page
    search_page.load()

    # Search for phrase
    search_page.search(phrase)

    # Create table of search result links
    results_before = result_page.result_link_titles()

    # Expand more results and create new table of search result links
    result_page.expand_more_results()
    results_after = result_page.result_link_titles()

    # Check if new table of links has more elements than previous one
    assert len(results_after) > len(results_before)


@pytest.mark.verify_autosuggestion
def test_verify_autosuggestion(browser, phrase='panda'):

    search_page = DuckDuckGoSearchPage(browser)

    # Load duckduckgo.com page
    search_page.load()

    # Write phrase in search textbox
    search_page.write_search_phrase(phrase)

    as_table = search_page.autosuggestion_table()
    matches = [match for match in as_table if match in match]

    assert len(matches) == len(as_table)


@pytest.mark.check_autosuggestion
def test_check_autosuggestion(browser, phrase='panda'):

    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Load duckduckgo.com page
    search_page.load()

    # Write phrase in search textbox
    search_page.write_search_phrase(phrase)

    # Search by clicking on first autosuggestion and return its text
    as_first = search_page.search_by_autosuggestion()

    # Check if results pertain to clicked autosuggestion
    titles = result_page.result_link_titles()
    matches = [t for t in titles if as_first.lower() in t.lower()]
    assert len(matches) > 0


@pytest.mark.search_another_phrase
def test_search_another_phrase(browser, phrase='panda', phrase_new='python'):

    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Load duckduckgo.com page
    search_page.load()

    # Write phrase in search textbox and search
    search_page.search(phrase)

    # Write phrase in search textbox and search again
    result_page.search_another_result(phrase_new)

    # Check if results do not match to previous search phrase
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) == 0

