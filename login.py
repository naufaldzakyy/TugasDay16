import unittest  # framework automtion etsting
from selenium import webdriver  # mau pake web driver buat pake selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import baseLogin
from PageObject.locator import elem


class TestLogin(unittest.TestCase):  # test scenario
    def setUp(self):
        self.browser = webdriver.Chrome(
            ChromeDriverManager().install()
        )  # ini auto install webdriver

    def test_failed_login(self):  # test cases 1
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, elem.username).send_keys("haitest")
        driver.find_element(By.NAME, elem.loginButton).click()
        error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        self.assertIn("Epic sadface: Password is required", error_message)

    def test_success_login(self):  # test cases 2
        driver = self.browser
        baseUrl = "https://www.saucedemo.com/"
        driver.get(baseUrl)
        baseLogin.test_success_login
        driver.find_element(By.NAME, elem.loginButton).click()


# def test_success_add(self): #test case 3
#     driver = self.browser
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()


if __name__ == "__main__":
    unittest.main()
