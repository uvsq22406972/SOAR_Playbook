def ia_explication_recommandation(alerte, score, decision):
    """
    Simule un assistant IA: produit une explication et des recommandations.
    """
    type_alerte = str(alerte.get("type_alerte", "Unknown"))
    ip_source = str(alerte.get("ip_source", ""))
    asset = str(alerte.get("asset", ""))
    user_cible = str(alerte.get("user_cible", ""))
    severite = str(alerte.get("severite", "")).lower()

    explanation = (
        f"Cette alerte indique un événement de type '{type_alerte}' impliquant l'IP source {ip_source} "
        f"sur l'asset '{asset}' et le compte '{user_cible}'. "
        f"Le score calculé ({score}/100) suggère un niveau de risque '{decision}'. "
        "Cette analyse est une assistance et doit être validée par un analyste SOC."
    )

    recs = []
    # Recos générales
    recs.append("Valider l'alerte via corrélation (même IP, même user, même asset) sur la fenêtre temporelle.")
    recs.append("Rechercher des signes de succès d'authentification, pas uniquement des échecs.")
    recs.append("Si l'asset est critique, prioriser l'investigation et documenter une timeline.")

    # Recos selon contexte
    if severite in ("high", "critical") or score >= 70:
        recs.append("Envisager une action de containment (blocage IP temporaire) après validation.")
        recs.append("Escalader si suspicion d'accès réussi ou d'activité post-compromission.")

    # Recos spécifiques brute force
    if "ssh" in type_alerte.lower() or "bruteforce" in type_alerte.lower():
        recs.append("Vérifier /var/log/auth.log et l'historique SSH.")
        recs.append("Vérifier si le compte 'root/admin' est autorisé en SSH et appliquer hardening (MFA).")

    return {
        "ia_explication": explanation,
        "ia_recommandations": recs,
        "ia_disclaimer": "IA est une assistance. La décision finale appartient à l'analyste SOC."
    }
