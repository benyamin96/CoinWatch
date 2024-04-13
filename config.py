URL = 'http://data.fixer.io/api/latest?access_key='
API_KEY = 'FIXER_API_KEY'


# Kavehnegar
KAVEHNEGAR_API_KEY = 'KAVEHNEGAR_API_KEY'


# Email configs
TO = 'example@domain.com'
FROM = 'notifications@coinwatch.com'

EMAIL_PROVIDER = 'example@domain.com'

SMTP_SERVER_EMAIL = 'example@domain.com'
SMTP_SERVER_PASSWORD = ''
SMTP_PORT = None


rules = {
    'archive': True,
    'send_mail': {
        'enable': False
    },
    'sms': {
        'enable': False,
        'receiver': 'YOUR PHONE NUMBER'
    },
    'currencies': {
        'USD': {'min': 1.085, 'max': 1.086},
        'IRR': {'min': 43000, 'max': 46000},
    }
}
