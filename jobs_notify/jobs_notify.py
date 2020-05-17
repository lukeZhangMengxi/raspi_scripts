import logging
import smtplib
import time
import os

from email.message import EmailMessage
from pyvirtualdisplay import Display
from selenium import webdriver
from sys import platform


def search_amz_newgrad_recent_10(key_words):
    # Only do virtual disply on linux system (supported by xvfb)
    if platform == "linux" or platform == "linux2":
        display = Display(visible=0, size=(800, 800))
        display.start()

    driver = webdriver.Chrome()
    url = "https://www.amazon.jobs/en/teams/jobs-for-grads?sort=recent"
    content = ''
    try:
        driver.get(url)
        content = driver.find_elements_by_xpath(
            '//div[@class="search-page"][1]')[0].text
    finally:
        driver.close()

    for key_word in key_words:
        if key_word.lower() in content.lower():
            return True
    return False


def send_email(to_address, subject, content):
    password = os.environ.get('PW_DEV_GAMIL')   # or input("Type your password and press enter:")
    from_addr = 'mengxidev@gmail.com'

    server = smtplib.SMTP('smtp.gmail.com:587')  
    try:
        server.starttls()  
        server.login(from_addr, password)

        msg = EmailMessage()
        msg.set_content(content)
        msg['Subject'] = subject
        msg['From'] = from_addr
        msg['To'] = to_address
        server.send_message(msg)
    finally:
        server.quit()
    

if __name__ == "__main__":

    targets = [
        # CONFIGURE THE KEY WORDS HERE
        {'key_words': ['Vancouver'], 'found': False},
        {'key_words': ['Santiago'], 'found': False}
    ]

    logging.basicConfig(format='%(asctime)s - %(message)s', filename='jobs_notify.log', level=logging.INFO)
    try:
        while True:
            for t in targets:
                search_signature = t['key_words'][0]
                if not t['found']:
                    logging.info('Searching {}'.format(search_signature))

                    if search_amz_newgrad_recent_10(t['key_words']):
                        logging.info('FOUND NEW JOB POSTING - {}'.format(search_signature))

                        send_email(
                            to_address='zmx94824@gmail.com',
                            subject='NEW JOB POSTING - {}'.format(search_signature),
                            content='check it out at https://www.amazon.jobs/en/teams/jobs-for-grads?sort=recent'
                        )
                        t['found'] = True
                    else:
                        logging.info('Target not found - {}'.format(search_signature))
                else:
                    logging.info('Target already found - {}'.format(search_signature))

            time.sleep(30*60)
    except:
        logging.exception('Job notifier exited unexpectedly')
        send_email(
            to_address='zmx94824@gmail.com',
            subject='Check your worker (Raspberry Pi)',
            content='Job notifier exited unexpectedly'
        )
