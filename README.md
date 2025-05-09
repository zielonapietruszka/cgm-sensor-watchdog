# cgm-sensor-watchdog - Monitor Dostępności Sensorów CGM do pompy 780G MMT-5120

Aplikacja do monitorowania dostępności sensorów CGM Simplera Sync do pompy 780G MMT-5120 w polskich sklepach medycznych. Automatycznie sprawdza dostępność produktu i wysyła powiadomienia na telefon, gdy sensor jest dostępny.

## Szybki start (tylko powiadomienia)

Jeśli chcesz tylko otrzymywać powiadomienia o dostępności sensora, wystarczy że:

1. Pobierzesz aplikację ntfy z oficjalnego sklepu:
   - [Google Play Store](https://play.google.com/store/apps/details?id=io.heckel.ntfy)
   - [App Store](https://apps.apple.com/us/app/ntfy/id1625396347)

2. Po zainstalowaniu aplikacji:
   - Otwórz aplikację ntfy
   - Kliknij "+" aby dodać nową subskrypcję
   - Wpisz nazwę kanału: `sensor-cgm`
   - Kliknij "Subscribe"

Gotowe! Będziesz otrzymywać powiadomienia, gdy sensor stanie się dostępny w którymkolwiek z monitorowanych sklepów.

## Monitorowane sklepy

- Diabetyk24.pl
- Medital.pl
- Infusion.pl
- SOS Diabetyka

## Instalacja lokalna (opcjonalnie)

Jeśli chcesz uruchomić skrypt lokalnie na swoim komputerze to:

1. Sklonuj repozytorium:
```bash
git clone https://github.com/twoje-repozytorium/MediWatch.git
cd MediWatch
```

2. Zainstaluj wymagane biblioteki:
```bash
pip install -r requirements.txt
```

3. Uruchom skrypt:
```bash
python check_product.py
```

Skrypt  sprawdzi dostępność sensora w sklepach i wyśle powiadomienie gdy będzie dostępny.

## Automatyczne uruchamianie

Skrypt jest skonfigurowany do automatycznego uruchamiania się co godzinę poprzez GitHub Actions. Nie musisz nic dodatkowo konfigurować - powiadomienia będą przychodzić automatycznie.


---

*Projekt tworzony z myślą o osobach szukających wyrobów medycznych, które często są  niedostępne w sprzedaży.*
