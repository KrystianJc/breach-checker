zadanie 1:
1.1
https://github.com/KrystianJc/breach-checker/actions/runs/44696676358 (usunięte </h1>)
1.2
#13 [lint 5/5] RUN htmlhint index.html
#13 0.153
#13 0.161 /site/index.html
#13 0.162 L16 | <h1>Sprawdź hasło tutaj - Breach Checker
#13 0.162 ^ Tag must be paired, missing: [ </h1> ], start tag match failed [ <h1> ] on line 16. (tag-pair)
#13 0.162
#13 0.163 Scanned 1 files, found 1 errors in 1 files (12 ms)
#13 ERROR: process "/bin/sh -c htmlhint index.html" did not complete successfully: exit code: 1

---

> [lint 5/5] RUN htmlhint index.html:
> 0.153
> 0.161 /site/index.html
> 0.162 L16 | <h1>Sprawdź hasło tutaj - Breach Checker
> 0.162 ^ Tag must be paired, missing: [ </h1> ], start tag match failed [ <h1> ] on line 16. (tag-pair)
> 0.162
> 0.163 Scanned 1 files, found 1 errors in 1 files (12 ms)

1.3
https://github.com/KrystianJc/breach-checker/actions/runs/44697268385
1.4
W zielonym uruchomieniu verify pobiera z rejestru oba obrazy (backend i frontend) z tagiem tego samego commita, więc test dymny sprawdza dokładnie te obrazy, które zostały opublikowane i trafiłyby na produkcję. We wcześniejszej wersji z rejestru pochodził tylko backend, a frontend był budowany na runnerze z kodu, więc opublikowany obraz frontendu w ogóle nie był sprawdzany.

zadanie 2
2.1
https://github.com/KrystianJc/breach-checker/actions/runs/44699131497
2.2
https://github.com/KrystianJc/breach-checker/actions/runs/44699726406
2.3
Po nieudanym uruchomieniu latest backendu nadal wskazywał na poprzednią wersję obrazu, która przeszła weryfikację, bo job promote został pominięty, a zepsuty obraz dostał tylko tag skrótu commita. To ważne, bo docker pull bez podania tagu pobiera właśnie latest, więc ktoś, kto pobiera obraz domyślnie, zawsze dostanie działającą wersję, a nie obraz, który nie przeszedł testu dymnego.

zadanie 3
3.1
docker pull ghcr.io/krystianjc/breach-checker-backend:latest
latest: Pulling from krystianjc/breach-checker-backend
c74288390aeb: Already exists
68bced9e0afa: Already exists
2dc99d2d0a39: Already exists
05e0eee5572e: Already exists
df33aa74aa56: Pull complete
7c702b350ce7: Pull complete
70d944561fab: Pull complete
0a705fcee309: Pull complete
7f5a68308785: Pull complete
Digest: sha256:6bf969cac15a51cd6a90ee91fdfbd8ea47fdcebbc176c9542f8a62d9ba8fd964
Status: Downloaded newer image for ghcr.io/krystianjc/breach-checker-backend:latest
ghcr.io/krystianjc/breach-checker-backend:latest

docker pull ghcr.io/krystianjc/breach-checker-backend:c5000a8c936f79d339d1e50051406ef53450c563
c5000a8c936f79d339d1e50051406ef53450c563: Pulling from krystianjc/breach-checker-backend
Digest: sha256:6bf969cac15a51cd6a90ee91fdfbd8ea47fdcebbc176c9542f8a62d9ba8fd964
Status: Downloaded newer image for ghcr.io/krystianjc/breach-checker-backend:c5000a8c936f79d339d1e50051406ef53450c563
ghcr.io/krystianjc/breach-checker-backend:c5000a8c936f79d339d1e50051406ef53450c563

docker images --digests ghcr.io/krystianjc/breach-checker-backend
REPOSITORY TAG DIGEST IMAGE ID CREATED SIZE
ghcr.io/krystianjc/breach-checker-backend c5000a8c936f79d339d1e50051406ef53450c563 sha256:6bf969cac15a51cd6a90ee91fdfbd8ea47fdcebbc176c9542f8a62d9ba8fd964 82c12def1bfd 8 minutes ago 142MB
ghcr.io/krystianjc/breach-checker-backend latest sha256:6bf969cac15a51cd6a90ee91fdfbd8ea47fdcebbc176c9542f8a62d9ba8fd964 82c12def1bfd 8 minutes ago 142MB

docker push ghcr.io/krystianjc/breach-checker-backend:latest
The push refers to repository [ghcr.io/krystianjc/breach-checker-backend]
db8846f152a4: Layer already exists
4cd3178a3f32: Layer already exists
4b0f45fd49c4: Layer already exists
19c1c9fc7fce: Layer already exists
71c0774e74ff: Layer already exists
340931a1d986: Layer already exists
96a69f98ae07: Layer already exists
3dc3efdf0110: Layer already exists
dd57f90311a2: Layer already exists
unauthorized: unauthenticated: User cannot be authenticated with the token provided.

3.2
Oba tagi (latest i skrót commita) mają ten sam digest i ten sam IMAGE ID, więc wskazują na dokładnie ten sam obraz, a tag jest tylko etykietą przypiętą do tej zawartości. pull zadziałał bez logowania, bo pakiet jest publiczny i pobierać może go każdy, a push się nie powiódł, bo publikacja zawsze wymaga uwierzytelnienia tokenem z prawem zapisu. Rejestr pozwolił nawet sprawdzić, że warstwy już istnieją (to tylko odczyt), ale odrzucił zapis tagu. Token z zakresem write:packages z kroku 1 służył właśnie do tego: do zalogowania się w GHCR i ręcznej publikacji obrazu (wtedy pakiet był prywatny, więc był potrzebny też do pobrania go).
