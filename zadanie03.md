docker inspect krystian-frontend:v1
[
{
"Id": "sha256:77c06d054b920669ce7d36112d1d2c40f8fe306ccd60162890423bee66d9020e",
"RepoTags": [
"krystian-frontend:latest",
"krystian-frontend:v1"
],
"RepoDigests": [],
"Comment": "buildkit.dockerfile.v0",
"Created": "2026-10-15T14:19:28.892039479Z",
"Config": {
"ExposedPorts": {
"80/tcp": {}
},
"Env": [
"PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
"NGINX_VERSION=1.31.6",
"PKG_RELEASE=1",
"DYNPKG_RELEASE=1",
"NJS_VERSION=1.0.1",
"NJS_RELEASE=1",
"ACME_VERSION=0.4.1"
],
"Entrypoint": [
"/docker-entrypoint.sh"
],
"Cmd": [
"nginx",
"-g",
"daemon off;"
],
"WorkingDir": "/",
"Labels": {
"autor": "Krystian Jackiewicz",
"data": "2026-10-15",
"maintainer": "krystian.jackiewicz@example.com"
},
"StopSignal": "SIGQUIT"
},
"Architecture": "amd64",
"Os": "linux",
"Size": 155065201,
"GraphDriver": {
"Data": {
"LowerDir": "/var/lib/docker/overlay2/y0enw3itl4y2bju1u8508t4vn/diff:/var/lib/docker/overlay2/1004i5b4gelmamo7iif29vhoy/diff:/var/lib/docker/overlay2/26d58e5ffbdcd38810a78a4f6c5d1ee591e631146782ff2ea821ffd5b7ee30e6/diff:/var/lib/docker/overlay2/b53fb940ddc685ce09fbc0034336fb31a51bd6a57ab646007a253ac3ec1ed4a1/diff:/var/lib/docker/overlay2/5dc6fb6badcbbc7cb53321a84e87b8b14fe33dd5a5f954f227a6e6c1ec2b28f5/diff:/var/lib/docker/overlay2/aa5b293d79872782264f97255b7ac9294ebb9a025410f23bc975c9c260c57349/diff:/var/lib/docker/overlay2/8e0a7cdf43ab3ef908d66ff05057e26c32eed34e6d0ae82bf3fd9db32abb49a0/diff:/var/lib/docker/overlay2/f1c7b180724ae243554671c2450107bddbe4a30b2cf8e6a0c4f9efb2f100811e/diff:/var/lib/docker/overlay2/6df9fb2be661f215ca79ccb2a2117a7c7965bbb27d82e43a10e4fbea1b6fc750/diff:/var/lib/docker/overlay2/ae61952f707736cfec785702e3d95c8516059cb709694a982e138d0f663c231e/diff",
"MergedDir": "/var/lib/docker/overlay2/sjzf49lti0zleztiblwk7c3i8/merged",
"UpperDir": "/var/lib/docker/overlay2/sjzf49lti0zleztiblwk7c3i8/diff",
"WorkDir": "/var/lib/docker/overlay2/sjzf49lti0zleztiblwk7c3i8/work"
},
"Name": "overlay2"
},
"RootFS": {
"Type": "layers",
"Layers": [
"sha256:74d97c428c51a828f9051a7a40a53ff1fc99e54fc30323ce36760701b0b7f711",
"sha256:379f51bf5b58bf458dfe39fe97ba49d63950929004af1808361bfe01ba73d6d0",
"sha256:641b74319bab4250ece7d99c1e71fba36e67931d64b62a1d574a56986d45dae0",
"sha256:2a7ed9afc1c38e245bbe331a4bbf99010cc9ff2ae546ee9507373a3a2dc80f0c",
"sha256:149ab1e5d6caa8add417a7dc26743baa867bf078b3c6aafc96b8197221a87a1c",
"sha256:41473198c04ae23f0434ac3a73f8e52549312be4638d2979bc1df9d209bdb9c0",
"sha256:c86f6810da0b81ee848c1e6cc4bc22c0b7bd4f553f81ef3a33c41791b90631a2",
"sha256:001b5608a9297e16ed0253a4694ca1cc98fa554c7e39c36ca652742cfc294efc",
"sha256:790258fd7fe44cd20313b857b9fa9b66157784f3b5e5787cf38bf2eac34471fd",
"sha256:4dc21b2c022dce27ccf55bdf6bad0e9ef11d27544d32de1ed35bd8a8306b9387",
"sha256:4e13475d1b9c4cc4a8d9a1fbb63510c003e749c3145599457e688c5200968912"
]
},
"Metadata": {
"LastTagTime": "2026-10-15T14:19:29.055460873Z"
}
}
]

