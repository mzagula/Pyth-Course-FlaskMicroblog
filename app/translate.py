import json
import requests
from flask_babel import _
from app import app

def translate(text, source_language, dest_language):
    r = requests.get('https://api.mymemory.translated.net/get?q={}&langpair={}|{}').format(text,
    if r.status_code != 200:
        return json.loads(r.content.decore('utf-8-sig'))
                                                                                          dest_language)

