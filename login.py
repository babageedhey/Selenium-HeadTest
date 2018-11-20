import unittest
import time

import os

from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

parser = ConfigParser()
options = webdriver.ChromeOptions()

parser.read("credentials.ini")

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Jide\Desktop\Training\Projects\LinuxJobberProject\Testing\chromedriver.exe")
        self.driver.maximize_window()

    def test_login_valid(self):
        self.driver.get('http://live.chatscrum.com/home')
        self.driver.implicitly_wait(30)
        username = parser.get('chatscrum.com/valid_login', 'username')
        password = parser.get('chatscrum.com/valid_login', 'password')
        project_title = parser.get('chatscrum.com/valid_login', 'project')
        self.driver.find_element_by_id('login_username').send_keys(username)
        self.driver.find_element_by_id('login_password').send_keys(password)
        self.driver.find_element_by_id('login_project').send_keys(project_title)
        self.driver.find_element_by_class_name('submit').click()
        self.driver.implicitly_wait(20)
        time.sleep(2)
        current_page = self.driver.current_url
        print (current_page)
        self.assertEqual('http://live.chatscrum.com/profile', self.driver.current_url)
        

    # def test_login_invalid(self):
    #     self.driver.get('http://chatscrum.com/home')
    #     self.driver.implicitly_wait(30)
    #     username = parser.get('chatscrum.com/invalid', 'username')
    #     password = parser.get('chatscrum.com/invalid', 'password')
    #     project_title = parser.get('chatscrum.com/invalid', 'project')
    #     self.driver.find_element_by_id('login_username').send_keys(username)
    #     self.driver.find_element_by_id('login_password').send_keys(password)
    #     self.driver.find_element_by_id('login_project').send_keys(project_title)
    #     self.driver.find_element_by_class_name('submit').click()
    #     time.sleep(2)
    #     current_page = self.driver.current_url
    #     print (current_page)
    #     self.assertEqual('http://chatscrum.com/home', self.driver.current_url)

    def tearDown(self):

        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()