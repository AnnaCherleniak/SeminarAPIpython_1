from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, '''//*[@id="login"]/div[1]/label/input''')
    LOCATOR_PASS_FIELD = (By.XPATH, '''//*[@id="login"]/div[2]/label/input''')
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, '''button''')
    LOCATOR_ERROR_FIELD = (By.XPATH, '''//*[@id="app"]/main/div/div/div[2]/h2''')
    LOCATOR_MAIN_USER = (By.XPATH, '''//*[@id="app"]/main/nav/ul/li[3]/a''')
    LOCATOR_MENU_USER = (By.XPATH, '''//*[@id="app"]/main/nav/ul/li[3]''')
    LOCATOR_PROFILE = (By.XPATH, '''//*[@id="app"]/main/nav/ul/li[3]/div/ul/li[1]''')
    LOCATOR_BTN_CREATE_POST = (By.XPATH, '''//*[@id="create-btn"]''')
    LOCATOR_POST_TITLE = (By.XPATH, '''//*[@id="update-post-item"]/div/div/div[1]/div/label/input''')
    LOCATOR_POST_DESCRIPTION = (By.XPATH, '''//*[@id="update-post-item"]/div/div/div[2]/div/label/span/textarea''')
    LOCATOR_POST_CONTENT = (By.XPATH, '''//*[@id="update-post-item"]/div/div/div[3]/div/label/span/textarea''')
    LOCATOR_BTN_SAVE_POST = (By.XPATH, '''//*[@id="update-post-item"]/div/div/div[7]/div/button/span''')
    LOCATOR_TITLE_POST_PAGE = (By.XPATH, '''//*[@id="app"]/main/div/div[1]/h1''')
    LOCATOR_BTN_MENU_CONTACT = (By.XPATH, '''//*[@id="app"]/main/nav/ul/li[2]/a''')
    LOCATOR_YNAME_FIELD = (By.XPATH, '''//*[@id="contact"]/div[1]/label/input''')
    LOCATOR_YEMAIL_FIELD = (By.XPATH, '''//*[@id="contact"]/div[2]/label/input''')
    LOCATOR_CONTENT_FIELD = (By.XPATH, '''//*[@id="contact"]/div[3]/label/span/textarea''')
    LOCATOR_BTN_CONTACT_US = (By.XPATH, '''//*[@id="contact"]/div[4]/button/span''')


class OperationsHelper(BasePage):
    def enter_login(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD,
                                        time=3)
        return error_field.text

    def get_main_user(self):
        main_user = self.find_element(TestSearchLocators.LOCATOR_MAIN_USER,
                                      time=3)
        return main_user.text

    def click_menu_user(self):
        self.find_element(TestSearchLocators.LOCATOR_MENU_USER).click()

    def click_profile(self):
        self.find_element(TestSearchLocators.LOCATOR_PROFILE).click()

    def click_btn_create_post(self):
        self.find_element(TestSearchLocators.LOCATOR_BTN_CREATE_POST).click()

    def enter_post_title(self, text):
        title_field = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE)
        title_field.clear()
        title_field.send_keys(text)

    def enter_post_description(self, text):
        descr_field = self.find_element(TestSearchLocators.LOCATOR_POST_DESCRIPTION)
        descr_field.clear()
        descr_field.send_keys(text)

    def enter_post_content(self, text):
        content_field = self.find_element(TestSearchLocators.LOCATOR_POST_CONTENT)
        content_field.clear()
        content_field.send_keys(text)

    def click_btn_save_post(self):
        self.find_element(TestSearchLocators.LOCATOR_BTN_SAVE_POST).click()

    def get_title_post_page(self):
        title_post = self.find_element(TestSearchLocators.LOCATOR_TITLE_POST_PAGE)
        return title_post.text

    def click_btn_menu_contact(self):
        self.find_element(TestSearchLocators.LOCATOR_BTN_MENU_CONTACT).click()

    def enter_yourname_field(self, text):
        yourname_field = self.find_element(TestSearchLocators.LOCATOR_YNAME_FIELD)
        yourname_field.clear()
        yourname_field.send_keys(text)

    def enter_youremail_field(self, text):
        youremail_field = self.find_element(TestSearchLocators.LOCATOR_YEMAIL_FIELD)
        youremail_field.clear()
        youremail_field.send_keys(text)

    def enter_content_field(self, text):
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FIELD)
        content_field.clear()
        content_field.send_keys(text)

    def click_btn_cintact_us(self):
        self.find_element(TestSearchLocators.LOCATOR_BTN_CONTACT_US).click()
