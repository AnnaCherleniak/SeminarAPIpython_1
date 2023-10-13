import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']


class Site:
    def __init__(self, address) -> None:
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'chrome':
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get(address)
        time.sleep(testdata['sleep_time'])

    def find_element(self, mode, path):
        if mode == 'css':
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == 'xpath':
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element

    def get_element_property(self, mode, path, property):
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)

    def close(self):
        self.driver.close()

    def input_text(self, mode, x_selector: str, text: str):
        input1 = self.find_element(mode, x_selector)
        input1.send_keys(text)

    def click_button(self, mode, btn_selector):
        btn = self.find_element(mode, btn_selector)
        btn.click()