docker history krystian-frontend:v1
IMAGE CREATED CREATED BY SIZE COMMENT
77c06d054b92 2 minutes ago EXPOSE [80/tcp] 0B buildkit.dockerfile.v0
<missing> 2 minutes ago RUN /bin/sh -c htmlhint /usr/share/nginx/htm… 0B buildkit.dockerfile.v0
<missing> 2 minutes ago COPY . /usr/share/nginx/html # buildkit 1.66kB buildkit.dockerfile.v0
<missing> 29 minutes ago RUN /bin/sh -c apk add --no-cache nodejs npm… 92.1MB buildkit.dockerfile.v0
<missing> 29 minutes ago LABEL autor=Krystian Jackiewicz data=2026-10… 0B buildkit.dockerfile.v0
<missing> 29 minutes ago LABEL maintainer=krystian.jackiewicz@example… 0B buildkit.dockerfile.v0
<missing> 3 weeks ago RUN /bin/sh -c set -x && apkArch="$(cat … 50.1MB buildkit.dockerfile.v0
<missing> 3 weeks ago ENV ACME_VERSION=0.4.1 0B buildkit.dockerfile.v0
<missing> 3 weeks ago ENV NJS_RELEASE=1 0B buildkit.dockerfile.v0
<missing> 3 weeks ago ENV NJS_VERSION=1.0.1 0B buildkit.dockerfile.v0
<missing> 3 weeks ago CMD ["nginx" "-g" "daemon off;"] 0B buildkit.dockerfile.v0
<missing> 3 weeks ago STOPSIGNAL SIGQUIT 0B buildkit.dockerfile.v0
<missing> 3 weeks ago EXPOSE map[80/tcp:{}] 0B buildkit.dockerfile.v0
<missing> 3 weeks ago ENTRYPOINT ["/docker-entrypoint.sh"] 0B buildkit.dockerfile.v0
<missing> 3 weeks ago COPY 30-tune-worker-processes.sh /docker-ent… 4.62kB buildkit.dockerfile.v0
<missing> 3 weeks ago COPY 20-envsubst-on-templates.sh /docker-ent… 3.03kB buildkit.dockerfile.v0
<missing> 3 weeks ago COPY 15-local-resolvers.envsh /docker-entryp… 389B buildkit.dockerfile.v0
<missing> 3 weeks ago COPY 10-listen-on-ipv6-by-default.sh /docker… 2.14kB buildkit.dockerfile.v0
<missing> 3 weeks ago COPY docker-entrypoint.sh / # buildkit 1.62kB buildkit.dockerfile.v0
<missing> 3 weeks ago RUN /bin/sh -c set -x && addgroup -g 101… 4.39MB buildkit.dockerfile.v0
<missing> 3 weeks ago ENV DYNPKG_RELEASE=1 0B buildkit.dockerfile.v0
<missing> 3 weeks ago ENV PKG_RELEASE=1 0B buildkit.dockerfile.v0
<missing> 3 weeks ago ENV NGINX_VERSION=1.31.6 0B buildkit.dockerfile.v0
<missing> 3 weeks ago LABEL maintainer=NGINX Docker Maintainers <d… 0B buildkit.dockerfile.v0
<missing> 3 weeks ago CMD ["/bin/sh"] 0B buildkit.dockerfile.v0
<missing> 3 weeks ago ADD alpine-minirootfs-3.24.2-x86_64.tar.gz /… 8.42MB buildkit.dockerfile.v0

Warstwy które pochodzą z obrazu bazowego to te które są pochodzą z 3 tygodni a z mojego Docker file te wcześniejsze. Niektóre mają rozmiar 0B ponieważ modyfikują tylko metadane obrazu. Widać tylko moją wersję maintainer ponieważ jest ona nadpisywana najnowszymi informacjami.

build.txt:
Thu Oct 15 14:31:18 UTC 2026
Thu Oct 15 14:31:18 UTC 2026

docker ps
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
2106ca6b1b4a krystian-frontend:latest "/docker-entrypoint.…" About a minute ago Up About a minute 0.0.0.0:8081->80/tcp, [::]:8081->80/tcp frontend3
343728b62573 krystian-frontend:latest "/docker-entrypoint.…" 2 minutes ago Up 2 minutes 0.0.0.0:8080->80/tcp, [::]:8080->80/tcp frontend

Czas jest taki sam ponieważ RUN date > /usr/share/nginx/html/build.txt jest zapisane w pamięci Cache

zadanie 3

docker run --rm breach-checker-frontend:v2 cat /etc/nginx/conf.d/default.conf

location / {
root /usr/share/nginx/html;
index index.html index.htm;
}
Dyrektywa `root` mówi nginx, z którego katalogu serwować pliki strony, dlatego nasze pliki muszą trafić właśnie do `/usr/share/nginx/html`, bo tylko stamtąd nginx je udostępni.

zadanie 4
docker exec bc-broken ls /usr/share/nginx
html
index.html
script.js
style.css

docker exec bc-broken ls /usr/share/nginx/html
50x.html
build.txt
index.html

htmlhint sprawdził plik /usr/share/nginx/html/index.html, czyli domyślną stronę nginx z obrazu bazowego, a nie nasz formularz. Ta strona jest poprawnym plikiem, więc htmlhint zakończył się sukcesem i build przeszedł bez błędu.

zadanie 5
docker rmi breach-checker-frontend:latest
Untagged: breach-checker-frontend:latest

docker rmi breach-checker-frontend:v2
Untagged: breach-checker-frontend:v2
Deleted: sha256:c918d8b8e2e64b3421692a4190c4346f8498ae54c305cccfc2bddf347d718f07

Po usunięciu latest obraz v2 nadal istniał, bo zniknęła tylko jedna z nazw wskazujących na ten sam IMAGE ID. docker rmi faktycznie usuwa obraz z dysku dopiero wtedy, gdy usuwamy ostatni tag wskazujący na dany IMAGE ID i żaden kontener z niego nie korzysta.
