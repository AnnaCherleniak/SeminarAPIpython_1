from testpage import OperationsHelper
import pytest
import yaml
import time
import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    assert testpage.get_error_text() == '401'


def test_step2(browser, data_user):
    testpage = OperationsHelper(browser)
    testpage.enter_login(data_user['username'])
    testpage.enter_pass(data_user['password'])
    testpage.click_login_button()
    assert data_user['username'] in testpage.get_main_user()


def test_step3(browser, data_post):
    testpage = OperationsHelper(browser)
    testpage.click_menu_user()
    testpage.click_profile()
    testpage.click_btn_create_post()
    testpage.enter_post_title(data_post['title'])
    testpage.enter_post_description(data_post['description'])
    testpage.enter_post_content(data_post['content'])
    time.sleep(testdata['sleep_time'])
    testpage.click_btn_save_post()
    time.sleep(testdata['sleep_time'])
    assert testpage.get_title_post_page() == data_post['title']


def test_step4(browser):
    testpage = OperationsHelper(browser)
    testpage.click_btn_menu_contact()
    testpage.enter_yourname_field(testdata['yourname'])
    testpage.enter_youremail_field(testdata['youremail'])
    testpage.enter_content_field(testdata['content'])
    time.sleep(testdata['sleep_time'])
    testpage.click_btn_cintact_us()
    time.sleep(testdata['sleep_time'])
    alert = testpage.driver.switch_to.alert
    assert testdata['text_alert'] == alert.text


if __name__ == '__main__':
    pytest.main(['-v'])

    fromaddr = 'oval24@mail.ru'
    toaddr = 'oval24@mail.ru'
    mypass = 'TSxgX0NTTdJGaLNCBk7K'
    reportname = 'log.log'

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'Test report'

    with open(reportname, 'rb') as f:
        part = MIMEApplication(f.read(), Name=basename(reportname))
        part['Content-Disposition'] = 'attachment; filename=%s"' % basename(reportname)
        msg.attach(part)
    body = 'Test message'
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(fromaddr, mypass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
