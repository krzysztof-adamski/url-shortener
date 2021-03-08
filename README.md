# url-shortener

http://shortener.adamski.work

http://shortener.adamski.work/admin

login: ************
password: *****

1. Uruchomienie aplikacji w dokerze:

make start-build

2. Zatrzymanie

make stop

***Requirements***

Wymagany plik .env ze zmiennymi środowiskowymi

```env
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
POSTGRES_HOST=

DEBUG=False
SECRET_KEY=
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] twoje_ip twoja_domena
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=
SQL_USER=
SQL_PASSWORD=
SQL_HOST=
SQL_PORT=
PORT=
SCHEME=
DOMAIN=twoja_domena
```


