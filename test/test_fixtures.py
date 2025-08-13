import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(params=['playright', 'selenium', 'cypress'])
def termino_de_busqueda(request):
    return request.param


@pytest.fixture()
def browser():
    # Setup:Initialize teh chrome browser
    driver = webdriver.Chrome(service=ChromeService())
    driver.get('https://www.google.com')
    yield driver
    driver.quit()

def test_google_busqueda(browser,  termino_de_busqueda):
    # Test: Perform a search on Google
    search_box = browser.find_element("name", "q")
    search_box.send_keys(termino_de_busqueda + Keys.RETURN)

    results = browser.find_element("id", "search")
    assert len (results.find_elements('xpath','.//div')) > 0, "No results found for the search term."
