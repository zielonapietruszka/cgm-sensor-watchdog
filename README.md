# cgm-sensor-watchdog - Monitor Dostępności Sensorów CGM

Aplikacja do monitorowania dostępności sensorów CGM Simplera Sync w polskich sklepach medycznych. Skrypt automatycznie sprawdza dostępność produktu i wysyła powiadomienia na telefon, gdy sensor staje się dostępny.

## Szybki start (tylko powiadomienia)

Jeśli chcesz tylko otrzymywać powiadomienia o dostępności sensora, wystarczy:

1. Pobierz aplikację ntfy z oficjalnego sklepu:
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

Jeśli chcesz uruchomić skrypt lokalnie na swoim komputerze, wykonaj poniższe kroki:

### Wymagania

- Python 3.6 lub nowszy
- Biblioteki Python:
  - requests
  - beautifulsoup4

### Instalacja

1. Sklonuj repozytorium:
```bash
git clone https://github.com/twoje-repozytorium/MediWatch.git
cd MediWatch
```

2. Zainstaluj wymagane biblioteki:
```bash
pip install -r requirements.txt
```

### Uruchomienie

1. Uruchom skrypt:
```bash
python check_product.py
```

2. Skrypt będzie sprawdzał dostępność sensora w sklepach i wysyłał powiadomienia na Twój telefon, gdy produkt stanie się dostępny.

## Automatyczne uruchamianie

Skrypt jest skonfigurowany do automatycznego uruchamiania się co godzinę poprzez GitHub Actions. Nie musisz nic dodatkowo konfigurować - powiadomienia będą przychodzić automatycznie.

## Powiadomienia

Gdy sensor stanie się dostępny w którymkolwiek ze sklepów, otrzymasz powiadomienie na telefon z informacją o dostępności i nazwą sklepu.

## Rozwiązywanie problemów

1. Jeśli nie otrzymujesz powiadomień:
   - Sprawdź czy aplikacja ntfy jest zainstalowana i skonfigurowana
   - Upewnij się, że subskrybujesz kanał `sensor-cgm`
   - Sprawdź ustawienia powiadomień w systemie

2. Jeśli skrypt nie działa (tylko dla instalacji lokalnej):
   - Upewnij się, że masz zainstalowane wszystkie wymagane biblioteki
   - Sprawdź połączenie z internetem
   - Sprawdź logi w GitHub Actions

## Wsparcie

W przypadku problemów lub pytań, utwórz issue w repozytorium projektu.

## Licencja

Ten projekt jest udostępniany na licencji MIT. Szczegóły znajdują się w pliku LICENSE.

---

*Projekt tworzony z myślą o osobach szukających wyrobów medycznych, które często są chwilowo niedostępne w sprzedaży.*
