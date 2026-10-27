import requests
def pobierz(url, klient=requests):
    response = klient.get(url, timeout=5)
    return response.json()
