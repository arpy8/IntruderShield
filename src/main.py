import os
import cv2
import requests
import pyautogui
from datetime import datetime
from twilio.rest import Client

account_sid = os.getenv("TWILIO_SID_2")
auth_token = os.getenv("TWILIO_API_2")
client = Client(account_sid, auth_token)
time_stamp = datetime.now().strftime("%H.%M.%S  %d-%m-%Y")


def get_location():
    try:
        response = requests.get('https://ipinfo.io')
        if response.status_code == 200:
            data = response.json()

            # Extract and print location details
            city = data.get('city', '')
            region = data.get('region', '')
            country = data.get('country', '')
            loc = data.get('loc', '').split(',')
            latitude, longitude = loc[0], loc[1]

            return f"ㅤ\nIMPORTANT! Someone tried to access your laptop.\n\nTime: {time_stamp}\n" \
                   f"Location: {city}, {region}, {country}\nLatitude: {latitude}\nLongitude: {longitude}"

        else:
            return f"ㅤ\nIMPORTANT! Someone tried to access your laptop.\n\nTime: {time_stamp}\n" \
                   f"Failed to retrieve location info\n." \
                   f"No internet connection detected."

    except Exception as e:
        print(f"An error occurred: {e}")


def send_sms():
    client.messages.create(
        from_=os.getenv("TWILIO_PHN_2"),
        to=os.getenv("MY_PHN"),
        body=get_location(),
    )


def click_picture():
    camera = cv2.VideoCapture(0)
    for i in range(1):
        return_value, image = camera.read()
        cv2.imwrite(f'./data/intruder/{time_stamp}.png', image)
    del camera


def lock_screen():
    pyautogui.hotkey("ctrl", "win", "d")
    pyautogui.hotkey("alt", "f4")

    pyautogui.press("enter")
    pyautogui.sleep(1)
    pyautogui.press("enter")
    for _ in range(2):
        pyautogui.press("enter")


try:
    send_sms()
except Exception:
    pass
finally:
    click_picture()
    lock_screen()
