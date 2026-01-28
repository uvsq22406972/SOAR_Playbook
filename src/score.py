def scoring(alerte):
    """
    Calculer un score de risque pour l'alerte en fonction de ses attributs enrichis.
    """
    
    score = 0
    raisons = []
    
    #Score basé sur l'adresse IP
    ip_is_private = bool(alerte.get("ip_is_private", False))
    if not ip_is_private:
        score += 25
        raisons.append("IP source publique (potentionellement externe): +25")
    
    #Score basé sur l'asset critique
    is_critical_asset = bool(alerte.get("is_critical_asset", False))
    if is_critical_asset:
        score += 30
        raisons.append("Cible critique: +30")
        
    #Score basé sur l'utilisateur cible
    user_cible = alerte.get("user_cible", "").lower()
    if user_cible in ["root", "admin", "administrator"]:
        score += 20
        raisons.append(f"Utilisateur cible privilégié ({user_cible}): +20")
    
    #Score basé sur la sévérité
    severite = alerte.get("severite", "low").lower()
    severite_map = {
        "low": 5,
        "medium": 15,
        "high": 25,
        "critical": 35
    }
    severite_score = severite_map.get(severite, 10)
    score += severite_score
    raisons.append(f"Sévérité de l'alerte ({severite}): +{severite_score}")
    
    if score > 100:
        score = 100
    
    return score, raisons
    
    