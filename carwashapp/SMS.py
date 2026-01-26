import requests
from django.conf import settings

CLICKATELL_URL = "https://platform.clickatell.com/messages"

def send_sms(number, message):
    headers = {
        "Authorization": settings.CLICKATELL_API_KEY,
        "X-Version": "1",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    payload = {
        "content": message,
        "to": [number],
    }

    response = requests.post(
        CLICKATELL_URL,
        headers=headers,
        json=payload,
        timeout=30
    )

    return response.status_code, response.json()
