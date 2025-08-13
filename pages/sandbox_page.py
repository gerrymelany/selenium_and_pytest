from selenium.webdriver.common.by import By
from .base_page import BasePage

class SandboxPage(BasePage):
    enviar_button_locator = (By.XPATH, "//button[contains(text(), 'Enviar')]")
    dynamic_id_button_locator = (By.XPATH, "//button[contains(text(), 'Hacé click para generar un ID dinámico y mostrar el elemento oculto')]")
    hidden_text_label = (By.XPATH, "//label[contains(text(), 'OMG, aparezco después de 3 segundos de haber hecho click en el botón')]")

    def navigate_sandbox(self):
        self.navigate_to("https://thefreerangetester.github.io/sandbox-automation-testing/")

    def click_enviar(self):
        self.click(self.enviar_button_locator)

    def click_dynamic_button(self):
        self.click(self.dynamic_id_button_locator)