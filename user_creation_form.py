#Form to send the details to fill the form for user creation
import os

from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

parser = ConfigParser()
options = webdriver.ChromeOptions()

parser.read("credentials.ini")

def send_details_qa(self):
    self.driver.get('http://18.236.106.129:5100/createuser')
    self.driver.implicitly_wait(10)
    email = parser.get('createuser_qa', 'email')
    password = parser.get('createuser_qa', 'password')
    full_name = parser.get('createuser_qa', 'full_name')
    self.driver.find_element_by_id('email').send_keys(email)
    self.driver.find_element_by_id('password').send_keys(password)
    self.driver.find_element_by_id('full_name').send_keys(full_name)

def send_details_admin(self):
    self.driver.get('http://18.236.106.129:5100/createuser')
    self.driver.implicitly_wait(10)
    email = parser.get('createuser_admin', 'email')
    password = parser.get('createuser_admin', 'password')
    full_name = parser.get('createuser_admin', 'full_name')
    self.driver.find_element_by_id('email').send_keys(email)
    self.driver.find_element_by_id('password').send_keys(password)
    self.driver.find_element_by_id('full_name').send_keys(full_name)

def send_details_dev(self):
    self.driver.get('http://18.236.106.129:5100/createuser')
    self.driver.implicitly_wait(10)
    email = parser.get('createuser_dev', 'email')
    password = parser.get('createuser_dev', 'password')
    full_name = parser.get('createuser_dev', 'full_name')
    self.driver.find_element_by_id('email').send_keys(email)
    self.driver.find_element_by_id('password').send_keys(password)
    self.driver.find_element_by_id('full_name').send_keys(full_name)
