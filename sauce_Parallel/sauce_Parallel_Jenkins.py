#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import time
import os
import sys
from selenium import webdriver
import sauceclient
import json
import new

SAUCE_USERNAME = os.environ.get('SAUCE_USERNAME')
SAUCE_ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')

test_result = sauceclient.SauceClient(SAUCE_USERNAME, SAUCE_ACCESS_KEY)

onDemandBrowsers = os.environ.get('SAUCE_ONDEMAND_BROWSERS')
data = json.loads(onDemandBrowsers)
print type (data)

class DesktopTest(unittest.TestCase):
    def setUp(self):
        for i in range(lent):
            self.desired_capabilities = {}
            self.desired_capabilities['browserName'] = data[i]['browser']
            self.desired_capabilities['platform'] = data[i]['platform']
            self.desired_capabilities['version'] = data[i]['version']
            self.desired_capabilities['name'] = 'test %s' (i)
            self.driver = webdriver.Remote(command_executor = ('http://' + SAUCE_USERNAME + ':' + SAUCE_ACCESS_KEY + '@ondemand.saucelabs.com:80/wd/hub'), desired_capabilities = self.desired_capabilities)
            self.driver.implicitly_wait(30)

    def test_google(self):
        self.driver.get('https://www.google.com.tw/')
        title = self.driver.title
        self.assertEquals("Google", title)
        time.sleep(2)
        val = self.driver.find_element_by_xpath('//*[@id="lst-ib"]')
        val.send_keys('python')
        val.submit()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[1]/div/h3/a').click()
        
    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        #using the sauce client to set the pass or fail flags for this test according to the assertions results.
        try:
            if sys.exc_info() == (None, None, None):
                test_result.jobs.update_job(self.driver.session_id, passed=True)
            else:
                test_result.jobs.update_job(self.driver.session_id, passed=False)
        finally:
            self.driver.quit()

if __name__ == '__main__':
    thread.start_new_thread(unittest.main())
