# SHA-1 hasła "123456" (jest w próbce) i "Kot-w-Kapeluszu-2026" (nie ma go w próbce)
LEAKED = "7c4a8d09ca3762af61e59520943dc26494f8941b"
NOT_LEAKED = "bc45408273d7e1914b741c3407b0b559764f7876"

def test_leaked_hash_is_found(client):
    response = client.post("/check", json={"hash": LEAKED})
    assert response.status_code == 200
    assert response.get_json() == {"found": True}

def test_unknown_hash_is_not_found(client):
    response = client.post("/check", json={"hash": NOT_LEAKED})
    assert response.status_code == 200
    assert response.get_json() == {"found": False}

def test_missing_hash_field(client):
    response = client.post("/check", json={})
    assert response.status_code == 400
    assert "error" in response.get_json()

def test_plaintext_password_is_rejected(client):
    # API przyjmuje tylko skrót - hasło w postaci jawnej musi zostać odrzucone
    response = client.post("/check", json={"hash": "123456"})
    assert response.status_code == 400

def test_uppercase_hash_is_found(client):
    # app.py robi .lower() na skrocie, wiec WIELKIE litery tez sa wykrywane
    response = client.post("/check", json={"hash": LEAKED.upper()})
    assert response.status_code == 200
    assert response.get_json() == {"found": True}


def test_too_short_hash_is_rejected(client):
    # SHA-1 ma 40 znakow; 39 to za malo
    response = client.post("/check", json={"hash": "a" * 39})
    assert response.status_code == 400


def test_non_hex_hash_is_rejected(client):
    # "g" nie jest cyfra szesnastkowa, mimo ze dlugosc (40) sie zgadza
    response = client.post("/check", json={"hash": "g" * 40})
    assert response.status_code == 400