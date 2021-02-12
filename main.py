import requests
import json
import smtplib
from email.message import EmailMessage
import getpass
import time

EMAIL_ADDRESS = input('Please provide your email: ')
EMAIL_PASSWORD = getpass.getpass('Enter your password (If you have 2fa enabled provide your token): ')

state = input('What state would you like to track? (Example: CA): ')

cities = []

while True:
    city = input('Enter in cities you would like to track. (When you are done listing cities type: exit): ')
    if city.lower() == 'exit':
        break
    else:
        cities.append(city.upper())

interval = int(input('How often would you like to send requests? (in seconds!): '))

print('Alright! It is now running press <ctrl> + <c> to exit.')

while True:
    res = requests.get(f'https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.{state}.json?vaccineinfo')

    data = json.loads(res.text)

    data = data['responsePayloadData']['data']['CA']

    for obj in data:
        if obj['city'] in cities and obj['status'] == 'Available':
            msg = EmailMessage()
            msg['Subject'] = 'Covid vaccination alert: '
            msg.set_content(f'{obj["city"]} is currently is open for vaccinations!')
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = EMAIL_ADDRESS
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(password=EMAIL_PASSWORD, user=EMAIL_ADDRESS)
                smtp.send_message(msg)
            time.sleep(1)  # cooldown if its spamming the email server
    time.sleep(interval)