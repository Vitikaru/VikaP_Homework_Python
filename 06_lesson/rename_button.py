from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)
driver.get("http://uitestingplayground.com/textinput")
text = "#newButtonName"
search_input = driver.find_element(By.CSS_SELECTOR, text)
search_input.send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
name_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(name_button)
driver.quit()
