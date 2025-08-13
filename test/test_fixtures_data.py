import pytest
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser():
    # Setup:Initialize teh chrome browser
    driver = webdriver.Chrome(service=ChromeService())
    driver.get('https://www.google.com')
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

#Funcion auxiliar para leer datos de un archivo CSV
def read_search_terms():
    with open("C:/Users/Mel/PycharmProjects/Selenium/TestData/Book(Hoja1).csv", newline = '') as csvfile:
        data = list(csv.reader(csvfile))
        #devuelve solo los terminos de busqueda, excluyendo el titulo de la columna
        return [row[0] for row in data[1:]]

#Fixture para parametrizar los terminos de busqueda leídos desde el archivo CSV
@pytest.fixture(params=read_search_terms())
def termino_de_busqueda(request):
    return request.param

def test_google_busqueda(browser,  termino_de_busqueda):
    # Test: Perform a search on Google
    search_box = browser.find_element("name", "q")
    search_box.send_keys(termino_de_busqueda + Keys.RETURN)

    results = browser.find_element("id", "search")
    assert len (results.find_elements('xpath','.//div')) > 0, "No results found for the search term."
