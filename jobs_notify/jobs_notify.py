import smtplib
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
    

# send_email('zmx94824@gmail.com', 'this is a title', 'this is a content')
# 
# # Expected to be False currently
# print(search_amz_newgrad_recent_10(['Vancouver']))
# # Expected to be True currently
# print(search_amz_newgrad_recent_10(['Santiago']))

