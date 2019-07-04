
import time

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

def login_owner(self):
    #Login to chatscrum
    self.driver.get('http://18.236.106.129:5100/home')
    self.driver.implicitly_wait(30)
    username = parser.get('valid_login/owner', 'username')
    password = parser.get('valid_login/owner', 'password')
    project_title = parser.get('valid_login/owner', 'project')
    self.driver.find_element_by_id('login_username').send_keys(username)
    self.driver.find_element_by_id('login_password').send_keys(password)
    self.driver.find_element_by_id('login_project').send_keys(project_title)
    self.driver.find_element_by_class_name('submit').click()
    time.sleep(2)


def login_qa(self):
    #Login to chatscrum
    self.driver.get('http://18.236.106.129:5100/home')
    self.driver.implicitly_wait(30)
    username = parser.get('valid_login/qa', 'username')
    password = parser.get('valid_login/qa', 'password')
    project_title = parser.get('valid_login/qa', 'project')
    self.driver.find_element_by_id('login_username').send_keys(username)
    self.driver.find_element_by_id('login_password').send_keys(password)
    self.driver.find_element_by_id('login_project').send_keys(project_title)
    self.driver.find_element_by_class_name('submit').click()
    time.sleep(2)

def login_admin(self):
    #Login to chatscrum
    self.driver.get('http://18.236.106.129:5100/home')
    self.driver.implicitly_wait(30)
    username = parser.get('valid_login/admin', 'username')
    password = parser.get('valid_login/admin', 'password')
    project_title = parser.get('valid_login/admin', 'project')
    self.driver.find_element_by_id('login_username').send_keys(username)
    self.driver.find_element_by_id('login_password').send_keys(password)
    self.driver.find_element_by_id('login_project').send_keys(project_title)
    self.driver.find_element_by_class_name('submit').click()
    time.sleep(2)

def login_dev(self):
    #Login to chatscrum
    self.driver.get('http://18.236.106.129:5100/home')
    self.driver.implicitly_wait(30)
    username = parser.get('valid_login/dev', 'username')
    password = parser.get('valid_login/dev', 'password')
    project_title = parser.get('valid_login/dev', 'project')
    self.driver.find_element_by_id('login_username').send_keys(username)
    self.driver.find_element_by_id('login_password').send_keys(password)
    self.driver.find_element_by_id('login_project').send_keys(project_title)
    self.driver.find_element_by_class_name('submit').click()
    time.sleep(2)