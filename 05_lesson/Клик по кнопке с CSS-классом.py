from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install(), options=options))
driver.get("http://uitestingplayground.com/classattr")
click = "button.btn-primary"
button = driver.find_element(By.CSS_SELECTOR, click)
button.click()
sleep(10)
