from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
click = '[onclick="addElement()"]'
search_input = driver.find_element(By.CSS_SELECTOR, click)
for x in range(1, 6):
    search_input.send_keys(click, Keys.ENTER)
delete = driver.find_elements(By.CSS_SELECTOR, '[onclick="deleteElement()"]')
print(len(delete))
sleep(10)
