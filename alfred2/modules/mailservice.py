
import requests
import config

def send(to, subject, body):
    r = requests.post(
        "https://api.mailgun.net/v3/mg.ewright3.com/messages",
        auth=("api", config.api_key),
        data={"from": "Jarvis <Jarvis@mg.ewright3.com>",
              "to": [to],
              "subject": subject,
              "text": body})

    print(r.json())


def send_troll(sender):
        r = requests.post(
        "https://api.mailgun.net/v3/mg.ewright3.com/messages",
        auth=("api", config.api_key),
        data={"from": "Jarvis <Jarvis@mg.ewright3.com>",
              "to": [sender],
              "subject": "Response",
              "text": config.trollresponse})
        print(r.json())