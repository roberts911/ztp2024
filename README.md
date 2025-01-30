# Zaawansowane Techniki Programowania 2024

## Projekt zaliczeniowy

### Założenia
Celem projektu jest opracowanie systemu przetwarzania danych, przychodzących w czasie rzeczywistym od współpracowników/sprzedawców dużej firmy handlowej. Sposób wymiany danych powinien zapewniać łatwą integrację z systemem współpracownika, nieinteraktywną/zautomatyzowaną wymianę danych, opartą na łatwo wdrażalnych protokołach (http). Elementem odpowiadającym za komunikację wszystkich jego części jest centralna baza danych.
Scalenie backendów w jednolity serwis jest poza zakresem projektu.

### Ograniczenia technologiczne
Ze względu na konieczność kooperacji różnych części projektu, wybór środowiska bazodanowego zostaje narzucony (PostgreSQL). Technologie realizacji poszczególnych części są dowolne, ograniczeniem jest tu uniwersalność wdrożeniowa (Java, Python, Javascript oraz inne środowiska niezależne od platformy uruchomieniowej). Nie zakłada się użycia metod komunikacji wymagających specjalnej konfiguracji/infrastruktury (np. mail).

### Części projektu

#### **SZU** - serwis zgłoszenia udziału współpracownika w programie
Ze względu interaktywny charakter procesu (zarówno od strony współpracownika, jak i centrali firmy), rozwiązanie powinno być klasyczną aplikacją webową z frontendem, pozwalającą na założenie kont w systemie.

Od strony współpracownika serwis ma stwarzać możliwości:
- złożenie wniosku o założenia konta, z określeniem NIPu (który jest kluczem głównym współpracowników), oraz danych tj. nazwa/nazwisko, kontakt itp.
- sprawdzenie stanu wniosku
- po pozytywnym rozpatrzeniu przez centralę firmy, wyświetlenie klucza dostępowego (klucza API) dla celów integracyjnych (początkowo może to być np. UUIDv4)

Od strony centrali firmy, serwis oferuje przeglądanie założonych kont oraz akceptację wniosku, połączoną z wytworzeniem klucza API dla współpracownika.


## Pobranie/aktualizacja projektu

Pobranie ostatniej wersji do nowego katalogu ``ztp2024``
```
git clone https://github.com/roberts911/ztp2024.git
```
Aktualizacja posiadanego kodu do ostatniej wersji
```
cd ztp2024
git reset
git pull
```
## Odpalenie bazy PostgreSQL na dockerze
```
docker run --name postgres -e POSTGRES_PASSWORD=qwerty -e POSTGRES_DB=ztp2024 -p 5432:5432 -d postgres
```

## Migracja bazy jeśli trzeba
```
cd szu
python manage.py makemigrations
python manage.py migrate
```

## Odpalenie apki
```
cd szu
python manage.py runserver
```

