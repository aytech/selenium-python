import os
import re
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class RunChromeTests(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        driver_location = os.path.abspath("C:\\bin\\chromedriver.exe")
        self.driver = webdriver.Chrome(options=chrome_options, executable_path=driver_location)
        app_url = 'https://mingle-ci01-portal.mingle.awsdev.infor.com'
        tenant_id = 'CI_TST'
        idm_logical_id = 'lid://infor.daf.daf'
        self.driver.get(
            "{}/{}?favoriteContext=$screenId=daf_search&LogicalId={}".format(app_url, tenant_id, idm_logical_id))
        login_button = self.driver.find_element_by_link_text("Cloud Identities")
        login_button.click()

        username_field = self.driver.find_element_by_id("username")
        password_field = self.driver.find_element_by_id("password")
        submit_button = self.driver.find_element_by_link_text("Sign On")

        username_field.send_keys("")
        password_field.send_keys("")
        submit_button.click()

        # wait for app switcher
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "mhdrAppBtn")))
        # wait for first frame
        # WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "iframe")))
        # find client top frame
        WebDriverWait(self.driver, 10).until(expected_conditions.frame_to_be_available_and_switch_to_it(
            (By.XPATH, "//iframe[contains(@name, \"daf_\")]")))
        WebDriverWait(self.driver, 20).until(
            expected_conditions.frame_to_be_available_and_switch_to_it((By.ID, "clientFrame")))
        # frame_elements = self.driver.find_elements_by_tag_name("iframe")
        # self.driver.switch_to.frame(0)
        # self.driver.switch_to.frame(client_parent_frame)
        # print(len(frame_elements))
        # for frame in self.driver.find_elements_by_tag_name("iframe"):
        #     is_idm = re.search("daf_", frame.get_attribute("name"))
        #     if is_idm is not None:
        #         self.driver.switch_to.frame(frame)
        #         print("Frame match: ", is_idm.group(0))
        # self.driver.switch_to.frame(0)
        # WebDriverWait(self.driver, 20).until(expected_conditions.frame_to_be_available_and_switch_to_it(
        #     (By.XPATH, "//iframe[contains(@name, \"daf_\")]")))

    def test_search_element_exists(self):
        # First switch to frame that holds the app

        # print(self.driver.find_element_by_id("clientFrame"))
        # print(self.driver.find_element_by_xpath("//iframe[contains(@name, \"daf_\")]"))
        # self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[contains(@name, \"daf_\")]"))
        print("Body: ", self.driver.find_element_by_tag_name("body").get_attribute("id"))
        # Client frame is the direct descendant
        # print(self.driver.find_element_by_tag_name("body").get_attribute("id"))
        # print(self.driver.find_element_by_id("search-dropdown"))
        # self.assertTrue(self.driver.find_elements_by_id("search-dropdown"))
