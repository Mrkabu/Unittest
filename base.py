import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.google.pl')
        return self.driver

    def test1(self):
        self.driver.find_element_by_xpath('//*[@id="lst-ib"]').send_keys('siała baba mak' + Keys.ENTER)
        time.sleep(5)
        a = self.driver.find_element_by_xpath('/html/body/div[5]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div/div/h3/a')
        action = ActionChains(self.driver)
        action.move_to_element(a)
        time.sleep(3)
        if a.is_displayed():
            print('Hurra!!! Działa')
            a.click()
        else:
            print('Nie ma tego elementu')


if __name__ == '__main__':
    unittest.main()
