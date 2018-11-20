import unittest
import time
import HTMLTestRunner
import os

import login
import account_creation
import move_goal
import change_role
import add_task


direct = os.getcwd()

from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains



class MyTestSuite(unittest.TestCase):

    def test_allTest(self):
        chatscrum_Test = unittest.TestSuite()
        chatscrum_Test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(account_creation.AccountCreation),
            unittest.defaultTestLoader.loadTestsFromTestCase(login.LoginTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(add_task.AddTask),
            unittest.defaultTestLoader.loadTestsFromTestCase(change_role.ChangeRole),
            unittest.defaultTestLoader.loadTestsFromTestCase(move_goal.MoveGoal)
        ])

        outfield = open(direct + "\ChatScrumTest.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream= outfield,
            title= "live.chatscrum.com Test Report",
            description= "An Automated Test for the Components and functions on live.chatscrum.com"
        )

        runner1.run(chatscrum_Test)


if __name__ == '__main__':
    unittest.main()
