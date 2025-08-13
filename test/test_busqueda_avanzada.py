import pytest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=ChromeService())
    driver.get('https://thefreerangetester.github.io/sandbox-automation-testing/')
    yield driver
    driver.quit()

def test_checkbox(browser):
    #Ubicar el elemento contenedor de los checkbox
    contenedor_checkboxes = browser.find_element(By.CLASS_NAME, "mt-3")
    #Dentro del contenedor, ubicar el checkbox para hamburguesa por su id
    checkbox_hamburguesa = contenedor_checkboxes.find_element(By.ID, "checkbox-1")
    #Interaccion con el checkbox (le hace click si no está seleccionado
    if not checkbox_hamburguesa.is_selected():
        checkbox_hamburguesa.click()
        time.sleep(1)
    #Validación de que el checkbox está seleccionado
    assert checkbox_hamburguesa.is_selected()

def hover_over_enviar(browser):
    #Localizae wl botón por su testo usando xpath
    button = WebDriverWait(browser, 10).until(
        presence_of_element_located(
            (By.XPATH, "//button[CONTAINS (text(), 'Enviar')]")  # Localiza el botón por su texto
        )
    )
    color_before_hover = button.value_of_css_property("background-color")
    ActionChains(browser).move_to_element(button).perform()
    WebDriverWait(browser, 10).until(
        lambda driver: button.value_of_css_property("background-color") != color_before_hover
    )
    color_after_hover = button.value_of_css_property("background-color")
    assert color_before_hover != color_after_hover



