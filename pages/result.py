from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class DuckDuckGoResultPage:

    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')
    SEARCH_BUTTON = (By.ID, 'search_button')
    SEARCH_KEYWORDS = (By.XPATH, '//meta[@name="keywords"]')
    SEARCH_FIRST_RESULT = (By.CLASS_NAME, 'result__a')
    MORE_RESULTS = (By.ID, 'rld-1')

    def __init__(self, browser):
        self.browser = browser

    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        return self.browser.title

    def check_first_result(self):
        search_first_result = self.browser.find_element(*self.SEARCH_FIRST_RESULT)
        ActionChains(self.browser).move_to_element(search_first_result).click().perform()

    def search_for_keywords(self):
        search_keywords = self.browser.find_element(*self.SEARCH_KEYWORDS)
        return search_keywords

    def expand_more_results(self):
        more_results = self.browser.find_element(*self.MORE_RESULTS)
        ActionChains(self.browser).move_to_element(more_results).click().perform()

    def search_another_result(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        ActionChains(self.browser).double_click(search_input).perform()
        search_input.send_keys(Keys.BACKSPACE + phrase)
        search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        ActionChains(self.browser).move_to_element(search_button).click().perform()
