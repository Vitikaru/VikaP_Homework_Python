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
        "https://www.saucedemo.com/")

    driver.find_element(
        By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(
        By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    driver.find_element(
        By.CSS_SELECTOR, "#shopping_cart_container > a").click()

    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    driver.find_element(
        By.CSS_SELECTOR, "#first-name").send_keys("Виктория")
    driver.find_element(
        By.CSS_SELECTOR, "#last-name").send_keys("Пржанова")
    driver.find_element(
        By.CSS_SELECTOR, "#postal-code").send_keys("628301")
    driver.find_element(
        By.CSS_SELECTOR, "#continue").click()

    WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "div.summary_total_label"), "$58.29"))
    assert "$58.29" in driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text

    driver.quit()
