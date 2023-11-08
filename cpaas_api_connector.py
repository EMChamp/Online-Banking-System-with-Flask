import requests, variables
sms_subaccount = variables.sms_subaccount
voice_subaccount = variables.voice_subaccount
sender_id = variables.sms_sender_id
voice_caller = variables.voice_caller_number

headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer " + variables.BearerToken
}

def sendSMS(phone_number):
    url = f"https://sms.8x8.com/api/v1/subaccounts/{sms_subaccount}/messages"

    payload = {
        "source": sender_id,
        "destination": phone_number,
        "text": "Your order is on its way!",
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.text)


def makeCall(phone_number):
    url = f"https://voice.wavecell.com/api/v1/subaccounts/{voice_subaccount}/callflows"

    payload = {
        "callflow": [
            {
            "action": "makeCall",
            "params": {
                "source": voice_caller,
                "destination": phone_number
                }
            },
            {
            "action": "say",
            "params": {
                "text": "Hello, we have detected a large withdrawl from your account, please contact your eight by eight bank representative at +65 9999 9999 to Confirm.",
                "voiceProfile": "en-IE-EmilyNeural",
                "repetition": 1,
                "speed": 1
                }
            },
            {
            "action": "hangup"
            }
        ]
    }

    response = requests.post(url, json=payload, headers=headers)
    response_data = response.json()
    return response_data

def sendOTP(phone_number):
    url = f"https://sms.8x8.com/api/v2/subaccounts/{sms_subaccount}/sessions"

    payload = {
        "destination": phone_number,
        "sms": {
            "source": sender_id,
            "encoding": "AUTO"
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    response_data = response.json()
    return response_data["sessionId"]


def verifyOTP(sessionID, otpCode):
    url = f"https://verify.8x8.com/api/v2/subaccounts/{sms_subaccount}/sessions/" + sessionID + "?code=" + otpCode

    response = requests.get(url, headers=headers)
    response_data = response.json()
    print(response_data)
    return response_data