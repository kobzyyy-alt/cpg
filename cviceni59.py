import sys
import requests

if __name__ == "__main__":

    url = "https://jcu.cz/cz"

    responce = requests.get(url)
    if responce.status_code != 200:
        print(f"Pri stahovani url {url} doslo k chybe {responce.status_code}")
        sys.exit(1)
    print(responce.content)
    