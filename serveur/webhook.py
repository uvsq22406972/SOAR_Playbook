from flask import Flask, request, jsonify
from datetime import datetime
from pathlib import Path

from src.enrichment import enrich_alerte
from src.score import scoring
from src.decision import decision_reponse
from src.assistant_ia import ia_explication_recommandation
from src.generer_rapport import genere_rapport_md

app = Flask(__name__)

def normalize_from_splunk(payload: dict) -> dict:
    """
    Payload attendu (simple) côté Splunk: on envoie direct un event déjà 'presque' au bon format.
    """
    evt = payload.get("event", payload)

    return {
        "type_alerte": evt.get("type_alerte", evt.get("alert_type", "Unknown")),
        "ip_source": evt.get("ip_source", evt.get("src_ip", "")),
        "asset": evt.get("asset", evt.get("host", "unknown")),
        "user_cible": evt.get("user_cible", evt.get("user", "")),
        "timestamp": evt.get("timestamp", datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")),
        "severite": evt.get("severite", evt.get("severity", "low")),
    }

@app.post("/splunk")
def splunk_webhook():
    payload = request.get_json(force=True, silent=False) or {}
    alerte = normalize_from_splunk(payload)

    alerte = enrich_alerte(alerte)
    score, raisons = scoring(alerte)
    decision, actions = decision_reponse(score, alerte)
    ia = ia_explication_recommandation(alerte, score, decision)

    out = Path("rapports") / f"rapport_{alerte['type_alerte'].replace(' ','_')}_{alerte['timestamp'].replace(':','').replace('-','')}.md"
    genere_rapport_md(alerte, score, raisons, decision, actions, ia, str(out))

    return jsonify({"status": "ok", "rapport": str(out), "decision": decision, "score": score})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
