docker compose up -d --build

[+] up 6/6
✔ Image breach-checker-frontend Built 4.0s
✔ Image breach-checker-backend Built 4.0s
✔ Network breach-checker_default Created 0.1s
✔ Container breach-checker-db-1 Healthy 6.7s
✔ Container breach-checker-backend-1 Healthy 12.6s
✔ Container breach-checker-frontend-1 Started

docker compose ps
NAME IMAGE COMMAND SERVICE CREATED STATUS PORTS
breach-checker-backend-1 breach-checker-backend "python app.py" backend About a minute ago Up About a minute (healthy) 5000/tcp
breach-checker-db-1 postgres:16-alpine "docker-entrypoint.s…" db About a minute ago Up About a minute (healthy) 5432/tcp
breach-checker-frontend-1 breach-checker-frontend "/docker-entrypoint.…" frontend About a minute ago Up About a minute 0.0.0.0:8080->80/tcp, [::]:8080->80/tcp

Po Insert:
'{"hash":"bc45408273d7e1914b741c3407b0b559764f7876"}' | curl.exe -X POST http://localhost:8080/api/check -H "Content-Type: application/json" -d '@-'
{"found":true}

Po docker compose down + docker compose up -d:
'{"hash":"bc45408273d7e1914b741c3407b0b559764f7876"}' | curl.exe -X POST http://localhost:8080/api/check -H "Content-Type: application/json" -d '@-'
{"found":true}

Po docker compose down -v + docker compose up -d:
'{"hash":"bc45408273d7e1914b741c3407b0b559764f7876"}' | curl.exe -X POST http://localhost:8080/api/check -H "Content-Type: application/json" -d '@-'
{"found":false}

Dlaczego skrót przetrwał down, a nie przetrwał down -v; dlaczego po down -v w bazie znów są 89 skróty z próbki, choć cała baza została skasowana.
Skrót przetrwał down ponieważ dodany skrót został zapisany w wolumenie a komenda z -v usuwa właśnie wolumen dlatego wtedy dodanego skrótu nie odnajdziemy. W bazie z powrotem sa 89 skróty ponieważ dane sa w pliku init.sql który jest dodany za pomoca bind mount i ta baza dodawana jest przy inicjalizacji.

docker compose ps
NAME IMAGE COMMAND SERVICE CREATED STATUS PORTS
breach-checker-backend-1 breach-checker-backend "python app.py" backend 8 minutes ago Up 7 minutes (healthy) 5000/tcp
breach-checker-backend-2 breach-checker-backend "python app.py" backend 4 minutes ago Up 4 minutes (healthy) 5000/tcp
breach-checker-backend-3 breach-checker-backend "python app.py" backend 4 minutes ago Up 4 minutes (healthy) 5000/tcp
breach-checker-db-1 postgres:16-alpine "docker-entrypoint.s…" db 8 minutes ago Up 8 minutes (healthy) 5432/tcp
breach-checker-frontend-1 breach-checker-frontend "/docker-entrypoint.…" frontend 8 minutes ago Up About a minute 0.0.0.0:8080->80/tcp, [::]:8080->80/tcp

docker compose exec frontend nslookup backend
Server: 127.0.0.11
Address: 127.0.0.11:53

Non-authoritative answer:

Non-authoritative answer:
Name: backend
Address: 172.19.0.5
Name: backend
Address: 172.19.0.3
Name: backend
Address: 172.19.0.6

docker compose logs backend przed restartem frontendu:
backend-1 | check: hash=bc454...
backend-1 | 172.19.0.4 - - [29/Oct/2026 15:21:06] "POST /check HTTP/1.1" 200 -
backend-1 | check: hash=bc454...
backend-1 | 172.19.0.4 - - [29/Oct/2026 15:21:06] "POST /check HTTP/1.1" 200 -
backend-1 | check: hash=bc454...
backend-1 | 172.19.0.4 - - [29/Oct/2026 15:21:06] "POST /check HTTP/1.1" 200 -
backend-1 | check: hash=bc454...
backend-1 | 172.19.0.4 - - [29/Oct/2026 15:21:07] "POST /check HTTP/1.1" 200 -
backend-1 | check: hash=bc454...
backend-1 | 172.19.0.4 - - [29/Oct/2026 15:21:07] "POST /check HTTP/1.1" 200 -
backend-1 | check: hash=bc454...

docker compose logs backend po restarcie frontendu:
backend-2 | check: hash=bc454...
backend-2 | 127.0.0.1 - - [29/Oct/2026 15:21:06] "GET /health HTTP/1.1" 200 -
backend-2 | 172.19.0.4 - - [29/Oct/2026 15:21:06] "POST /check HTTP/1.1" 200 -
backend-1 | check: hash=bc454...
backend-1 | 172.19.0.4 - - [29/Oct/2026 15:21:06] "POST /check HTTP/1.1" 200 -
backend-3 | check: hash=bc454...
backend-3 | 172.19.0.4 - - [29/Oct/2026 15:21:06] "POST /check HTTP/1.1" 200 -
backend-2 | check: hash=bc454...
backend-2 | 172.19.0.4 - - [29/Oct/2026 15:21:06] "POST /check HTTP/1.1" 200 -
backend-1 | check: hash=bc454...

dlaczego przed restartem frontendu ruch trafiał do jednej repliki (wskazówka: kiedy nginx tłumaczy nazwę backend na adresy - patrz krok 2); dlaczego skalowanie byłoby niemożliwe, gdyby backend nadal miał ports: "5000:5000"
Dlaczego przed restartem frontendu ruch trafiał do jednej repliki - Nginx domyślnie tłumaczy nazwę domenową backend na adres IP tylko jeden raz – w momencie swojego startu.
Drugie pytanie: Zapis ports: "5000:5000" oznacza przekierowanie portu z wnętrza kontenera bezpośrednio na port systemu operacyjnego hosta, dlatego tylko jeden proces na maszynie może nasłuchiwać na danym porcie w tym samym czasie
