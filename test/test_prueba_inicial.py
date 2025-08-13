import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService())

def test_inicial():
    driver.get("https://www.freerangetesters.com")
    titulo = driver.title
    assert titulo == "Free Range Testers"



