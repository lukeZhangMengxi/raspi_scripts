import argparse
import logging
import smtplib
import time
import os

from email.message import EmailMessage
from pyvirtualdisplay import Display
from selenium import webdriver
from sys import platform

from posters.amz import search_amz_newgrad_recent_10


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
    except:
        logging.exception('Failed sending email')
    finally:
        server.quit()
    

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Notify me on job posting updates.')
    parser.add_argument('-i', '--interval', type=int, help='Num of minutes to wait before check again')
    main_args = parser.parse_args()

    # CONFIGURE THE KEY WORDS HERE
    targets = {
        search_amz_newgrad_recent_10: [
            {'key_words': ['Vancouver'], 'found': False, 'url': 'https://www.amazon.jobs/en/teams/jobs-for-grads?sort=recent'},
            {'key_words': ['Taipei'], 'found': False, 'url': 'https://www.amazon.jobs/en/teams/jobs-for-grads?sort=recent'}
        ]
    }

    logging.basicConfig(format='%(asctime)s - %(message)s', filename='jobs_notify.log', level=logging.INFO)
    try:
        while True:
            for search_func, arg_list in targets.items():
                for args in arg_list:
                    search_signature = args['key_words'][0]
                    if not args['found']:
                        logging.info('Searching {}'.format(search_signature))

                        if search_func(args['url'], args['key_words']):
                            logging.info('FOUND NEW JOB POSTING - {}'.format(search_signature))

                            send_email(
                                to_address='zmx94824@gmail.com',
                                subject='NEW JOB POSTING - {}'.format(search_signature),
                                content='check it out at {}'.format(args['url'])
                            )
                            args['found'] = True
                        else:
                            logging.info('Target not found - {}'.format(search_signature))
                    else:
                        logging.info('Target already found - {}'.format(search_signature))

            time.sleep(main_args.interval*60)
    except:
        logging.exception('Job notifier exited unexpectedly')
        send_email(
            to_address='zmx94824@gmail.com',
            subject='Check your worker (Raspberry Pi)',
            content='Job notifier exited unexpectedly'
        )
