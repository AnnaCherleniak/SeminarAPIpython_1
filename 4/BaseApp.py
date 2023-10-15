import yaml
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)

logging.basicConfig(filename='log.log', filemode='w', encoding='utf-8', level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class BasePage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.base_url = testdata['address']

    def find_element(self, locator, time=5):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Can`t find element by locator {locator}')
        except:
            logging.exception('Find element exception')
            element = None
        return element

    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception('Exception while open site')
            start_browsing = None
        return start_browsing

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.exception(f'Property {property} not found in element with locator {locator}')
            return None

    def get_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except:
            logging.exception('Exception with alert')
            return None
