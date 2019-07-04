import os
import time
import unittest
from configparser import ConfigParser
from  login import LoginTest

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

parser = ConfigParser()
options = webdriver.ChromeOptions()

parser.read("credentials.ini")

class SprintFunction(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Jide\Desktop\Training\Projects\LinuxJobberProject\Testing\chromedriver.exe")
        self.driver.maximize_window()

    # def test_start_new_sprint(self):
    #     #Login to the live.chatscrum.com
    #     self.driver.get('http://live.chatscrum.com/home')
    #     self.driver.implicitly_wait(30)
    #     username = parser.get('chatscrum.com/valid_login', 'username')
    #     password = parser.get('chatscrum.com/valid_login', 'password')
    #     project_title = parser.get('chatscrum.com/valid_login', 'project')
    #     self.driver.find_element_by_id('login_username').send_keys(username)
    #     self.driver.find_element_by_id('login_password').send_keys(password)
    #     self.driver.find_element_by_id('login_project').send_keys(project_title)
    #     self.driver.find_element_by_class_name('submit').click()
    #     time.sleep(10)

    #     #Click the sprint button to start new sprint
    #     self.driver.find_element_by_class_name('s_button').click()
    #     time.sleep(1)
    #     self.driver.implicitly_wait(10)

    #     #switch to prompt to click ok and End current sprint to start new sprint
    #     alert = self.driver.switch_to.alert
    #     alert.accept()
    #     self.driver.implicitly_wait(12)

    def test_check_older_sprint(self):
        #Login to the portal
        self.driver.get('http://live.chatscrum.com/home')
        self.driver.implicitly_wait(30)
        username = parser.get('chatscrum.com/valid_login', 'username')
        password = parser.get('chatscrum.com/valid_login', 'password')
        project_title = parser.get('chatscrum.com/valid_login', 'project')
        self.driver.find_element_by_id('login_username').send_keys(username)
        self.driver.find_element_by_id('login_password').send_keys(password)
        self.driver.find_element_by_id('login_project').send_keys(project_title)
        self.driver.find_element_by_class_name('submit').click()
        time.sleep(10)
        self.driver.find_element_by_css_selector('select').click()
        self.driver.find_elements_by_css_selector('option').click()
       

    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
