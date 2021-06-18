import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class TestMain(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.get("https://www.saucedemo.com/")
        cls.password = "secret_sauce" # one password for all users
        cls.valid_users = ["standard_user", "problem_user", "performance_glitch_user"]
        cls.invalid_users = ["locked_out_user"]
        cls.valid_url = "/inventory.html"

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def helper_login(self, user, password):
        self.browser.find_element_by_id('user-name').send_keys(user)
        self.browser.find_element_by_id('password').send_keys(password)
        self.browser.find_element_by_id('login-button').click()

    def helper_logout(self):
        self.browser.find_element_by_id('react-burger-menu-btn').click()
        self.browser.find_element_by_id('logout_sidebar_link').click()

    def test_valid_logins(self):
        for user in self.valid_users:
            self.helper_login(user, self.password)
            if self.valid_url not in self.browser.current_url:
                return False
            self.helper_logout()

    def test_invalid_logins(self):
        for user in self.invalid_users:
            self.helper_login(user, self.password)
            if not self.browser.find_element_by_css_selector('.error-button').is_displayed():
                # if we accidently login logout
                if self.valid_url in self.browser.current_url:
                    self.helper_logout()
                self.browser.get("https://www.saucedemo.com/")
                return False
            self.browser.get("https://www.saucedemo.com/")

    def test_connection(self):
        expected = "Swag Labs"
        if self.browser.title != expected:
            print("Title is invalid")
            return False
        return True

if __name__ == "__main__":
    unittest.main()
