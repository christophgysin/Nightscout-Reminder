import os
import requests

print("Plik testowy")

#os.environ['haslo'] = 'nieudostepniacwebhooka'

#zmienna = os.environ.get('haslo')

#print(zmienna)
#test


import json


credentials = os.environ.get('haslo')
message = f"Test SLACKA ==> tajne {credentials}"


def post_to_slack(message, credentials):
    data = {'text': message}
    url = credentials
    requests.post(url, json=data, verify=False)

print("Message sent to SLACK")
print("tresc do wysania", message)

post_to_slack(message, credentials)