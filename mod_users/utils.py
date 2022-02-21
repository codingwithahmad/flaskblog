import random
from app import redis, mail


def add_to_redis(user, mode):
    token = random.randint(10000, 99999)
    name = f'{user.id}_{mode.lower()}'
    redis.set(name=name, value=token, ex=14400)
    return token


def send_signup_message(user, token):
    sender = '3eraji@gmail.com'
    recipients = [user.email]
    subject = "Flask Blog - Registration Confirm"
    body = f'Hello, <br /> Here is your token: {token}'
    mail.send_message(sender=sender, recipients=recipients, subject=subject, html=body)
