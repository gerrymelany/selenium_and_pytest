from selenium.webdriver.common.by import By
from .base_page import BasePage

class SandboxPage(BasePage):
    enviar_button_locator = (By.XPATH, "//button[contains(text(), 'Enviar')]")
    dynamic_id_button_locator = (By.XPATH, "//button[contains(text(), 'Hacé click para generar un ID dinámico y mostrar el elemento oculto')]")
    hidden_text_label = (By.XPATH, "//label[contains(text(), 'OMG, aparezco después de 3 segundos de haber hecho click en el botón')]")
    checkbox_button_locator = (By.XPATH, "//input[@type='checkbox' and @id='checkbox']")
    deporte_dropdown = (By.ID, "formBasicSelect")
    mostrar_popup_button = (By.XPATH, "//button[@type='button'][contains(.,'Mostrar popup')]")
    popup_title = (By.XPATH, "//div[@class='modal-title h4'][contains(.,'Popup de ejemplo')]")

    def navigate_sandbox(self):
        self.navigate_to("https://thefreerangetester.github.io/sandbox-automation-testing/")

    def click_enviar(self):
        self.click_element(self.enviar_button_locator)

    def click_dynamic_button(self):
        self.click_element(self.dynamic_id_button_locator)

    def select_checkbox(self, label_text):
        assert label_text in ["Pizza", "Hamburguesa", "Pasta", "Helado", "Torta"], "Las opciones aceptadas son: Pizza, Hamburguesa, Pasta, Helado, Torta."
        checkbox_locator = (By.XPATH, f"//label[contains(.,'{label_text}')]")
        self.click_element(checkbox_locator)

    def select_radio_button(self, option):
        assert  option in ["Si", "No"], "Opción inválida. Use 'Si' o 'No'."
        radio_button_locator = (By.XPATH, f"//label[@class='form-check-label' and contains(text(),'{option}')]")
        self.click_element(radio_button_locator)

    def select_deporte(self, deporte):
        assert deporte in ["Fútbol", "Básquet", "Tenis", "Natación"], "Deporte inválido. Use 'Fútbol', 'Básquet', 'Tenis' o 'Natación'."
        self.select_from_dropdown_by_visible_text(self.deporte_dropdown, deporte)

    def get_deporte_dropdown_options(self):
        return self.get_select_options(self.deporte_dropdown)

    def click_button_popup(self):
        self.hover_over_element(self.mostrar_popup_button)
        self.click_element(self.mostrar_popup_button)


    def get_popup_title_text(self):
        return self.wait_for_element(self.popup_title).text

    def get_cell_value(self, fila, columna):
        celda_xpath = f"(//table[@class='table table-striped table-bordered table-hover']/tbody/tr)[{fila}]/td[{columna}]"
        celda = self.wait_for_element((By.XPATH, celda_xpath))
        return celda.text if celda else None

    def get_valor_celda_estatica(self, fila, columna):
        celda_xpath = f"(//h2[normalize-space()='Tabla estática']/following-sibling::table/tbody/tr)[{fila}]/td[{columna}]"
        celda = self.wait_for_element((By.XPATH, celda_xpath))
        return celda.text if celda else None