import unittest  # framework automtion etsting
from selenium import webdriver  # mau pake web driver buat pake selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import baseLogin
from PageObject.locator import elem
from PageObject.data import inputan


class checkout(unittest.TestCase):  # test scenario
    def setUp(self):
        self.browser = webdriver.Chrome(
            ChromeDriverManager().install()
        )  # ini auto install webdriver

    def test_checkout(self):  # test cases 2
        baseUrl = "https://www.saucedemo.com/"
        driver = self.browser
        driver.get(inputan.baseUrl)
        baseLogin.test_success_login(driver)
        driver.find_element(By.ID, "first-name").send_keys("Naufal")
        driver.find_element(By.ID, "last-name").send_keys("Dzaky")
        driver.find_element(By.ID, "postal-code").send_keys("21515")
        driver.find_element(
            By.CLASS_NAME, "submit-button btn btn_primary cart_button btn_action"
        ).click()
        url = driver.get.current_url()
        self.assertIn(url, baseUrl + "/checkout-step-one.html")

    if __name__ == "__main__":
        unittest.main()
