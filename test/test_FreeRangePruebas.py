import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser():
    # Setup:Initialize teh chrome browser
    driver = webdriver.Chrome(service=ChromeService())
    driver.get('https://www.freerangetesters.com')
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_navegacion_free_range_web(browser):
    # Test: Navigate to Free Range Web
    browser.find_element(By.XPATH, '/html/body/div[1]/div/section/div/header/nav/ul/li[2]/a').click()

