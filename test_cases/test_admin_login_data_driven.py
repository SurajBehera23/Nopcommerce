from selenium.webdriver.chrome import webdriver
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from utilities import excel_utils


class Test01_Admin_Login:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    logger = Log_Maker.log_gen()

    def test_valid_admin_login(self, setup):
        self.logger.info("**********test_valid_admin_login Started**********")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        actual_dashboard_text = self.driver.find_element(By.XPATH, "//div[@class='content-header']/h1").text
        expected_dashboard_text = "Dashboard"
        if actual_dashboard_text == expected_dashboard_text:
            self.logger.info("**********test_valid_admin_login Passed**********")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshot\\test_valid_admin_login.png")
            self.logger.info("**********test_valid_admin_login failed**********")
            self.driver.close()
            assert False
