import allure
from selenium.webdriver.common.by import By


class AddingProduct():

    def __init__(self, browser):
        self.driver = browser
        self.driver.implicitly_wait(5)

    @allure.step("Добавление товаров в корзину")
    def add(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#shopping_cart_container > a").click()

        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
