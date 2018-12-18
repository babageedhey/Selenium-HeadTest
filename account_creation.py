import unittest
import time


import os

from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from user_creation_form import *

parser = ConfigParser()
options = webdriver.ChromeOptions()

parser.read("credentials.ini")

class AccountCreation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Jide\Desktop\Training\Projects\LinuxJobberProject\Testing\chromedriver.exe")
        self.driver.maximize_window()

    def test_account_creation_owner(self):

        self.driver.get('http://18.236.106.129:5100/home')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_class_name('sign_up').click()
        email = parser.get('createuser_owner', 'email')
        password = parser.get('createuser_owner', 'password')
        full_name = parser.get('createuser_owner', 'full_name')
        project_name = parser.get('createuser_owner', 'project_name')
        self.driver.find_element_by_id('email').send_keys(email)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_id('full_name').send_keys(full_name)
        element = self.driver.find_element_by_css_selector("input[type='radio'][value='Owner']")
        self.driver.execute_script("arguments[0].click()", element)
        self.driver.find_element_by_id('projname').send_keys(project_name)
        self.driver.find_element_by_id('create_user').click()
        message = self.driver.find_element_by_xpath('/html/body/app-root/app-user/div[2]/div/div/div[2]/h4[1]')
        time.sleep(3)
        if (message.text == "User Created Successfully"):
            print ("User creation for Owner passed")
            self.assertIn("User Created Successfully" ,  message.text )
        else :
            print ("user creation for Owner failed")
            print (message.text)

    def test_account_creation_qa(self):

        self.driver.get('http://18.236.106.129:5100/home')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_class_name('sign_up').click()
        #send details from the credentials file
        send_details_qa(self)
        self.driver.find_element_by_id('create_user').click()
        message = self.driver.find_element_by_xpath('/html/body/app-root/app-user/div[2]/div/div/div[2]/h4[1]')
        time.sleep(3)
        print (message.text)
        print ('User creation for QA ')


    def test_account_creation_admin(self):
        self.driver.get('http://18.236.106.129:5100/home')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_class_name('sign_up').click()
        #send details from the credentials file
        send_details_admin(self)
        self.driver.find_element_by_id('create_user').click()
        message = self.driver.find_element_by_xpath('/html/body/app-root/app-user/div[2]/div/div/div[2]/h4[1]')
        time.sleep(3)
        print (message.text)
        print('User creation for admin')


    def test_account_creation_dev(self):
        self.driver.get('http://18.236.106.129:5100/home')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_class_name('sign_up').click()
        #send details from the credentials file
        send_details_dev(self)
        self.driver.find_element_by_id('create_user').click()
        message = self.driver.find_element_by_xpath('/html/body/app-root/app-user/div[2]/div/div/div[2]/h4[1]')
        time.sleep(3)
        print (message.text)
        print ('User creation for developer')


    def tearDown(self):

        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()