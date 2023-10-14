import yaml
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


class BasePage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.base_url = testdata['address']

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message='element not find')

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        return element.value_of_css_property(property)
