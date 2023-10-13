import yaml
import pytest
import time

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def test_step1(site):
    site.input_text('xpath', '//*[@id="login"]/div[1]/label/input', 'test')
    site.input_text('xpath', '//*[@id="login"]/div[2]/label/input', 'test')
    site.click_button('css', 'button')
    x_selector = '//*[@id="app"]/main/div/div/div[2]/h2'
    err_label = site.find_element('xpath', x_selector)
    assert err_label.text == '401'


def test_step2(site, data_user, login):
    login
    x_selector3 = '//*[@id="app"]/main/nav/ul/li[3]/a'
    result = site.find_element('xpath', x_selector3)
    assert data_user['username'] in result.text


def test_step3(site, data_user, data_post, login):
    login
    site.click_button('xpath', '//*[@id="app"]/main/nav/ul/li[3]')
    # profile
    site.click_button('xpath', '//*[@id="app"]/main/nav/ul/li[3]/div/ul/li[1]')
    # button creat post
    site.click_button('xpath', '//*[@id="create-btn"]')
    # titel
    site.input_text('xpath',
                    '//*[@id="update-post-item"]/div/div/div[1]/div/label/input',
                    data_post['title'])
    # description
    site.input_text('xpath',
                    '//*[@id="update-post-item"]/div/div/div[2]/div/label/span/textarea',
                    data_post['description'])
    # content
    site.input_text('xpath',
                    '//*[@id="update-post-item"]/div/div/div[3]/div/label/span/textarea',
                    data_post['content'])
    # click save
    time.sleep(testdata['sleep_time'])
    site.click_button('xpath',
                      '//*[@id="update-post-item"]/div/div/div[7]/div/button/span')
    time.sleep(testdata['sleep_time'])
    x_selector = '//*[@id="app"]/main/div/div[1]/h1'
    result = site.find_element('xpath', x_selector)
    assert data_post['title'] == result.text


if __name__ == '__main__':
    pytest.main(['-v'])
