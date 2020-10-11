import json
import requests
from flask_babel import _
from app import app

def translate(text, source_language, dest_language):
    page = 'https://api.mymemory.translated.net/get?q={}&langpair={}|{}'.format(text, source_language,dest_language)
    r = requests.get(page)
    if r.status_code != 200:
        return _('Error: The translation service failed!')

    return json.loads(r.content.decode('utf-8-sig'))['responseData']['translatedText']

