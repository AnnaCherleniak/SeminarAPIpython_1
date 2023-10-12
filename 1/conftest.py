import pytest
import requests
import yaml
import random
import string

with open('config.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def get_token():
    respons = requests.post(url=data['url'],
                            data={'username': data['username'],
                            'password': data['password']})
    return respons.json()['token']


@pytest.fixture()
def data_post():
    dict_post = {}
    dict_post['titel'] = ''.join(random.choices(string.ascii_lowercase, k=5))
    dict_post['description'] = ''.join(random.choices(string.ascii_lowercase,
                                                      k=10))
    dict_post['content'] = ''.join(random.choices(string.ascii_lowercase,
                                                  k=15))
    return dict_post
