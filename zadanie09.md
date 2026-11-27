zadanie 1

Wynik `docker compose exec prometheus wget -qO- http://log:5001/metrics`:

```
# HELP log_attempts_total Number of logged hash check attempts
# TYPE log_attempts_total counter
log_attempts_total{found="true"} 3.0
log_attempts_total{found="false"} 7.0
```

Wartości odczytane z panelu w Grafanie:

- `found="true"`: 3
- `found="false"`: 7

Etykietą licznika jest tylko `found`, bo `hash_prefix` jako etykieta zapisałby w Prometheusie na stałe, które początki skrótów były sprawdzane i czy były w wycieku, czyli dokładnie te dane, których usługa log ma nie przechowywać. Drugi powód to liczba szeregów czasowych: każda wartość etykiety tworzy osobny szereg, a pięć znaków hex daje 16^5 ≈ 1 mln możliwych prefiksów (razy 2 dla `found`), co zapchałoby pamięć i dysk Prometheusa. Z `found` są tylko dwa szeregi. Po `docker compose up -d --build log` licznik spada do zera, bo Compose tworzy nowy kontener z nowym procesem, a licznik był trzymany tylko w pamięci starego procesu. Prometheus widzi to jako reset licznika i funkcje takie jak `rate()` uwzględniają ten reset.

zadanie 2

2.1
https://github.com/KrystianJc/breach-checker/actions/runs/45957839271
2.2
Usługa zapisała próbę:
Run docker compose logs log | grep "'hash_prefix': '7c4a8'"
time="2026-11-27T07:22:48Z" level=warning msg="The \"GRAFANA_PASSWORD\" variable is not set. Defaulting to a blank string."
log-1 | log: {'time': '2026-11-27T07:22:48+00:00', 'hash_prefix': '7c4a8', 'found': True}
2.3
Backend celowo ukrywa awarię usługi log: przy błędzie połączenia i tak odpowiada użytkownikowi poprawnym wynikiem, więc test przez frontend przeszedłby nawet wtedy, gdy obraz log nie działa albo backend nie może się z nim połączyć. Dopiero wpis w logu usługi log potwierdza, że obraz z rejestru działa i że komunikacja backend -> log jest poprawna, a przy okazji że trafia tam tylko początek skrótu.

zadanie 3

Pierwsze sprawdzenie (skrótu nie ma w bazie):

```
{
  "found": false
}
 czas: 0.235193s
```

Dodanie skrótu do bazy i ponowne sprawdzenie:

```
INSERT 0 1
```

```
{
  "found": false
}
 czas: 0.034556s
```

TTL i DEL:

```
(integer) 214
(integer) 1
```

Sprawdzenie po usunięciu klucza:

```
{
  "found": true
}
 czas: 0.125225s
```

Sprawdzenie przy zatrzymanym Redisie:

```
{
  "found": true
}
 czas: 4.088709s
```

Logi backendu:

```
backend-1  | check: hash=bc454... cache=miss
backend-1  | check: hash=bc454... cache=hit
backend-1  | check: hash=bc454... cache=miss
backend-1  | check: hash=bc454... cache=niedostępny
```

Backend odpowiadał false, bo przy pierwszym sprawdzeniu zapisał w Redisie wynik 0 z TTL 300 s, a potem brał odpowiedź z cache i nie pytał bazy, więc nie widział nowego skrótu, dopóki klucz nie wygasł albo nie został usunięty. Można to naprawić, usuwając klucz z Redisa przy każdym dodaniu skrótu do bazy (unieważnienie cache), albo nie zapisując w cache wyników 0 i zapamiętując tylko trafienia, bo skrót, który już jest w wycieku, z niego nie zniknie. Gdyby w find_cached nie było except redis.RedisError, wyjątek połączenia z Redisem przeszedłby do Flaska i użytkownik dostałby błąd 500, mimo że baza działa. Cache stałby się wtedy elementem koniecznym do działania aplikacji.
