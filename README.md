# 🏥 cgm-sensor-watchdog - Monitor Dostępności Sensorów CGM do pompy insulinowej 780G MMT-5120

Aplikacja do monitorowania dostępności sensorów CGM Simplera Sync do pompy insulinowej 780G MMT-5120 w polskich sklepach medycznych. Automatycznie sprawdza dostępność produktu i wysyła powiadomienia na telefon, gdy sensor jest dostępny.

## ⏰ Automatyczne uruchamianie

Skrypt jest skonfigurowany do automatycznego uruchamiania poprzez GitHub Actions co 15 minut między 7:00 a 22:00 UTC (czyli 9:00–00:00 czasu lokalnego w Polsce).

## 🔒 Uwaga 

Obecnie program używa otwartego kanału ntfy (`sensor-cgm`), co oznacza że każdy może subskrybować ten kanał i otrzymywać powiadomienia.


## 📱 Szybki start (tylko powiadomienia)

Jeśli chcesz tylko otrzymywać powiadomienia o dostępności sensora, wystarczy że:

1. Pobierzesz aplikację ntfy z oficjalnego sklepu:
   - [Google Play Store](https://play.google.com/store/apps/details?id=io.heckel.ntfy)
   - [App Store](https://apps.apple.com/us/app/ntfy/id1625396347)

2. Po zainstalowaniu aplikacji:
   - Otwórz aplikację ntfy
   - Kliknij "+" aby dodać nową subskrypcję
   - Wpisz nazwę kanału: `sensor-cgm`
   - Kliknij "Subskrybuj'

✅ Gotowe! Będziesz otrzymywać powiadomienia, gdy sensor stanie się dostępny w którymkolwiek z monitorowanych sklepów.

## 🏪 Monitorowane sklepy

- Diabetyk24.pl
- Medital.pl
- Infusion.pl
- Sosdiabetyka.pl

## 📋 Do zrobienia

   1. Dodanie prywatnego tokena do kanału ntfy
   2. Optymalizacja częstotliwości sprawdzania sklepów
   3. Implementacja systemu przewidywania dostaw


## 💻 Instalacja lokalna (opcjonalnie)

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

Skrypt sprawdzi dostępność sensora w sklepach, wyświetli status w terminalu i wyśle powiadomienie gdy będzie dostępny.
