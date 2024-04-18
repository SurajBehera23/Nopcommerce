from selenium.webdriver.chrome import webdriver
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Login_Admin_Page import Login_Admin_Page
class Test01_Admin_Login:
    admin_page_url = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = "admin@yourstore.com"
    password = "admin"
    invalid_username = "admin@yourstored.com"

    def test_title_verification(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)
        actual_title=self.driver.title
        expected_title="Your store. Login"
        if actual_title==expected_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".//screenshot//test_title_verification.png")
            self.driver.close()
            assert False

    def test_valid_admin_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)
        self.admin_lp=Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        actual_dashboard_text=self.driver.find_element(By.XPATH,"//div[@class='content-header']/h1").text
        expected_dashboard_text="Dashboard"
        if actual_dashboard_text==expected_dashboard_text:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".//screenshot//test_valid_admin_login.png")
            self.driver.close()
            assert False

    def test_invalid_admin_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        actual_error_text = self.driver.find_element(By.XPATH, "//div[@class='message-error validation-summary-errors']/ul").text
        expected_error_text = "No customer account found"
        if actual_error_text == expected_error_text:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".//screenshot//test_invalid_admin_login.png")
            self.driver.close()
            assert False

