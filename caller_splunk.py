import time
import requests
import urllib3
import os

from dotenv import load_dotenv
load_dotenv()


urllib3.disable_warnings()

SPLUNK_HOST = "https://localhost:8089"
USERNAME = os.getenv("SPLUNK_USER")
PASSWORD = os.getenv("SPLUNK_PASSWORD")

SEARCH_QUERY = 'search index=main sourcetype="soc:alert" type_alerte="Bruteforce SSH" | head 1'

WEBHOOK_URL = "http://127.0.0.1:5001/splunk"


def run_search():
    """Lance une recherche Splunk via API REST"""
    url = f"{SPLUNK_HOST}/services/search/jobs"

    data = {
        "search": SEARCH_QUERY,
        "output_mode": "json"
    }

    response = requests.post(
        url,
        data=data,
        auth=(USERNAME, PASSWORD),
        verify=False
    )

    if response.status_code != 201:
        print("Erreur création job:", response.text)
        return None

    sid = response.json()["sid"]
    return sid


def get_results(sid):
    """Récupère les résultats d'un job Splunk"""
    url = f"{SPLUNK_HOST}/services/search/jobs/{sid}/results"

    params = {"output_mode": "json"}

    response = requests.get(
        url,
        params=params,
        auth=(USERNAME, PASSWORD),
        verify=False
    )

    if response.status_code != 200:
        print("Erreur récupération résultats: ", response.text)
        return []

    return response.json().get("results", [])



def call_webhook(event):
    """Envoie l'événement vers le webhook SOAR"""
    try:
        r = requests.post(WEBHOOK_URL, json={"event": event})
        print("Webhook envoyé: ", r.status_code)
    except Exception as e:
        print("Erreur webhook: ", e)


def main():
    visite = set()

    while True:
        sid = run_search()

        if sid:
            time.sleep(2)
            results = get_results(sid)

            for event in results:
                key = str(event)

                if key not in visite:
                    print("Incident détecté: ", event)
                    call_webhook(event)
                    visite.add(key)

        time.sleep(30)


if __name__ == "__main__":
    main()