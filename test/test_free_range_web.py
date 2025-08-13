import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time



driver = webdriver.Chrome(service=ChromeService())
driver.implicitly_wait(10)  # Espera implícita de 10 segundos


@pytest.mark.regression
def test_free_range_web():
     #Navegar  a la pagina de inicio
    driver.get("https://www.freerangetesters.com/")
    driver.maximize_window()
    cursos = driver.find_element(By.XPATH,'//*[@id="page_header"]/div/section/div/header/nav/ul/li[2]/a')
    cursos.click()