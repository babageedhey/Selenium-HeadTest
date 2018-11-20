import unittest
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

class MoveGoal(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Jide\Desktop\Training\Projects\LinuxJobberProject\Testing\chromedriver.exe")
        self.driver.maximize_window()

    def test_move_goal_Verify_Done(self):
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
        #Locate the element to move from WG to DT
        element = self.driver.find_element_by_class_name('list_div')
        DT_column = self.driver.find_element_by_id('3')
        #Drag element from target to source
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, DT_column).perform()  

    def test_move_goal_DT_Verify(self):
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
        #Locate the element to move from WG to DT
        element = self.driver.find_element_by_class_name('list_div')
        DT_column = self.driver.find_element_by_id('2')
        #Drag element from target to source
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, DT_column).perform()

    def test_move_goal_WG_DT(self):
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
        #Locate the element to move from WG to DT
        element = self.driver.find_element_by_class_name('list_div')
        DT_column = self.driver.find_element_by_id('1')
        #Drag element from target to source
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, DT_column).perform()


    def tearDown(self):

        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()