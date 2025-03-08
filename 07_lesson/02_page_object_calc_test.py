from pages_calc.Calkulator import Calkulator
from selenium import webdriver


def test_calc():
    browser = webdriver.Chrome()
    calc = Calkulator(browser)
    calc.calc("45")
    browser.quit()
