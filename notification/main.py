import argparse
import logging
import smtplib
import time
import os

from email.message import EmailMessage


def send_email(to_address, subject, content):
    password = os.environ.get('PW_DEV_GAMIL') or input("Type your password and press enter:")
    from_addr = 'mengxidev@outlook.com'

    server = smtplib.SMTP('smtp.office365.com:587')  
    try:
        server.starttls()
        server.login(from_addr, password)

        msg = EmailMessage()
        msg.set_content(content)
        msg['Subject'] = subject
        msg['From'] = from_addr
        msg['To'] = to_address
        server.send_message(msg)
    except Exception as e:
        logging.exception('Failed sending email \n' + e)
    finally:
        server.quit()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Notification service')
    parser.add_argument('-i', '--interval', type=int, help='Num of minutes to wait before check again', default=7*24*60)
    main_args = parser.parse_args()

    logging.basicConfig(format='%(asctime)s - %(message)s', filename='notification.log', level=logging.INFO)
    try:
        while True:
            send_email(
                to_address='zmx94824@gmail.com',
                subject='RasPi Notification',
                content='I am alive! Tell me to do something~'
            )

            logging.info('Sent email')
            time.sleep(main_args.interval*60)
    except:
        logging.exception('Notification service exited unexpectedly')
        send_email(
            to_address='zmx94824@gmail.com',
            subject='Check your worker (Raspberry Pi)',
            content='Notification service exited unexpectedly'
        )
