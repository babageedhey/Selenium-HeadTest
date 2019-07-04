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

from login_function import *

parser = ConfigParser()
options = webdriver.ChromeOptions()

parser.read("credentials.ini")



class AddTask(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Jide\Desktop\Training\Projects\LinuxJobberProject\Testing\chromedriver.exe")
        self.driver.maximize_window()

    #Owner Function test
    def test_add_task_owner(self):
        login_owner(self)
        #click the add button
        self.driver.find_element_by_id('add').click()
        self.driver.implicitly_wait(10)
        #Send message to the input field to add goal
        self.driver.find_element_by_id('goal').send_keys('New Task Added 2')
        #click the Add task button
        self.driver.find_element_by_xpath("//*[@type='submit']").click()
        time.sleep(3)
        message = self.driver.find_element_by_xpath('/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3')
        print (message.text)
        print ('Goal added or not see message above')

    def test_delete_task_owner(self):
        login_owner(self)
        #locate the delete the button to delete a task by moving mouse over
        action_chains = ActionChains(self.driver)
        element = self.driver.find_element_by_class_name('list_div')
        delete_button = self.driver.find_element_by_class_name('delete_task')
        #hover over a task
        action_chains.move_to_element(element)
        action_chains.click(delete_button)
        action_chains.perform()
        time.sleep(3)
        message = self.driver.find_element_by_xpath('/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3')
        print (message.text)
        print ('Delete Task or not see message above')

    def test_edit_task_owner(self):
        login_owner(self)
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
        message = self.driver.find_element_by_xpath('/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3')
        print (message.text)
        print ('Edit Task or not see message above')

    #QA functions Add Edit and Delete    
    def test_add_task_qa(self):
        login_qa(self)
        #click the add button
        self.driver.find_element_by_xpath('//*[@id="m6"]/tbody/tr/div/a[2]').click()
        self.driver.implicitly_wait(10)
        #Send message to the input field to add goal
        self.driver.find_element_by_id('goal').send_keys('New Task Added for QA')
        #click the Add task button
        self.driver.find_element_by_xpath("//*[@type='submit']").click()
        time.sleep(3)
        message = self.driver.find_element_by_xpath('/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3')
        print (message.text)
        print ('Goal added by QA or not see message above')


    def test_edit_task_qa(self):
        login_qa(self)
        #Double click a goal to open the edit task
        action_chains = ActionChains(self.driver)
        element = self.driver.find_element_by_xpath('//*[@id="g12"]/div')
        action_chains.move_to_element(element)
        action_chains.double_click(element)
        action_chains.perform()
        #Switch to the prompt to edit
        prompt = self.driver.switch_to.alert
        self.assertIn("Editing Task ID" , prompt.text)
        prompt.send_keys('This task is been edited')
        prompt.accept()
        time.sleep(3)
        message = self.driver.find_element_by_xpath('/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3')
        print (message.text)
        print ('Edit Task by QA or not see message above')

    def test_delete_task_qa(self):
        login_qa(self)
        #locate the delete the button to delete a task by moving mouse over
        action_chains = ActionChains(self.driver)
        element = self.driver.find_element_by_xpath('//*[@id="g13"]/div')
        delete_button = self.driver.find_element_by_class_name('delete_task')
        #hover over a task
        action_chains.move_to_element(element)
        action_chains.click(delete_button)
        action_chains.perform()
        time.sleep(3)
        message = self.driver.find_element_by_xpath('/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3')
        print (message.text)
        print ('Delete Task by QA or not see message above')

    #Admin function for add edit and delete
    def test_add_task_admin(self):
        login_admin(self)
        #click the add button
        self.driver.find_element_by_xpath('//*[@id="m4"]/tbody/tr/div/a[2]').click()
        self.driver.implicitly_wait(10)
        #Send message to the input field to add goal
        self.driver.find_element_by_id('goal').send_keys('New Task Added for Admin 2')
        #click the Add task button
        self.driver.find_element_by_xpath("//*[@type='submit']").click()
        time.sleep(3)
        message = self.driver.find_element_by_xpath('/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3')
        print (message.text)
        print ('Goal added by Admin or not see message above')

    def test_edit_task_admin(self):
        login_admin(self)
        #Double click a goal to open the edit task
        action_chains = ActionChains(self.driver)
        element = self.driver.find_element_by_xpath('//*[@id="g17"]/div')
        action_chains.move_to_element(element)
        action_chains.double_click(element)
        action_chains.perform()
        #Switch to the prompt to edit
        prompt = self.driver.switch_to.alert
        self.assertIn("Editing Task ID" , prompt.text)
        prompt.send_keys('This task is been edited')
        prompt.accept()
        time.sleep(3)
        message = self.driver.find_element_by_xpath('/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3')
        print (message.text)
        print ('Edit Task by ADmin or not see message above')

    def test_delete_task_admin(self):
        login_admin(self)
        #locate the delete the button to delete a task by moving mouse over
        action_chains = ActionChains(self.driver)
        element = self.driver.find_element_by_xpath('//*[@id="g19"]/div')
        delete_button = self.driver.find_element_by_class_name('delete_task')
        #hover over a task
        action_chains.move_to_element(element)
        action_chains.click(delete_button)
        action_chains.perform()
        time.sleep(3)
        message = self.driver.find_element_by_xpath('/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3')
        print (message.text)
        print ('Delete Task by Admin or not see message above')

    #Developers Function add, delete and Edit
    def test_add_task_dev(self):
        login_dev(self)
        #click the add button
        self.driver.find_element_by_xpath('//*[@id="m5"]/tbody/tr/div/a[2]').click()
        self.driver.implicitly_wait(10)
        #Send message to the input field to add goal
        self.driver.find_element_by_id('goal').send_keys('New Task Added for Developer 2')
        #click the Add task button
        self.driver.find_element_by_xpath("//*[@type='submit']").click()
        time.sleep(3)
        message = self.driver.find_element_by_xpath('/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3')
        print (message.text)
        print ('Goal added by Developer or not see message above')


    def test_edit_task_dev(self):
        login_dev(self)
        #Double click a goal to open the edit task
        action_chains = ActionChains(self.driver)
        element = self.driver.find_element_by_xpath('//*[@id="g22"]/div')
        action_chains.move_to_element(element)
        action_chains.double_click(element)
        action_chains.perform()
        #Switch to the prompt to edit
        prompt = self.driver.switch_to.alert
        self.assertIn("Editing Task ID" , prompt.text)
        prompt.send_keys('This task is been edited')
        prompt.accept()
        time.sleep(3)
        message = self.driver.find_element_by_xpath('/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3')
        print (message.text)
        print ('Edit Task by developer or not see message above')

    def test_delete_task_dev(self):
        login_dev(self)
        #locate the delete the button to delete a task by moving mouse over
        action_chains = ActionChains(self.driver)
        element = self.driver.find_element_by_xpath('//*[@id="g15"]/div')
        delete_button = self.driver.find_element_by_class_name('delete_task')
        #hover over a task
        action_chains.move_to_element(element)
        action_chains.click(delete_button)
        action_chains.perform()
        time.sleep(3)
        message = self.driver.find_element_by_xpath('/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3')
        print (message.text)
        print ('Delete Task by Developer or not see message above')


      
    def test_add_edit_delete_owner(self):
        login_owner(self)
        #click the add button
        self.driver.find_element_by_id('add').click()
        self.driver.implicitly_wait(10)
        #Send message to the input field to add goal
        self.driver.find_element_by_id('goal').send_keys('All in one Add Edit and Delete Task')
        #click the Add task button
        self.driver.find_element_by_xpath("//*[@type='submit']").click()
        time.sleep(3)
        message = self.driver.find_element_by_xpath('/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3')
        print (message.text)
    

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
        message = self.driver.find_element_by_xpath('/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3')
        print (message.text)
    

        #Delete Task
        #locate the delete the button to delete a task by moving mouse over
        action_chains = ActionChains(self.driver)
        element = self.driver.find_element_by_class_name('list_div')
        delete_button = self.driver.find_element_by_class_name('delete_task')
        #hover over a task
        action_chains.move_to_element(element)
        action_chains.click(delete_button)
        action_chains.perform()
        time.sleep(3)
        message = self.driver.find_element_by_xpath('/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3')
        print (message.text)
        
    

    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()