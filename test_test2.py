# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest2():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test2(self):
    # Test name: test2
    # Step # | name | target | value
    # 1 | open | /cabinet/licenses/inProcess | 
    self.driver.get("https://lk-test.egais.ru/cabinet/licenses/inProcess")
    # 2 | setWindowSize | 1854x1048 | 
    self.driver.set_window_size(1854, 1048)
    # 3 | click | css=html | 
    # self.driver.find_element(By.CSS_SELECTOR, "html").click()
    # 4 | click | css=.dx-data-row > .dx-cell-focus-disabled | 
    # self.driver.find_element(By.CSS_SELECTOR, ".dx-data-row > .dx-cell-focus-disabled").click()
    # 5 | click | css=#mat-tab-label-0-1 > .mat-tab-label-content | 
    self.driver.find_element(By.CSS_SELECTOR, "#mat-tab-label-0-1 > .mat-tab-label-content").click()
    # 6 | click | css=#mat-select-value-41 > .mat-select-placeholder | 
    self.driver.find_element(By.CSS_SELECTOR, "#mat-select-value-41 > .mat-select-placeholder").click()
    # 7 | click | css=.mat-option-text | 
    self.driver.find_element(By.CSS_SELECTOR, ".mat-option-text").click()
    # 8 | click | css=.ng-tns-c58-110 > .mat-form-field-infix | 
    self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c58-110 > .mat-form-field-infix").click()
    # 9 | type | id=mat-input-4 | 234
    self.driver.find_element(By.ID, "mat-input-4").send_keys("234")
    # 10 | click | id=mat-select-value-35 | 
    self.driver.find_element(By.ID, "mat-select-value-35").click()
    # 11 | click | css=#mat-option-7 > .mat-option-text | 
    self.driver.find_element(By.CSS_SELECTOR, "#mat-option-7 > .mat-option-text").click()
    # 12 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 13 | click | css=.ng-tns-c88-103 > .mat-select-min-line | 
    self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c88-103 > .mat-select-min-line").click()
    # 14 | click | css=#mat-option-9 > .mat-option-text | 
    self.driver.find_element(By.CSS_SELECTOR, "#mat-option-9 > .mat-option-text").click()
    # 15 | click | css=#mat-option-9 > .mat-option-text | 
    self.driver.find_element(By.CSS_SELECTOR, "#mat-option-9 > .mat-option-text").click()
    # 16 | click | css=.cdk-overlay-backdrop | 
    self.driver.find_element(By.CSS_SELECTOR, ".cdk-overlay-backdrop").click()
    # 17 | click | css=.ng-tns-c88-105 > .mat-select-min-line | 
    self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c88-105 > .mat-select-min-line").click()
    # 18 | click | css=#mat-option-32 > .mat-option-text | 
    self.driver.find_element(By.CSS_SELECTOR, "#mat-option-32 > .mat-option-text").click()
    # 19 | click | css=#mat-option-32 > .mat-option-text | 
    self.driver.find_element(By.CSS_SELECTOR, "#mat-option-32 > .mat-option-text").click()
    # 20 | doubleClick | css=#mat-option-32 > .mat-option-text | 
    element = self.driver.find_element(By.CSS_SELECTOR, "#mat-option-32 > .mat-option-text")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    # 21 | click | css=.cdk-overlay-backdrop | 
    self.driver.find_element(By.CSS_SELECTOR, ".cdk-overlay-backdrop").click()
    # 22 | runScript | window.scrollTo(0,320) | 
    self.driver.execute_script("window.scrollTo(0,320)")
    # 23 | click | id=mat-input-2 | 
    self.driver.find_element(By.ID, "mat-input-2").click()
    # 24 | click | css=.ng-tns-c58-107 > .mat-form-field-infix | 
    self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c58-107 > .mat-form-field-infix").click()
    # 25 | mouseOver | css=.pb-3 > .mat-focus-indicator:nth-child(1) > .mat-button-wrapper | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".pb-3 > .mat-focus-indicator:nth-child(1) > .mat-button-wrapper")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 26 | type | id=mat-input-3 | qweqweqweqwe
    self.driver.find_element(By.ID, "mat-input-3").send_keys("qweqweqweqwe")
    # 27 | click | css=.cdk-focused > .mat-button-wrapper | 
    self.driver.find_element(By.CSS_SELECTOR, ".cdk-focused > .mat-button-wrapper").click()
    # 28 | mouseOut | css=.mat-button-disabled:nth-child(1) > .mat-button-wrapper | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
  
