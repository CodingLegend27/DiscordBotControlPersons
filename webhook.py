# webhook.py
# Author: Christoph Waffler

# Python Skript to send a specific string to the discord channel
# the bot reacts on the specific text

import requests

# webhook url
url = "https://discord.com/api/webhooks/816450174603886664/k3jnSrUsai543y7T_PLohqqVcl5qDQu5Oblb3clwVBgrcB31lYE8MYpaiUEVunpx4wc4"

# for more params: https://discordapp.com/developers/docs/resources/webhook#execute-webhook
data = {
    "username": "Wildes Python Skript",    
}



def call_disconnect():
    data["content"] = "!kicken daniel"

def call_mute():
    data["content"] = "!mute chrissi"

def call_unmute():
    data["content"] = "!unmute daniel"
    
def call_silence(): 
    data["content"] = "!silence chrissi"


# # for more params: https://discordapp.com/developers/docs/resources/channel#embed-object
# data["embed"] = [
#     {
#         "description": "text in embed",
#         "title": "embed title"
#     }
# ]

def send_request():
    result = requests.post(url, json=data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        
    else:
        print(f"Successful, code {result.status_code}")
        
        
if __name__ == "__main__":
    call_silence()
    send_request()