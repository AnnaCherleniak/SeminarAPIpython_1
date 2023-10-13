import yaml
from module import Site
import pytest
import random
import string
import requests

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def site():
    site = Site(testdata["address"])
    yield site
    site.close()


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


@pytest.fixture()
def get_token():
    respons = requests.post(url=testdata['address'],
                            data={'username': testdata['username'],
                            'password': testdata['password']})
    return respons.json()['token']


@pytest.fixture()
def login(site, data_user):
    site.input_text('xpath', '//*[@id="login"]/div[1]/label/input',
                    data_user['username'])
    site.input_text('xpath', '//*[@id="login"]/div[2]/label/input',
                    data_user['password'])
    site.click_button('css', 'button')
