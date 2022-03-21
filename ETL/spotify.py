import pandas as pd
import json
from datetime import date, datetime, timedelta
import requests


USER_ID = '12148243992'
TOKEN = "BQDcCpMRbHBKXMLxjXgB0zwjoyAoWxZC432-PqqH1IBGgyTG6HfH8E0SXecRCKV-f4QdSBwM-2w8EKJtqt60Yy2R7wgiT2gP61r4ayxWew0n0j53IrasYM7CUHAXjsDtpzceIiTZ8BzDwH-j0amRQg"


if __name__ == '__main__':

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {token}".format(token=TOKEN),
    }

    today = datetime.now()
    yesterday = today - timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000
    
    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp), headers=headers)

    data = r.json()
    

    for songs in data['item']:
        songs['track']
