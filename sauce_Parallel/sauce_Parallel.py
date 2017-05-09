#coding=utf-8
import unittest, optparse, time, os
from selenium import webdriver
from array import *
import multiprocessing
import Queue
#import sauceclient
# Declaring the Suace list of browsers
SAUCEBROWSER = {
 'firefox': webdriver.DesiredCapabilities.FIREFOX,
 'ie': webdriver.DesiredCapabilities.INTERNETEXPLORER,
 'opera': webdriver.DesiredCapabilities.OPERA,
 'chrome':webdriver.DesiredCapabilities.CHROME,
 'edge':webdriver.DesiredCapabilities.EDGE,
 'Safari':webdriver.DesiredCapabilities.SAFARI
}
# Declaring the Sauce OS environnment
SAUCEOS = {
 'xp': 'Windows xp',
 'winxp': 'Windows XP',
 'win2003': 'Windows 2003',
 'win2008': 'Windows 2008',
 'linux': 'Linux',
 'win10':'Windows 10',
 'win8':'Windows 8',
 'win8.1':'Windows 8.1',
 'win7':'Windows 7',
 'mac':'Mac 10.12'
}
test_result = sauceclient.SauceClient(sauce_userid, sauce_apikey)

class Selenium2OnSauce(unittest.TestCase):
    def setUp(self,s_browsers,s_userid,s_apikey,b_video,b_screenshot,s_testname):
      self.s_browsers = s_browsers
      self.s_userid = s_userid
      self.s_apikey = s_apikey
      self.s_testname = s_testname
      self.b_video = b_video
      self.b_screenshot = b_screenshot
      browser, version, os = self.s_browsers.split('-')
           
      desired_capabilities = SAUCEBROWSER[browser.lower()].copy()
      desired_capabilities['version'] = version if version.lower() != 'latest' else ''
      desired_capabilities['platform'] = SAUCEOS[os.lower()]
      desired_capabilities['name'] = self.s_testname
      desired_capabilities['record-video'] = self.b_video
      desired_capabilities['record-screenshots'] = self.b_screenshot
      self.driver = webdriver.Remote(desired_capabilities = desired_capabilities,command_executor = "http://{user}:{key}@{host}:{port}/wd/hub".format(user=self.s_userid, key=self.s_apikey, host="ondemand.saucelabs.com", port="80"))
      self.driver.implicitly_wait(30)
    def test_sauce(self):
        self.driver.get('https://www.lingvist.com.tw/')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/ul/li[5]/a').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/section[4]/section/main/footer/button[4]').click()
        self.driver.find_element_by_xpath('/html/body/div[3]/section[4]/section/main/main/form/div[1]/input').send_keys('mac31010@gmail.com')
        self.driver.find_element_by_xpath('/html/body/div[3]/section[4]/section/main/main/form/div[2]/input').send_keys('gp6nj4')
        self.driver.find_element_by_xpath('/html/body/div[3]/section[4]/section/main/footer/button').click()
        time.sleep(2)

    def tearDown(self):
      print "Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id
      self.driver.quit()

      try:
            if sys.exc_info() == (None, None, None):
                test_result.jobs.update_job(self.driver.session_id, passed=True)
            else:
                test_result.jobs.update_job(self.driver.session_id, passed=False)
      finally:
            self.driver.quit()

def worker(l_browsers,s_suite,sauce_userid,sauce_apikey,sauce_video,sauce_screenshots,test_name):
  for test in s_suite:
             job_queue = multiprocessing.Queue()
             job_queue.put(test.setUp(l_browsers,sauce_userid,sauce_apikey,sauce_video,sauce_screenshots,test_name))
             job_queue.put(test.test_sauce())
             job_queue.put(test.tearDown())
             job_queue.put(unittest.TextTestRunner().run(s_suite))
             
if __name__ == '__main__':
      parser = optparse.OptionParser(usage='usage: %prog [options]')
      parser.set_defaults(
        sauce_video=True,
        sauce_screenshots=True,
                         )
      parser.add_option('--sauce-user', action='store', dest='sauce_userid')
      parser.add_option('--sauce-key', action='store', dest='sauce_apikey')
      parser.add_option('--sauce-video', action='store_true', dest='sauce_video')
      parser.add_option('--sauce-screenshots', action='store_true', dest='sauce_screenshots')
      parser.add_option('--testName', action='store', dest='test_name')
      parser.add_option('--browser', action='store', dest='browser')
 
      o, args = parser.parse_args()
      arr_browser = []
      jobs = []
      arr_browser = o.browser.split(',') 
      suite = unittest.TestLoader().loadTestsFromTestCase(Selenium2OnSauce)
      for j in arr_browser:
          p = multiprocessing.Process(target=worker,args=(j,suite,o.sauce_userid,o.sauce_apikey,o.sauce_video,o.sauce_screenshots,o.test_name))
          jobs.append(p)
          p.start()
