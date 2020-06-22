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
from posters.ms import search_ms_newgrad_ca


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


POSTER_AMZ = 'Amazon'
POSTER_MS = 'Microsoft'

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Notify me on job posting updates.')
    parser.add_argument('-i', '--interval', type=int, help='Num of minutes to wait before check again')
    main_args = parser.parse_args()

    # CONFIGURE THE KEY WORDS HERE
    targets = {
        POSTER_AMZ: [
            {'key_words': ['Vancouver'], 'found': False, 'url': 'https://www.amazon.jobs/en/teams/jobs-for-grads?sort=recent'},
            {'key_words': ['Taipei'], 'found': False, 'url': 'https://www.amazon.jobs/en/teams/jobs-for-grads?sort=recent'}
        ],
        POSTER_MS: [
            # `key_words` here is not required by the selenium search, only for logging purpose
            {'key_words': ['Canada fulltime'], 'found': False, 'url': 'https://careers.microsoft.com/students/us/en/canada-full-time-results'}
        ]
    }

    search_funcs = {
        POSTER_AMZ: search_amz_newgrad_recent_10,
        POSTER_MS: search_ms_newgrad_ca
    }

    logging.basicConfig(format='%(asctime)s - %(message)s', filename='jobs_notify.log', level=logging.INFO)
    try:
        while True:
            for poster, arg_list in targets.items():
                for args in arg_list:
                    search_signature = '{}: {}'.format(poster, args['key_words'][0])
                    if not args['found']:
                        logging.info('Searching {}'.format(search_signature))

                        if search_funcs[poster](args['url'], args['key_words']):
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
