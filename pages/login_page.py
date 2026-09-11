from selenium.webdriver.common.by import By
from .base_page import BasePage
from .inventory_page import InventoryPage

class LoginPage(BasePage):
    username_input_locator = (By.ID, "user-name")
    password_input_locator = (By.ID, "password")
    login_button_locator = (By.ID, "login-button")
    error_message_locator = (By.XPATH, "//h3[contains(.,'Epic sadface')]")

    def navigate_sauce_demo(self):
        self.navigate_to(self.BASE_URL)

    def login_user(self, username, password):
        self.type_text(self.username_input_locator, username)
        self.type_text(self.password_input_locator, password)
        self.click_element(self.login_button_locator)
        if username == "locked_out_user":
            return self  # LoginPage con mensaje de error
        return InventoryPage(self.driver)

    def text_locked_out_user(self):
        return self.get_text(self.error_message_locator)

