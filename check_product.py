import requests
from bs4 import BeautifulSoup

URL = 'https://diabetyk24.pl/sensor-cgm-simpleratm-sync-1-szt-do-pompy-minimed-780g-mmt-5120d2'
HEADERS = {'User-Agent': 'Mozilla/5.0'}
NTFY_TOPIC = 'sensor-cgm'
NTFY_URL = f'https://ntfy.sh/{NTFY_TOPIC}'

def is_available():
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    return "Brak produktu na stanie" not in soup.text

def send_notification():
    requests.post(NTFY_URL, data='Produkt Sensor CGM jest dostępny na diabetyk24!')

if is_available():
    send_notification()
