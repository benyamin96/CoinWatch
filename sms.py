from kavenegar import *
from config import KAVEHNEGAR_API_KEY, rules


def send_sms(text):
    try:
        api = KavenegarAPI(KAVEHNEGAR_API_KEY)
        params = {
            'sender': '10008663',
            'receptor': rules['sms']['receiver'],
            'message': text
        }
        response = api.sms_send(params)
        print(str(response))
    except APIException as e:
        print(str(e))
    except HTTPException as e:
        print(str(e))
