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
from selenium.webdriver import ActionChains

parser = ConfigParser()
options = webdriver.ChromeOptions()

parser.read("credentials.ini")



class MoveGoal(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Jide\Desktop\Training\Projects\LinuxJobberProject\Testing\chromedriver.exe")
        self.driver.maximize_window()

    # def test_hour_removed(self):
    #     login(self)
    #     element = self.driver.find_element_by_xpath('//*[@id="g62"]/div')
    #     WT_column = self.driver.find_element_by_id('0')
    #     #Drag element from target to source
    #     action_chains = ActionChains(self.driver)
    #     action_chains.drag_and_drop(element, WT_column).perform() 
    #     time.sleep(2)
    #     user_name = self.driver.find_element_by_xpath('//*[@id="author"]/a')
    #     hours = user_name.text[11: ]
    #     print(hours)


    # def test_move_WG_Done(self):
    #     login(self)
    #     element = self.driver.find_element_by_class_name("list_div")
    #     WT_column = self.driver.find_element_by_id('1')
    #     #Drag element from target to source
    #     action_chains = ActionChains(self.driver)
    #     action_chains.drag_and_drop(element, WT_column).perform()
    #     time.sleep(2)
    #     move_status = self.driver.find_element_by_xpath("/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3")
    #     print(move_status.text)
    #     time.sleep(2)
    #     #locate the element to ove from DT to verify
    #     element = self.driver.find_element_by_class_name('list_div')
    #     DT_column = self.driver.find_element_by_id('2')
    #     #Drag element from target to source
    #     action_chains = ActionChains(self.driver)
    #     action_chains.drag_and_drop(element, DT_column).perform()
    #     time.sleep(2)
    #     move_status = self.driver.find_element_by_xpath("/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3")
    #     print(move_status.text)
    #     #locate the element to move from verify to done
    #     element = self.driver.find_element_by_class_name('list_div')
    #     Verify_column = self.driver.find_element_by_id('3')
    #     #Drag element from verify to done
    #     action_chains = ActionChains(self.driver)
    #     action_chains.drag_and_drop(element, Verify_column).perform()
    #     time.sleep(2)
    #     move_status = self.driver.find_element_by_xpath("/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3")
    #     print(move_status.text)


    # def test_move_goal_Verify_Done(self):
    #     login(self)
    #     #Locate the element to move from WG to DT
    #     element = self.driver.find_element_by_xpath('//*[@id="g63"]/div')
    #     Verify_column = self.driver.find_element_by_id('3')
    #     #Drag element from target to source
    #     action_chains = ActionChains(self.driver)
    #     action_chains.drag_and_drop(element, Verify_column).perform() 
    #     time.sleep(2)
    #     move_status =  self.driver.find_element_by_xpath("/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3")
    #     print (move_status.text)
    #     self.assertAlmostEqual('Goal Moved Successfully!', move_status.text)


    # def test_move_goal_DT_Verify_dev(self):
    #     login_dev(self)
    #     #Locate the element to move from WG to DT
    #     element = self.driver.find_element_by_xpath('//*[@id="g24"]/div')
    #     DT_column = self.driver.find_element_by_xpath('//*[@id="u5"]/div[3]')
    #     #Drag element from target to source
    #     action_chains = ActionChains(self.driver)
    #     action_chains.drag_and_drop(element, DT_column).perform()
    #     time.sleep(2)
    #     prompt = self.driver.switch_to.alert
    #     self.assertIn("How many hours did you spend on this task?" , prompt.text)
    #     prompt.send_keys('4 hours')
    #     prompt.accept()
    #     time.sleep(3)
    #     move_status = self.driver.find_element_by_xpath("/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3")
    #     print(move_status.text)
    #     print ('Move goal by Developer to Verify wth Hours added')
    #     self.assertAlmostEqual('Goal Moved Successfully! Hours Applied!', move_status.text)

    # def test_move_goal_WG_DT_dev(self):
    #     login_dev(self)
    #     #Locate the element to move
    #     element = self.driver.find_element_by_xpath('//*[@id="g24"]/div')
    #     DT_column = self.driver.find_element_by_xpath('//*[@id="u5"]/div[2]')
    #     #Drag element from target to source
    #     action_chains = ActionChains(self.driver)
    #     action_chains.drag_and_drop(element, DT_column).perform()
    #     time.sleep(3)
    #     move_status = self.driver.find_element_by_xpath("/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3")
    #     print (move_status.text)
    #     print ('Goal moved Successfully... result above')
    


    #QA Move tasks functions
    def test_qa_move_goal_DT_Verify(self):
        login(self)
        #Locate the element to move from WG to DT
        element = self.driver.find_element_by_class_name('//*[@id="g25"]/div')
        Verify_column = self.driver.find_element_by_xpath('//*[@id="u5"]/[@id="2"]')
        #Drag element from target to source
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, Verify_column).perform()
        time.sleep(2)
        prompt = self.driver.switch_to.alert
        self.assertIn("How many hours did you spend on this task?" , prompt.text)
        prompt.send_keys('4 hours')
        prompt.accept()
        move_status = self.driver.find_element_by_xpath("/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3")
        print(move_status.text)
        self.assertAlmostEqual('Goal Moved Successfully! Hours Applied!', move_status.text)


    # def test_qa_move_goal_WT_DT(self):
    #     login(self)
    #     #Locate the element to move
    #     element = self.driver.find_element_by_xpath('//*[@id="g25"]/div')
    #     DT_column = self.driver.find_element_by_xpath('//*[@id="u5"]/[@id="1"]')
    #     #Drag element from target to source
    #     action_chains = ActionChains(self.driver)
    #     action_chains.drag_and_drop(element, DT_column).perform()
    #     time.sleep(2)
    #     move_status = self.driver.find_element_by_xpath("/html/body/app-root/app-profile/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/h3")
    #     print(move_status.text)
    #     self.assertAlmostEqual('Goal Moved Successfully!', move_status.text)

    def tearDown(self):

        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()



