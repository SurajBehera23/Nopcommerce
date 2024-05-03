from selenium.webdriver.chrome import webdriver
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from utilities import excel_utils


class Test02_Admin_Login_data_driven:
    admin_page_url = Read_Config.get_admin_page_url()
    path = ".//test_data//admin_login_data.xlsx"
    logger = Log_Maker.log_gen()

    def test_valid_admin_login_data_driven(self, setup):
        self.logger.info("**********test_valid_admin_login_data_driven Started**********")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)

        self.rows=excel_utils.get_row_count(self.path,"Sheet1")
        print("num of rows= ", self.rows)

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
