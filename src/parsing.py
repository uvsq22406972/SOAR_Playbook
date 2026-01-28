import json

CHAMPS_REQUIS = ["type_alerte", "ip_source", "asset", "user_cible", "timestamp", "severite"]

def parse_alert(path_json_alerte):
    """
    Vérifier que tous les champs requis sont présents dans le fichier JSON de l'alerte.
    Il prend en argument le chemin du fichier JSON et renvoie un dictionnaire avec les données de l'alerte.
    """
    
    with open(path_json_alerte, 'r') as fichier:
        alerte = json.load(fichier)
        
    for champ in CHAMPS_REQUIS:
        if (champ not in alerte):
            raise ValueError(f"Il manque le champ requis: {champ}")
        
    return alerte
