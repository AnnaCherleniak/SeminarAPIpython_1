from task2 import get, post
import pytest


def test_step1(get_token):
    res = get(get_token)
    lst_res = res['data']
    lst_id = [el['id'] for el in lst_res]
    assert 82432 in lst_id


def test_step2(get_token, data_post):
    post(get_token, data_post['titel'], data_post['description'],
         data_post['content'])
    res = get(get_token)
    lst_res = res['data']
    lst_id = [el['description'] for el in lst_res]
    assert data_post['description'] in lst_id


if __name__ == '__main__':
    pytest.main(['-v'])
