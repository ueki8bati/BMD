from .models import Dictionary
import requests

class ReadMessage():
    url = "https://slack.com/api/conversations.history" 
    token = "XXX"

    header={"Authorization": "Bearer {}".format(token)}

    payload  = {"channel" : "bookmark"}
    res = requests.get(url, headers=header, params=payload)
    print(res.json())