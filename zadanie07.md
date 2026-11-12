# breach-checker-backend:prod (debian 13.7)

Total: 49 (HIGH: 49, CRITICAL: 0)

# breach-checker-frontend:prod (alpine 3.24.4)

Total: 3 (HIGH: 3, CRITICAL: 0)

z --ignore-unfixed:

# breach-checker-backend:prod (debian 13.7)

Total: 2 (HIGH: 2, CRITICAL: 0)

# breach-checker-frontend:prod (alpine 3.24.4)

Total: 3 (HIGH: 3, CRITICAL: 0)

--pull zmienił wynik — po pobraniu nowszej bazy liczba podatności HIGH spadła. Większa zmiana dotyczy tego obrazu, którego baza doczekała się w międzyczasie nowszego wydania z łatkami; druga baza zmieniła się mniej

docker compose logs backend
backend-1 | FileNotFoundError: [Errno 2] No usable temporary directory found in ['/tmp', '/var/tmp', '/usr/tmp', '/app']

docker compose exec backend touch /etc/test
touch: cannot touch '/etc/test': Read-only file system
docker compose exec backend touch /tmp/test
pusto
docker compose exec backend grep CapEff /proc/1/status
CapEff: 0000000000000000

> docker compose exec backend pytest
> =================================================================== test session starts ====================================================================
> platform linux -- Python 3.12.16, pytest-8.4.2, pluggy-1.7.0
> rootdir: /app
> collected 7 items

tests/test_check.py ....... [100%]

==================================================================== 7 passed in 0.33s =====================================================================

read_only blokuje zapis do całego systemu plików kontenera — atakujący nie podrzuci ani nie podmieni żadnego pliku. cap_drop: ALL odbiera procesowi wszystkie uprawnienia jądra , więc nawet przejęty proces ma mocno ograniczone pole działania. no-new-privileges blokuje zdobycie wyższych uprawnień w trakcie działania. Różnica względem USER appuser: appuser mówi tylko kim jest proces , a więc czego nie może dotknąć z racji właściciela plików; read_only działa niezależnie od tożsamości — blokuje zapis wszystkim, nawet gdyby proces był rootem.

docker history sekret-demo:plik
IMAGE CREATED CREATED BY SIZE COMMENT
fa6960c950f4 About a minute ago RUN /bin/sh -c rm /tmp/klucz.txt # buildkit 0B buildkit.dockerfile.v0
<missing> About a minute ago RUN /bin/sh -c test -s /tmp/klucz.txt && ech… 0B buildkit.dockerfile.v0
<missing> About a minute ago COPY klucz.txt /tmp/klucz.txt # buildkit 20B buildkit.dockerfile.v0
<missing> 6 days ago CMD ["/bin/sh"] 0B buildkit.dockerfile.v0
<missing> 6 days ago ADD alpine-minirootfs-3.22.8-x86_64.tar.gz /… 8.3MB buildkit.dockerfile.v0

Get-ChildItem obraz/blobs/sha256 | Where-Object { tar -tf $_.FullName 2>$null | Select-String '^tmp/klucz.txt$' } | ForEach-Object { tar -xOf $\_.FullName tmp/klucz.txt }
tajny-klucz-Krystian

RUN rm nie usunął sekretu, bo każda instrukcja tworzy osobną warstwę: polecenie rm dodaje tylko nową warstwę z informacją „ten plik jest usunięty“, a oryginał nadal leży w poprzedniej warstwie i da się go odzyskać z obrazu (docker save). Klucz potrzebny podczas budowania należało przekazać przez docker build --secret i RUN --mount=type=secret — wtedy jest dostępny jako plik tylko na czas jednej instrukcji i nie trafia ani do żadnej warstwy, ani do historii obrazu.
