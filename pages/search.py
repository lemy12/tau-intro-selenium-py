from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class DuckDuckGoSearchPage:
    URL = 'https://www.duckduckgo.com'

    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')
    SEARCH_BUTTON = (By.ID, 'search_button_homepage')
    AUTOSUGGESTION = (By.CLASS_NAME, 'acp')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)
        search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        ActionChains(self.browser).move_to_element(search_button).click().perform()

    def write_search_phrase(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)
        ActionChains(self.browser).move_to_element(search_input).click().perform()

    def autosuggestion_table(self):
        elements = self.browser.find_elements(*self.AUTOSUGGESTION)
        table = [e.text for e in elements]
        return table

    def search_by_autosuggestion(self):
        elements = self.browser.find_elements(*self.AUTOSUGGESTION)
        first_element_text = elements[1].text
        ActionChains(self.browser).move_to_element(elements[1]).click().perform()
        return first_element_text
