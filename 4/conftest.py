import yaml
from selenium import webdriver
import pytest
import random
import string


with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']


@pytest.fixture(scope='session')
def browser():
    if browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def data_user():
    dict_user = {}
    dict_user['username'] = testdata['username']
    dict_user['password'] = testdata['password']
    return dict_user


@pytest.fixture()
def data_post():
    dict_post = {}
    dict_post['title'] = ''.join(random.choices(string.ascii_lowercase, k=5))
    dict_post['description'] = ''.join(random.choices(string.ascii_lowercase,
                                                      k=10))
    dict_post['content'] = ''.join(random.choices(string.ascii_lowercase,
                                                  k=15))
    return dict_post
