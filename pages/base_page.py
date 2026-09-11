from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:
    BASE_URL = "https://www.saucedemo.com/"
    DEFAULT_PASSWORD = "secret_sauce"

    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def reload_page(self):
        self.driver.refresh()

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        element = WebDriverWait(self.driver, timeout=10).until(EC.element_to_be_clickable(locator))
        element.click()

    def hover_over_element(self, locator):
        element = self.wait_for_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def type_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def get_select_options(self, locator):
        """
        Devuelve una lista con los textos visibles de las opciones de un dropdown.
        """
        dropdown = Select(self.wait_for_element(locator))
        return [option.text for option in dropdown.options]

    def select_from_dropdown_by_visible_text(self, locator, text):
        dropdown = Select(self.wait_for_element(locator))
        dropdown.select_by_visible_text(text)

    def get_text(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    def get_title(self):
        return self.driver.title
