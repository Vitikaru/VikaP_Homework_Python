import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    driver.find_element(By.CSS_SELECTOR, "#delay").clear()
    driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(45)

    driver.find_element(
        By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)").click()
    driver.find_element(
        By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(4)").click()
    driver.find_element(
        By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(2)").click()
    driver.find_element(
        By.CSS_SELECTOR,
        "#calculator > div.keys > span.btn.btn-outline-warning").click()

    WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '[class="screen"]'), "15")
        )

    assert "15" in driver.find_element(
        By.CSS_SELECTOR, '[class="screen"]').text
