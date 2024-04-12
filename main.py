import requests
import json
from datetime import datetime
from config import URL, API_KEY, rules
from mail import send_smtp_email
from sms import send_sms

BASE_PATH = URL + API_KEY


def get_rates():
    try:
        response = requests.get(BASE_PATH)
        if response.status_code == 200:
            return json.loads(response.text)
        return None
    except Exception as e:
        print(e)


def archive(filename, rates):
    currency = {}
    with open(f'archive/{filename}.json', 'w') as file:
        for rate in rates.keys():
            if rate in rules['currencies']:
                if rate not in currency.keys():
                    currency[rate] = rates[rate]
        file.write(json.dumps(currency))


def check_price(rates):
    msg = ''
    for price in rules['currencies'].keys():
        if rates[price] <= rules['currencies'][price]['min']:
            msg += f'The price of {price} reached its lowest level'
        if rates[price] >= rules['currencies'][price]['max']:
            msg += f'The price of {price} reached its highest level'
    return msg


if __name__ == '__main__':

    data = get_rates()
    print(data)
    if data:
        filename = datetime.now()
        try:
            rates = data['rates']
        except Exception as e:
            print(e)
            exit()
        if rules['archive']:
            archive(filename, rates)
        if rules['currencies']:
            message = check_price(rates)
            if rules['send_mail']['enable']:
                if message:
                    send_smtp_email(message)
            if rules['sms']['enable']:
                if message:
                    send_sms(message)
