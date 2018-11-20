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

class AccountCreation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Jide\Desktop\Training\Projects\LinuxJobberProject\Testing\chromedriver.exe")
        self.driver.maximize_window()

    def test_account_creation_owner(self):

        self.driver.get('http://live.chatscrum.com/home')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_class_name('sign_up').click()
        email = parser.get('chatscrum.com/createuser', 'email')
        password = parser.get('chatscrum.com/createuser', 'password')
        full_name = parser.get('chatscrum.com/createuser', 'full_name')
        self.driver.find_element_by_id('email').send_keys(email)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_id('full_name').send_keys(full_name)
        element = self.driver.find_element_by_css_selector("input[type='radio'][value='Owner']")
        self.driver.execute_script("arguments[0].click()", element)
        self.driver.find_element_by_id('projname').send_keys('project-alpha')
        self.driver.find_element_by_id('create_user').click()
        # message = self.driver.find_element_by_tag_name('h4')
        # self.driver.implicitly_wait(10)
        # self.assertIn("User Created Successfully" ,  message )

    def test_account_creation_user(self):

        self.driver.get('http://live.chatscrum.com/home')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_class_name('sign_up').click()
        email = parser.get('chatscrum.com/createuser_dev', 'email')
        password = parser.get('chatscrum.com/createuser_dev', 'password')
        full_name = parser.get('chatscrum.com/createuser_dev', 'full_name')
        self.driver.find_element_by_id('email').send_keys(email)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_id('full_name').send_keys(full_name)
        self.driver.find_element_by_id('create_user').click()
        # message = self.driver.find_elements_by_tag_name('h4[1]')
        # self.driver.implicitly_wait(10)
        # self.assertEqual("User Created Successfully",  message )


    def tearDown(self):

        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()