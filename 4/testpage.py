from BaseApp import BasePage
from selenium.webdriver.common.by import By
import yaml
import logging

logging.basicConfig(filename='log.log', filemode='w', encoding='utf-8',
                    level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class TestSearchLocators:
    ids = dict()
    with open('./locators.yaml') as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):

    def enter_text_info_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send {word} to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception while operation with {locator}')
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        buttor = self.find_element(locator)
        if not buttor:
            return False
        try:
            buttor.click()
        except:
            logging.exception('Exception with click')
            return False
        logging.debug(f'Clicked {element_name} button')
        return True

    def get_text_for_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get test frome {element_name}')
            return None
        logging.debug(f'We find text {text} in field {element_name}')
        return text

    # enter text
    def enter_login(self, word):
        self.enter_text_info_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'],
                                   word, description='login form')
        logging.info('enter in the login field')

    def enter_pass(self, word):
        self.enter_text_info_field(TestSearchLocators.ids['LOCATOR_PASS_FIELD'],
                                   word, description='login form')
        logging.info('enter in the password field')

    def enter_post_title(self, text):
        self.enter_text_info_field(TestSearchLocators.ids['LOCATOR_POST_TITLE'],
                                   text, description='Created post')
        logging.info('enter in the title pots field')

    def enter_post_description(self, text):
        self.enter_text_info_field(TestSearchLocators.ids['LOCATOR_POST_DESCRIPTION'],
                                   text, description='Created post')
        logging.info('enter in the description post field')

    def enter_post_content(self, text):
        self.enter_text_info_field(TestSearchLocators.ids['LOCATOR_POST_CONTENT'],
                                   text, description='Created post')
        logging.info('enter in the content post field')

    def enter_yourname_field(self, text):
        self.enter_text_info_field(TestSearchLocators.ids['LOCATOR_YNAME_FIELD'],
                                   text, description='Contact us')
        logging.info('enter in the yuorname contact field')

    def enter_youremail_field(self, text):
        self.enter_text_info_field(TestSearchLocators.ids['LOCATOR_YEMAIL_FIELD'],
                                   text, description='Contact us')
        logging.info('enter in the youremail contact field')

    def enter_content_field(self, text):
        self.enter_text_info_field(TestSearchLocators.ids['LOCATOR_CONTENT_FIELD'],
                                   text, description='Contact us')
        logging.info('enter in the content contact field')

    # click
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'],
                          description='Login')

    def click_menu_user(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_MENU_USER'],
                          description='Open menu User')

    def click_profile(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_PROFILE'],
                          description='Open Profile')

    def click_btn_create_post(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_BTN_CREATE_POST'],
                          description='Created post')

    def click_btn_save_post(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_BTN_SAVE_POST'],
                          description='Save post')

    def click_btn_menu_contact(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_BTN_MENU_CONTACT'],
                          description='Menu Contact')

    def click_btn_cintact_us(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_BTN_CONTACT_US'],
                          description='Contact us')

    # get
    def get_error_text(self):
        return self.get_text_for_element(TestSearchLocators.ids['LOCATOR_ERROR_FIELD'])

    def get_main_user(self):
        return self.get_text_for_element(TestSearchLocators.ids['LOCATOR_MAIN_USER'])

    def get_title_post_page(self):
        return self.get_text_for_element(TestSearchLocators.ids['LOCATOR_TITLE_POST_PAGE'])
