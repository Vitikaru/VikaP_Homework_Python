from selenium.webdriver.common.by import By


class ColorCheck():
    def __init__(self, browser):
        self.driver = browser
        self.driver.implicitly_wait(5)

    def color_check_red(self):
        assert "alert py-2 alert-danger" in self.driver.find_element(
            By.CSS_SELECTOR, "#zip-code"
            ).get_attribute("class")

    def color_check_green(self):
        assert "alert py-2 alert-success" in self.driver.find_element(
            By.CSS_SELECTOR, "#first-name"
            ).get_attribute("class")
        assert "alert py-2 alert-success" in self.driver.find_element(
            By.CSS_SELECTOR, "#last-name"
            ).get_attribute("class")
        assert "alert py-2 alert-success" in self.driver.find_element(
            By.CSS_SELECTOR, "#address"
            ).get_attribute("class")
        assert "alert py-2 alert-success" in self.driver.find_element(
            By.CSS_SELECTOR, "#city"
            ).get_attribute("class")
        assert "alert py-2 alert-success" in self.driver.find_element(
            By.CSS_SELECTOR, "#country"
            ).get_attribute("class")
        assert "alert py-2 alert-success" in self.driver.find_element(
            By.CSS_SELECTOR, "#e-mail"
            ).get_attribute("class")
        assert "alert py-2 alert-success" in self.driver.find_element(
            By.CSS_SELECTOR, "#phone"
            ).get_attribute("class")
        assert "alert py-2 alert-success" in self.driver.find_element(
            By.CSS_SELECTOR, "#job-position"
            ).get_attribute("class")
        assert "alert py-2 alert-success" in self.driver.find_element(
            By.CSS_SELECTOR, "#company"
            ).get_attribute("class")
