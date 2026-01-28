from parsing import parse_alert
from enrichment import enrich_alerte
from score import scoring
from decision import decision_reponse
from assistant_ia import ia_explication_recommandation
from generer_rapport import genere_rapport_md
from pathlib import Path

FICHIERS_ALERTES = [
    "exemples/alerte_bruteforce.json",
    "exemples/alerte_phishing.json",
    "exemples/alerte_malware.json",
]

def main():
    for alert_path in FICHIERS_ALERTES:
        alerte = parse_alert(alert_path)
        alerte = enrich_alerte(alerte)

        score, raisons = scoring(alerte)
        decision, actions = decision_reponse(score, alerte)

        ia = ia_explication_recommandation(alerte, score, decision)

        #Générer le rapport Markdown
        path_output = f"rapports/rapport_{Path(alert_path).stem}.md"
        genere_rapport_md(alerte, score, raisons, decision, actions, ia, path_output)

        print(f"Rapport généré: {path_output}")

if __name__ == "__main__":
    main()
