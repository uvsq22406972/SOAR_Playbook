# Rapport SOC: {'type_alerte': 'Suspicion de phishing', 'ip_source': '203.0.113.10', 'asset': 'mail-gw-01', 'user_cible': 'john.doe', 'timestamp': '2026-01-03T09:10:00Z', 'severite': 'high', 'ip_is_private': True, 'is_critical_asset': False, 'tags': ['source interne']}

- **Généré**: 2026-01-28 23:07:31Z
- **Timestamp (alerte)**: 2026-01-03T09:10:00Z
- **Sévérité (initiale)**: high
- **Score**: **25/100**
- **Décision**: **Fermer l'alerte**

## Contexte de l'alerte
- **IP Source**: `203.0.113.10` (private=True)
- **Asset**: `mail-gw-01` (critical=False)
- **User**: `john.doe`
- **Tags**: `source interne`

## Raison du score
- Sévérité de l'alerte (high): +25

## Actions recommandées
- Vérifier les logs associés sur l'asset cible
- Corréler avec d'autres alertes récentes pour identifier des patterns
- Aucune menace détectée, fermer l'alerte après vérification

## Assistant IA
**Explication:** Cette alerte indique un événement de type 'Suspicion de phishing' impliquant l'IP source 203.0.113.10 sur l'asset 'mail-gw-01' et le compte 'john.doe'. Le score calculé (25/100) suggère un niveau de risque 'Fermer l'alerte'. Cette analyse est une assistance et doit être validée par un analyste SOC.

**Recommandations:**
- Valider l'alerte via corrélation (même IP, même user, même asset) sur la fenêtre temporelle.
- Rechercher des signes de succès d'authentification, pas uniquement des échecs.
- Si l'asset est critique, prioriser l'investigation et documenter une timeline.
- Envisager une action de containment (blocage IP temporaire) après validation.
- Escalader si suspicion d'accès réussi ou d'activité post-compromission.

**Disclaimer:** IA est une assistance. La décision finale appartient à l'analyste SOC.
