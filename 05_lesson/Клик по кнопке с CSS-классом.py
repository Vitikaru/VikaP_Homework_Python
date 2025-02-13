from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install(), options=options))
driver.get("http://uitestingplayground.com/classattr")
click = "button.btn-primary"
search_input = driver.find_element(By.CSS_SELECTOR, click)
search_input.send_keys(click, Keys.ENTER)
sleep(10)
