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

class AddTask(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Jide\Desktop\Training\Projects\LinuxJobberProject\Testing\chromedriver.exe")
        self.driver.maximize_window()

    def test_add_task(self):
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
        #click the add button
        self.driver.find_element_by_id('add').click()
        self.driver.implicitly_wait(10)
        #Send message to the input field to add goal
        self.driver.find_element_by_id('goal').send_keys('Another test goal added')
        #click the Add task button
        self.driver.find_element_by_xpath("//*[@type='submit']").click()

    def test_delete_task(self):
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
        #locate the delete the button to delete a task by moving mouse over
        action_chains = ActionChains(self.driver)
        element = self.driver.find_element_by_class_name('list_div')
        delete_button = self.driver.find_element_by_class_name('delete_task')
        #hover over a task
        action_chains.move_to_element(element)
        action_chains.click(delete_button)
        action_chains.perform()

    def test_edit_task(self):
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
        #Double click a goal to open the edit task
        action_chains = ActionChains(self.driver)
        element = self.driver.find_element_by_class_name('list_div')
        action_chains.move_to_element(element)
        action_chains.double_click(element)
        action_chains.perform()
        #Switch to the prompt to edit
        prompt = self.driver.switch_to.alert
        self.assertIn("Editing Task ID" , prompt.text)
        prompt.send_keys('This task is been edited')
        prompt.accept()


    def test_add_edit_delete(self):
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
        #click the add button
        self.driver.find_element_by_id('add').click()
        self.driver.implicitly_wait(10)
        #Send message to the input field to add goal
        self.driver.find_element_by_id('goal').send_keys('All in one Add Edit and Delete Task')
        #click the Add task button
        self.driver.find_element_by_xpath("//*[@type='submit']").click()
        time.sleep(3)
        #Edit Task
        #Double click a goal to open the edit task
        action_chains = ActionChains(self.driver)
        element = self.driver.find_element_by_class_name('list_div')
        action_chains.move_to_element(element)
        action_chains.double_click(element)
        action_chains.perform()
        #Switch to the prompt to edit
        prompt = self.driver.switch_to.alert
        self.assertIn("Editing Task ID" , prompt.text)
        prompt.send_keys('This task is been edited')
        prompt.accept()
        time.sleep(3)

        #Delete Task
        #locate the delete the button to delete a task by moving mouse over
        action_chains = ActionChains(self.driver)
        element = self.driver.find_element_by_class_name('list_div')
        delete_button = self.driver.find_element_by_class_name('delete_task')
        #hover over a task
        action_chains.move_to_element(element)
        action_chains.click(delete_button)
        action_chains.perform()


    
        

    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()