curl.exe 'http://localhost:5000/health'
{"status":"ok"}

docker logs backend:
172.19.0.1 - - [22/Oct/2026 14:21:56] "GET /health HTTP/1.1" 200 -

docker run --rm --network breach-net healthcheck-probe
backend: OK
docker run --rm healthcheck-probe
backend: UNREACHABLE

docker stop backend
backend
docker run --rm --network breach-net healthcheck-probe
backend: UNREACHABLE

docker start backend
backend
docker run --rm --network breach-net healthcheck-probe
backend: OK

Bez flagi --network nazwa backend nie działa, ponieważ Docker domyślnie uruchamia kontenery w izolowanej sieci o nazwie bridge, która ma wyłączony mechanizm DNS

Po restarcie:
docker exec backend cat /tmp/notatka.txt
notatka

Po rm i run:
docker exec backend cat /tmp/notatka.txt
cat: /tmp/notatka.txt: No such file or directory

docker run --rm -v breach-dane:/dane alpine sh -c "date >> /dane/historia.txt; cat /dane/historia.txt"
Thu Oct 22 14:38:17 UTC 2026
Thu Oct 22 14:38:22 UTC 2026

Plik /tmp/notatka.txt przetrwał restart, bo docker restart zatrzymuje i uruchamia ten sam kontener razem z jego warstwą zapisywalną. Po docker rm ta warstwa została usunięta, a nowy docker run utworzył kontener z czystego obrazu, w którym tego pliku nie ma. historia.txt przetrwała, bo była zapisana w wolumenie breach-dane, który istnieje niezależnie od kontenerów i nie jest usuwany razem z nimi. Lista wycieków przetrwałaby docker rm, bo plik z hashami nie jest przechowywany w kontenerze, tylko podłączany do niego bind mountem z dysku hosta.
