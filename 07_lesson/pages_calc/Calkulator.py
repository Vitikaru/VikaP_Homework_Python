from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calkulator:

    def __init__(self, browser):
        self.driver = browser
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def calc(self, value):
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(value)
        self.driver.find_element(
            By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)"
            ).click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(4)"
            ).click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(2)"
            ).click()
        self.driver.find_element(
            By.CSS_SELECTOR,
            "#calculator > div.keys > span.btn.btn-outline-warning").click()

        WebDriverWait(self.driver, 45).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '[class="screen"]'), "15"))

        assert "15" in self.driver.find_element(
            By.CSS_SELECTOR, '[class="screen"]').text
