import unittest  # framework automtion etsting
from selenium import webdriver  # mau pake web driver buat pake selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PageObject.locator import elem
from PageObject.data import inputan


def test_success_login(driver):  # test cases 2
    baseUrl = "https://www.saucedemo.com/"

    driver.get(baseUrl)
    driver.find_element(By.ID, elem.username).send_keys(
        inputan.validuser
    )  # sendkeys itu untuk inputan
    driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys(
        inputan.validpass
    )
    driver.find_element(By.NAME, elem.loginButton).click()
