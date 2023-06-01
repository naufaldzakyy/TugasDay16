import unittest  # framework automtion etsting
from selenium import webdriver  # mau pake web driver buat pake selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import baseLogin
from PageObject.locator import elem
from PageObject.data import inputan


class TestCart(unittest.TestCase):  # test scenario
    def setUp(self):
        self.browser = webdriver.Chrome(
            ChromeDriverManager().install()
        )  # ini auto install webdriver

    def test_add_cart(self):  # test cases 2
        baseUrl = "https://www.saucedemo.com/"
        driver = self.browser
        driver.get(inputan.baseUrl)
        baseLogin.test_success_login(driver)

        driver.find_element(By.CSS_SELECTOR, elem.addCart).click()
        driver.find_element(By.CLASS_NAME, elem.cart).click(0)
        url = driver.get.current_url()
        self.assertIn(url, baseUrl + "/cart.html")

    if __name__ == "__main__":
        unittest.main()
