import allure
from selenium.webdriver.common.by import By


class Authorization:

    def __init__(self, browser):
        self.driver = browser
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    @allure.step("Авторизация на сайте")
    def autho(self, user, sauce):
        self.driver.find_element(By.CSS_SELECTOR, "#user-name"
                                 ).send_keys(user)
        self.driver.find_element(By.CSS_SELECTOR, "#password"
                                 ).send_keys(sauce)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
