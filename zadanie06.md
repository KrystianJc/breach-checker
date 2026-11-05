docker compose exec backend pytest -v
=================================================================== test session starts ====================================================================
platform linux -- Python 3.12.16, pytest-8.4.2, pluggy-1.7.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /app
collected 7 items

tests/test_check.py::test_leaked_hash_is_found PASSED [ 14%]
tests/test_check.py::test_unknown_hash_is_not_found PASSED [ 28%]
tests/test_check.py::test_missing_hash_field PASSED [ 42%]
tests/test_check.py::test_plaintext_password_is_rejected PASSED [ 57%]
tests/test_check.py::test_uppercase_hash_is_found PASSED [ 71%]
tests/test_check.py::test_too_short_hash_is_rejected PASSED [ 85%]
tests/test_check.py::test_non_hex_hash_is_rejected PASSED [100%]

==================================================================== 7 passed in 0.40s =====================================================================

docker compose exec backend pytest
=================================================================== test session starts ====================================================================
platform linux -- Python 3.12.16, pytest-8.4.2, pluggy-1.7.0
rootdir: /app
collected 7 items

tests/test_check.py ....F.. [100%]

========================================================================= FAILURES =========================================================================
**\*\***\*\***\*\***\*\***\*\***\*\***\*\***\_\_\_**\*\***\*\***\*\***\*\***\*\***\*\***\*\*** test_uppercase_hash_is_found **\*\***\*\***\*\***\*\***\*\***\*\***\*\***\_\_\_**\*\***\*\***\*\***\*\***\*\***\*\***\*\***

client = <FlaskClient <Flask 'app'>>

    def test_uppercase_hash_is_found(client):
        # app.py robi .lower() na skrocie, wiec WIELKIE litery tez sa wykrywane
        response = client.post("/check", json={"hash": LEAKED.upper()})

>       assert response.status_code == 200
>
> E assert 400 == 200
> E + where 400 = <WrapperTestResponse streamed [400 BAD REQUEST]>.status_code

tests/test_check.py:28: AssertionError
================================================================= short test summary info ==================================================================
FAILED tests/test_check.py::test_uppercase_hash_is_found - assert 400 == 200
=============================================================== 1 failed, 6 passed in 0.73s ================================================================

Testy z zajęć sprawdzały tylko skróty zapisane małymi literami, a dla takich danych kod działa identycznie z .lower() i bez niego, więc usunięcie przechodzi niezauważone. Dopiero test ze skrótem wielkimi literami wchodzi na tę ścieżkę i dlatego wykrywa brak .lower().

curl -s -o blad.html -w "HTTP %{http_code}\n" -X POST http://localhost:8080/api/check -H "Content-Type: application/json" -d '{"hash":"7c4a8d09ca3762af61e59520943dc26494f8941b"}'
HTTP 400

docker compose ps -a
NAME IMAGE COMMAND SERVICE CREATED STATUS PORTS
breach-checker-backend-1 breach-checker-backend "flask --app app run…" backend 31 minutes ago Exited (1) 9 seconds ago
breach-checker-db-1 postgres:16-alpine "docker-entrypoint.s…" db 42 minutes ago Exited (0) 3 minutes ago
breach-checker-frontend-1 breach-checker-frontend "/docker-entrypoint.…" frontend 42 minutes ago Up 42 minutes 0.0.0.0:8080->80/tcp, [::]:8080->80/tcp

