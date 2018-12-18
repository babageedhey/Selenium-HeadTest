import unittest
import time
import os

from login_function import *
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

    def test_change_role_qa(self):
        #Login as owner to test
        self.driver.get('http://18.236.106.129:5100')
        self.driver.implicitly_wait(30)
        login_owner(self)
        #click the settings button to change role 
        time.sleep(3)
        #Click the settings of the second user to change role
        self.driver.find_element_by_xpath('.//*[@id="m6"]/tbody/tr/div/a[1]').click()
       
        #Send message to the input field to add goal
        
        prompt = self.driver.switch_to.alert
        self.assertIn("Change User Role" , prompt.text)
        time.sleep(2)
        prompt.send_keys('Quality Analyst')
        self.driver.implicitly_wait(2)
        time.sleep(2)
        prompt.accept()
        time.sleep(3)
        message = self.driver.find_element_by_xpath('/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3')
        if (message.text == 'User Role Changed!'):
            print ('User Role Changed Passed for QA')
            self.assertEqual ('User Role Changed!', message.text)
        else:
            print ('User Role changed Failed')
        
    def test_change_role_admin(self):
        #Login as owner to test
        self.driver.get('http://18.236.106.129:5100')
        self.driver.implicitly_wait(30)
        login_owner(self)
        #click the settings button to change role 
        time.sleep(3)
        #Click the settings of the second user to change role
        self.driver.find_element_by_xpath('.//*[@id="m4"]/tbody/tr/div/a[1]').click()
       
        #Send message to the input field to add goal
        
        prompt = self.driver.switch_to.alert
        self.assertIn("Change User Role" , prompt.text)
        time.sleep(2)
        prompt.send_keys('Admin')
        self.driver.implicitly_wait(2)
        time.sleep(2)
        prompt.accept()
        time.sleep(3)
        message = self.driver.find_element_by_xpath('/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3')
        if (message.text == 'User Role Changed!'):
            print ('User Role Changed Passed for Admin')
            self.assertEqual ('User Role Changed!', message.text)
        else:
            print ('User Role changed Failed')    
  
        
    def tearDown(self):

        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()