from datetime import datetime
from pathlib import Path

def _md_escape(text):
    return str(text).replace("\n", " ").strip()

def genere_rapport_md(alerte, score, score_raisons, decision, actions, ia, path_output):
    """
    Génère un rapport SOC en Markdown.
    """
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ")
    out = Path(path_output)
    out.parent.mkdir(parents=True, exist_ok=True)

    lignes = []
    lignes.append(f"# Rapport SOC: {_md_escape(alerte.get('type_alerte', ''))}")
    lignes.append("")
    lignes.append(f"- **Généré**: {now}")
    lignes.append(f"- **Timestamp (alerte)**: {_md_escape(alerte.get('timestamp', ''))}")
    lignes.append(f"- **Sévérité (initiale)**: {_md_escape(alerte.get('severite', ''))}")
    lignes.append(f"- **Score**: **{score}/100**")
    lignes.append(f"- **Décision**: **{decision}**")
    lignes.append("")

    lignes.append("## Contexte de l'alerte")
    lignes.append(f"- **IP Source**: `{_md_escape(alerte.get('ip_source', ''))}` (private={alerte.get('ip_is_private')})")
    lignes.append(f"- **Asset**: `{_md_escape(alerte.get('asset', ''))}` (critical={alerte.get('is_critical_asset')})")
    lignes.append(f"- **User**: `{_md_escape(alerte.get('user_cible', ''))}`")
    lignes.append(f"- **Tags**: `{', '.join(alerte.get('tags', []))}`")
    lignes.append("")

    lignes.append("## Raison du score")
    for r in score_raisons:
        lignes.append(f"- { _md_escape(r) }")
    lignes.append("")

    lignes.append("## Actions recommandées")
    for a in actions:
        lignes.append(f"- { _md_escape(a) }")
    lignes.append("")

    lignes.append("## Assistant IA")
    lignes.append(f"**Explication:** { _md_escape(ia.get('ia_explication', '')) }")
    lignes.append("")
    lignes.append("**Recommandations:**")
    for rec in ia.get("ia_recommandations", []):
        lignes.append(f"- { _md_escape(rec) }")
    lignes.append("")
    lignes.append(f"**Disclaimer:** { _md_escape(ia.get('ia_disclaimer', '')) }")
    lignes.append("")
    out.write_text("\n".join(lignes), encoding="utf-8")
