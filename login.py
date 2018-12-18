import unittest
import time

import os

from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_function import *

parser = ConfigParser()
options = webdriver.ChromeOptions()

parser.read("credentials.ini")


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Jide\Desktop\Training\Projects\LinuxJobberProject\Testing\chromedriver.exe")
        self.driver.maximize_window()

    def test_login_valid_owner(self):
        login_owner(self)
        time.sleep(2)
        current_page = self.driver.current_url
        welcome_message = self.driver.find_element_by_xpath('/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3')
        
        if ( welcome_message.text == 'Welcome!'):
            print ('Login Successful for Owner')
            print (welcome_message.text)
        else:
            print ('Login failed for Owner')
            print (current_page)
        
    def test_login_valid_qa(self):
        login_qa(self)
        time.sleep(2)
        current_page = self.driver.current_url
        welcome_message = self.driver.find_element_by_xpath('/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3')
        
        if ( welcome_message.text == 'Welcome!'):
            print ('Login Successful for QA')
            print (welcome_message.text)
        else:
            print ('Login failed for QA')
            print (current_page)

    def test_login_valid_admin(self):
        login_admin(self)
        time.sleep(2)
        current_page = self.driver.current_url
        welcome_message = self.driver.find_element_by_xpath('/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3')
        
        if ( welcome_message.text == 'Welcome!'):
            print ('Login Successful for Admin')
            print (welcome_message.text)
        else:
            print ('Login failed for Admin')
            print (current_page)

    def test_login_valid_dev(self):
        login_dev(self)
        time.sleep(2)
        current_page = self.driver.current_url
        welcome_message = self.driver.find_element_by_xpath('/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3')
        
        if ( welcome_message.text == 'Welcome!'):
            print ('Login Successful for Developer')
            print (welcome_message.text)
        else:
            print ('Login failed for Developer')
            print (current_page)

    def tearDown(self):

        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()