# MediWatchdog

**MediWatchdog** to prosty bot monitorowania trudno dostępnych produktów medycznych w sklepach internetowych. Wykorzystuje GitHub Actions do cyklicznego sprawdzania stron oraz wysyła powiadomienia push (np. przez ntfy.sh) gdy produkt pojawi się na stanie.

## 🔧 Jak to działa?

1. Skrypt w Pythonie sprawdza stronę internetową z produktem.
2. Jeśli wykryje zmianę (produkt dostępny), wysyła powiadomienie.
3. GitHub Actions automatycznie uruchamia skrypt co 15 minut (w określonych godzinach).

## 📦 Przykład monitorowanego produktu

- Sensor CGM Simplera™ Sync 1 szt. do pompy MiniMed 780G  
  https://diabetyk24.pl/sensor-cgm-simpleratm-sync-1-szt-do-pompy-minimed-780g-mmt-5120d2

## 🔔 Powiadomienia

Projekt wykorzystuje [ntfy.sh](https://ntfy.sh) — darmowy system do otrzymywania powiadomień push.  
Zainstaluj aplikację mobilną **ntfy** i zasubskrybuj swój kanał (np. `sensor-cgm`).

## 🛠️ Jak dodać kolejną stronę?

1. Skopiuj istniejący skrypt `check_product.py` jako nowy plik (np. `check_product_2.py`)
2. Podmień adres URL i warunek dostępności
3. Dodaj nowy `step` w pliku `.github/workflows/check.yml` uruchamiający dodatkowy skrypt

## 📅 Harmonogram
Skrypt uruchamia się automatycznie co 15 minut między 7:00 a 22:00 UTC (czyli 9:00–00:00 czasu lokalnego w Polsce).

## 📜 Licencja

Projekt open-source, MIT License.

---

*Projekt tworzony z myślą o osobach szukających wyrobów medycznych, które często są chwilowo niedostępne w sprzedaży.*
