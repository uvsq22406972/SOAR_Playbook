import ipaddress

def enrich_alerte(alerte):
    """
    Enrichir les données de l'alerte en ajoutant des informations supplémentaires.
    - IP publique ou privée (ip_is_private)
    - source cible critique ou pas (is_critical_asset)
    - tags associés (tags)
    """
    
    enriched = alerte.copy()
    
    #Verifier si l'IP est privée ou publique
    ip_src = enriched.get("ip_source")
    try:
        ip_obj = ipaddress.ip_address(ip_src)
        enriched["ip_is_private"] = ip_obj.is_private
    except ValueError:
        enriched["ip_is_private"] = False
        enriched.setdefault("tags", [])
        enriched["tags"].append("ip src invalide")
    
    #Vérifier si l'asset est critique
    asset = enriched.get("asset", "").lower()
    if "prod" in asset or asset.startswith("srv-prod"):
        enriched["is_critical_asset"] = True
    else:
        enriched["is_critical_asset"] = False
    
    #Ajouter des tags
    tags = enriched.get("tags", [])
    if enriched["ip_is_private"] is False:
        tags.append("source externe")
    else:
        tags.append("source interne")
        
    if enriched["is_critical_asset"]:
        tags.append("cible critique")
    
    enriched["tags"] = sorted(set(tags))
    return enriched
    