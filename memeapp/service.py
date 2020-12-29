import requests

def get_memes():
    url = 'https://api.imgflip.com/get_memes'
    r = requests.get(url)
    memes = r.json()
    return memes