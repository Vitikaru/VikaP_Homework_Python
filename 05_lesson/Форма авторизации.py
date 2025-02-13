from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/login")
username = '[name="username"]'
search_input = driver.find_element(By.CSS_SELECTOR, username)
search_input.send_keys("tomsmith")
password = '[name="password"]'
search_input = driver.find_element(By.CSS_SELECTOR, password)
search_input.send_keys("SuperSecretPassword!")
close_button = driver.find_element(By.CSS_SELECTOR, 'button.radius > i')
close_button.click()
sleep(10)
