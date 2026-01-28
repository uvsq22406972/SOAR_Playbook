def decision_reponse(score,alert):
    """
    Prendre une décision de réponse en fonction du score de risque de l'alerte.
    - Score entre 0 et 30 : Fermer l'alerte si aucune indication de menace n'est présente.
    - Score entre 31 et 70 : Transférer à l'équipe SOC N1 pour une analyse plus approfondie.
    - Score entre 71 et 100 : Escalader immédiatement à l'équipe SOC N2 et notifier les responsables.
    """
    
    actions = []
    type_alerte = alert.get("type_alerte", "").lower()
    
    actions.append("Vérifier les logs associés sur l'asset cible")
    actions.append("Corréler avec d'autres alertes récentes pour identifier des patterns")
    
    if "ssh" in type_alerte or "bruteforce" in type_alerte:
        actions.append("Chercher des 'Failed password' et 'Accepted password' dans /var/log/auth.log")
        actions.append("Vérifier si le compte ciblé a un comportement anormal")
    
    #Décision basée sur le score
    if score <= 30:
        decision = "Fermer l'alerte"
        actions.append("Aucune menace détectée, fermer l'alerte après vérification")
    
    elif 31 <= score <= 70:
        decision = "Transférer à l'équipe SOC N1"
        actions.append("Ouvrir une enquête approfondie par l'équipe SOC N1")
        actions.append("Si l'IP source est publique, envisager de bloquer l'IP temporairement")
    
    else:
        decision = "Escalader à l'équipe SOC N2"
        actions.append("Notifier immédiatement les responsables de la sécurité")
        actions.append("Proposer d'isoler l'asset cible du réseau pour éviter toute propagation")
        actions.append("Vérifier les accès récents et les modifications système sur l'asset cible")
    
    return decision, actions
        
        