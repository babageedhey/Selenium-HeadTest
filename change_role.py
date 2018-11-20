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

class ChangeRole(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Jide\Desktop\Training\Projects\LinuxJobberProject\Testing\chromedriver.exe")
        self.driver.maximize_window()

    def test_change_role_owner(self):
        #Login to chatscrum
        self.driver.get('http://live.chatscrum.com/home')
        self.driver.implicitly_wait(30)
        username = parser.get('chatscrum.com/valid_login', 'username')
        password = parser.get('chatscrum.com/valid_login', 'password')
        project_title = parser.get('chatscrum.com/valid_login', 'project')
        self.driver.find_element_by_id('login_username').send_keys(username)
        self.driver.find_element_by_id('login_password').send_keys(password)
        self.driver.find_element_by_id('login_project').send_keys(project_title)
        self.driver.find_element_by_class_name('submit').click()
        time.sleep(2)
        #clic the settings button to change role 
        self.driver.implicitly_wait(10)
        element = self.driver.find_element_by_id("settings")
        self.driver.execute_script("arguments[0].click()", element)
        #Send message to the input field to add goal
        prompt = self.driver.switch_to.alert
        self.assertIn("Change User Role" , prompt.text)
        prompt.send_keys('Owner')
        prompt.accept()
        self.driver.implicitly_wait(10)
        # message = self.driver.find_element_by_css_selector("h3")
        # self.assertTrue('Error ', message)
        
        

   
        

    def tearDown(self):

        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()