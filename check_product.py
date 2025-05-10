import requests
from bs4 import BeautifulSoup

# Strony do monitorowania
STORES = {
    'diabetyk24': {
        'url': "https://diabetyk24.pl/sensor-cgm-simpleratm-sync-1-szt-do-pompy-minimed-780g-mmt-5120d2/availability_notification",
        'unavailable_text': "brak produktu na stanie",
        'name': "Diabetyk24",
        'check_type': 'text'
    },
    'medital': {
        'url': "https://medital.pl/pl/p/Sensor-CGM-Simplera-Sync-Medtronic-do-pompy-780G-MMT-5120/634",
        'unavailable_text': "tymczasowo niedostępny",
        'name': "Medital",
        'check_type': 'class',
        'class_name': 'second',
        'element_type': 'span'
    },
    'infusion': {
        'url': "https://infusion.pl/sensory-i-transmitery-/753-1414-sensor-simplera-sync-do-pompy-780g.html#/223-simplera-r0301_ponizej_26_lat",
        'unavailable_text': "Oczekiwanie na dostawę",
        'name': "Infusion",
        'check_type': 'id',
        'element_id': 'product-availability',
        'element_type': 'span'
    },
    'sosdiabetyka': {
        'url': "https://sosdiabetyka.pl/product?productId=670ce787c8be4494e25ebdcc",
        'unavailable_text': "Produkt niedostępny",
        'name': "SOS Diabetyka",
        'check_type': 'button',
        'element_type': 'button'
    }
}

NTFY_URL = "https://ntfy.sh/sensor-cgm"

def check_availability_by_element(soup, store_config):
    # Sprawdzanie dostępność produktu wyszukując element po klasie, id lub tagu 
    if store_config['check_type'] == 'button':
        # Sprawdzanie Buttona
        if 'button_class' in store_config:
            # Sprawdzanie dla medital.pl button z konkretną 
            element = soup.find('button', class_=store_config['button_class'])
        else:
            # Standardowe sprawdzanie dla przycisku
            element = soup.find('button', string=lambda text: text and store_config['unavailable_text'] in text)
    elif 'class_name' in store_config:
        element = soup.find(store_config['element_type'], class_=store_config['class_name'])
    elif 'element_id' in store_config:
        element = soup.find(store_config['element_type'], id=store_config['element_id'])
    else:
        return False

    if not element:
        print(f"⚠️ Nie znaleziono elementu dostępności w {store_config['name']}")
        return False
    
    # Sprawdzanie tekstu buttona
    if store_config['check_type'] == 'button':
        if 'button_class' in store_config:
            return False
        return False 
    
    availability_text = element.get_text().lower().strip()
    return store_config['unavailable_text'].lower() not in availability_text

def check_product(store_config):
    response = requests.get(store_config['url'])
    soup = BeautifulSoup(response.text, "html.parser")
    
    is_available = False
    if store_config['check_type'] in ['class', 'id']:
        is_available = check_availability_by_element(soup, store_config)
    else:
        # Sprawdzanie dla diabetyk24 w tekscie
        text = soup.get_text().lower()
        is_available = store_config['unavailable_text'].lower() not in text

    if is_available:
        print(f"✅ Produkt dostępny w {store_config['name']} – wysyłanie powiadomienia.")
        send_notification(store_config['name'])
        return True
    else:
        print(f"❌ Produkt niedostępny w {store_config['name']}.")
        return False
# Wysyłanie powiadomienia   
def send_notification(store_name):
    message = f'🎉 Sensor CGM jest DOSTĘPNY w sklepie {store_name}!'
    headers = {'Content-Type': 'text/plain; charset=utf-8'}
    requests.post(NTFY_URL, data=message.encode('utf-8'), headers=headers)

def check_all_stores():
    for store_id, store_config in STORES.items():
        check_product(store_config)

if __name__ == "__main__":
    check_all_stores()