> docker inspect breach-checker-backend-1
> [

    {
        "Id": "6a9211352fc7935bb352aae04b8e84d04e1bd229099ed6771a35efa9be0b5303",
        "Created": "2026-11-05T14:36:03.723539093Z",
        "Path": "flask",
        "Args": [
            "--app",
            "app",
            "run",
            "--host=0.0.0.0",
            "--port=5000",
            "--debug"
        ],
        "State": {
            "Status": "exited",
            "Running": false,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 0,
            "ExitCode": 1,
            "Error": "",
            "StartedAt": "2026-11-05T15:06:55.90092654Z",
            "FinishedAt": "2026-11-05T15:07:01.023571283Z",
            "Health": {
                "Status": "unhealthy",
                "FailingStreak": 0,
                "Log": [
                    {
                        "Start": "2026-11-05T15:04:42.790641141Z",
                        "End": "2026-11-05T15:04:43.166574059Z",
                        "ExitCode": 0,
                        "Output": ""
                    },
                    {
                        "Start": "2026-11-05T15:04:53.164155451Z",
                        "End": "2026-11-05T15:04:53.553953244Z",
                        "ExitCode": 0,
                        "Output": ""
                    },
                    {
                        "Start": "2026-11-05T15:05:03.555534146Z",
                        "End": "2026-11-05T15:05:03.964132724Z",
                        "ExitCode": 0,
                        "Output": ""
                    },
                    {
                        "Start": "2026-11-05T15:05:13.966129552Z",
                        "End": "2026-11-05T15:05:14.449883333Z",
                        "ExitCode": 0,
                        "Output": ""
                    },
                    {
                        "Start": "2026-11-05T15:05:26.195966669Z",
                        "End": "2026-11-05T15:05:26.589753129Z",
                        "ExitCode": 137,
                        "Output": ""
                    }
                ]
            }
        },
        "Image": "sha256:3a9fa5bf76cf26b4236801bf18a3ec4913ce149bf5fe57129cac8c281e82b938",
        "ResolvConfPath": "/var/lib/docker/containers/6a9211352fc7935bb352aae04b8e84d04e1bd229099ed6771a35efa9be0b5303/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/6a9211352fc7935bb352aae04b8e84d04e1bd229099ed6771a35efa9be0b5303/hostname",
        "HostsPath": "/var/lib/docker/containers/6a9211352fc7935bb352aae04b8e84d04e1bd229099ed6771a35efa9be0b5303/hosts",
        "LogPath": "",
        "Name": "/breach-checker-backend-1",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": [
                "C:\\Users\\jacki\\Documents\\Politechnika\\Metody_wirtualizacji\\breach-checker\\backend:/app:rw"
            ],
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "local",
                "Config": {}
            },
            "NetworkMode": "breach-checker_default",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                0,
                0
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": null,
            "DnsOptions": null,
            "DnsSearch": null,
            "ExtraHosts": [],
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": null,
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": null,
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/acpi",
                "/proc/asound",
                "/proc/interrupts",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/sys/devices/virtual/powercap",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "ID": "6a9211352fc7935bb352aae04b8e84d04e1bd229099ed6771a35efa9be0b5303",
                "LowerDir": "/var/lib/docker/overlay2/71e055c85c73b340e03dc0079a6d452ea1f36348270a2e3263e8ad4c6475ec41-init/diff:/var/lib/docker/overlay2/zozcidogugdbamjd02m6uvj9h/diff:/var/lib/docker/overlay2/0a4wnhkcku34heoz3csd4x7pr/diff:/var/lib/docker/overlay2/ph37d0x12ssyfes7hnkvcd18k/diff:/var/lib/docker/overlay2/8eb8c49759d64fe7dc08a65fc6e48f7a61c9a04e38159a41ae107917832bfe8a/diff:/var/lib/docker/overlay2/8f35cf46d122f3c05a4edd52dbc796bc8bdf6ed30d01b7709488ac4baacb364e/diff:/var/lib/docker/overlay2/c3a63e70cbdd4305e4115755c801d4fba15e00f96a2f71bbae9e053cc012255b/diff:/var/lib/docker/overlay2/d4a71df06a6922ded8ebdf14f64b8905847be1e55f8a5187004fb62c5f12a2c2/diff",
                "MergedDir": "/var/lib/docker/overlay2/71e055c85c73b340e03dc0079a6d452ea1f36348270a2e3263e8ad4c6475ec41/merged",
                "UpperDir": "/var/lib/docker/overlay2/71e055c85c73b340e03dc0079a6d452ea1f36348270a2e3263e8ad4c6475ec41/diff",
                "WorkDir": "/var/lib/docker/overlay2/71e055c85c73b340e03dc0079a6d452ea1f36348270a2e3263e8ad4c6475ec41/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [
            {
                "Type": "bind",
                "Source": "C:\\Users\\jacki\\Documents\\Politechnika\\Metody_wirtualizacji\\breach-checker\\backend",
                "Destination": "/app",
                "Mode": "rw",
                "RW": true,
                "Propagation": "rprivate"
            }
        ],
        "Config": {
            "Hostname": "6a9211352fc7",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": true,
            "AttachStderr": true,
            "ExposedPorts": {
                "5000/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "DB_NAME=breachdb",
                "DB_USER=breach",
                "DB_PASSWORD=sekretnehaslo",
                "DB_HOST=db",
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "LANG=C.UTF-8",
                "GPG_KEY=7169605F62C751356D054A26A821E680E5FA6305",
                "PYTHON_VERSION=3.12.16",
                "PYTHON_SHA256=b5796915dc45ff745cfb4e990a7e7c93d6f546328a102ce31448d69ebc37575c"
            ],
            "Cmd": [
                "flask",
                "--app",
                "app",
                "run",
                "--host=0.0.0.0",
                "--port=5000",
                "--debug"
            ],
            "Healthcheck": {
                "Test": [
                    "CMD",
                    "python",
                    "-c",
                    "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"
                ],
                "Interval": 10000000000,
                "Timeout": 5000000000,
                "StartPeriod": 5000000000,
                "Retries": 3
            },
            "Image": "breach-checker-backend",
            "Volumes": null,
            "WorkingDir": "/app",
            "Entrypoint": null,
            "Labels": {
                "com.docker.compose.config-hash": "fcb1f61f78bef76258acc76aac1ff169cdd3e608db9d0ac32c895fe94da394e8",
                "com.docker.compose.container-number": "1",
                "com.docker.compose.depends_on": "db:service_healthy:false",
                "com.docker.compose.image": "sha256:3a9fa5bf76cf26b4236801bf18a3ec4913ce149bf5fe57129cac8c281e82b938",
                "com.docker.compose.oneoff": "False",
                "com.docker.compose.project": "breach-checker",
                "com.docker.compose.project.config_files": "C:\\Users\\jacki\\Documents\\Politechnika\\Metody_wirtualizacji\\breach-checker\\docker-compose.yml,C:\\Users\\jacki\\Documents\\Politechnika\\Metody_wirtualizacji\\breach-checker\\docker-compose.override.yml",
                "com.docker.compose.project.working_dir": "C:\\Users\\jacki\\Documents\\Politechnika\\Metody_wirtualizacji\\breach-checker",
                "com.docker.compose.replace": "backend-1",
                "com.docker.compose.service": "backend",
                "com.docker.compose.version": "5.5.1"
            }
        },
        "NetworkSettings": {
            "SandboxID": "",
            "SandboxKey": "",
            "Ports": {},
            "Networks": {
                "breach-checker_default": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": [
                        "breach-checker-backend-1",
                        "backend"
                    ],
                    "DriverOpts": null,
                    "GwPriority": 0,
                    "NetworkID": "6997ff81f19196cb0b5c9792787ad4d3cc79f6464a4a44f2c57c60c6db20304c",
                    "EndpointID": "",
                    "Gateway": "",
                    "IPAddress": "",
                    "MacAddress": "",
                    "IPPrefixLen": 0,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "DNSNames": [
                        "breach-checker-backend-1",
                        "backend",
                        "6a9211352fc7"
                    ]
                }
            }
        }
    }

]
ocker compose logs --tail 20 backend
backend-1 | raise e from None
backend-1 | File "/usr/local/lib/python3.12/site-packages/flask/cli.py", line 963, in run_command
backend-1 | app: WSGIApplication = info.load_app() # pyright: ignore
backend-1 | ^^^^^^^^^^^^^^^
backend-1 | File "/usr/local/lib/python3.12/site-packages/flask/cli.py", line 349, in load_app
backend-1 | app = locate_app(import_name, name)
backend-1 | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
backend-1 | File "/usr/local/lib/python3.12/site-packages/flask/cli.py", line 245, in locate_app
backend-1 | **import**(module_name)
backend-1 | File "/app/app.py", line 19, in <module>
backend-1 | conn = connect()
backend-1 | ^^^^^^^^^
backend-1 | File "/app/app.py", line 11, in connect
backend-1 | return psycopg2.connect(
backend-1 | ^^^^^^^^^^^^^^^^^
backend-1 | File "/usr/local/lib/python3.12/site-packages/psycopg2/**init**.py", line 122, in connect
backend-1 | conn = \_connect(dsn, connection_factory=connection_factory, \*\*kwasync)
backend-1 | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
backend-1 | psycopg2.OperationalError: could not translate host name "db" to address: No address associated with hostname
backend-1 |

docker stats
CONTAINER ID NAME CPU % MEM USAGE / LIMIT MEM % NET I/O BLOCK I/O PIDS
5b28923eca34 breach-checker-frontend-1 0.00% 10.01MiB / 2.765GiB 0.35% 50.5kB / 50.5kB 11.1MB / 8.19kB 9

blad.html zawierał stronę debugera Flaska z pełnym śladem
wyjątku: ścieżki plików na serwerze , nazwy i wersje bibliotek
(Flask, psycopg2), nazwę hosta bazy oraz fragmenty kodu z numerami linii.
Na produkcji taka odpowiedź ujawnia wewnętrzną budowę aplikacji

curl http://localhost:8080/nginx.conf
server {
listen 80;

    # Pliki strony (index.html, style.css, script.js)
    location / {
        root /usr/share/nginx/html;
        index index.html;
    }

    # Wszystko pod /api/ nginx przekazuje do usługi backend w sieci Compose
    location /api/ {
        proxy_pass http://backend:5000/;
    }

}
curl -I http://localhost:8080/nginx.conf
HTTP/1.1 404 Not Found
Server: nginx/1.31.6
Date: Thu, 05 Nov 2026 15:25:29 GMT
Content-Type: text/html
Content-Length: 153
Connection: keep-alive

Obraz produkcyjny nie ma tego problemu, bo frontend/Dockerfile kopiuje do katalogu serwowanego przez nginx tylko wybrane pliki strony (COPY konkretnych plików). nginx.conf i Dockerfile zostają poza tym katalogiem — w wersji deweloperskiej błąd brał się wyłącznie z bind-mountu całego folderu ./frontend.
Montowanie całego katalogu projektu pod katalog WWW jest ryzykowne, bo serwer udostępnia wtedy wszystko, co w nim leży — konfiguracje, Dockerfile, pliki pomocnicze, a nierzadko też .git czy pliki z sekretami — co ujawnia wewnętrzną strukturę aplikacji i może prowadzić do wycieku danych uwierzytelniających.