import requests, variables
destination = variables.destination
subaccount = variables.subaccount
sender_id = variables.sender_id

headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer " + variables.BearerToken
}

def sendSMS(phone_number):
    url = f"https://sms.8x8.com/api/v1/subaccounts/{subaccount}/messages"

    payload = {
        "source": sender_id,
        "destination": phone_number,
        "text": "Your order is on its way!",
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.text)



def sendOTP(phone_number):
    url = f"https://sms.8x8.com/api/v2/subaccounts/{subaccount}/sessions"

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
    url = f"https://verify.8x8.com/api/v2/subaccounts/{subaccount}/sessions/" + sessionID + "?code=" + otpCode

    response = requests.get(url, headers=headers)
    response_data = response.json()
    print(response_data)
    return response_data