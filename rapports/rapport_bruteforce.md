# Rapport SOC: {'type_alerte': 'Bruteforce SSH', 'ip_source': '50.7.14.253', 'asset': 'srv-prod-01', 'user_cible': 'root', 'timestamp': '2026-01-20T16:48:00Z', 'severite': 'medium', 'ip_is_private': False, 'is_critical_asset': True, 'tags': ['cible critique', 'source externe']}

- **Généré**: 2026-01-28 22:55:52Z
- **Timestamp (alerte)**: 2026-01-20T16:48:00Z
- **Sévérité (initiale)**: medium
- **Score**: **90/100**
- **Décision**: **Escalader à l'équipe SOC N2**

## Contexte de l'alerte
- **IP Source**: `50.7.14.253` (private=False)
- **Asset**: `srv-prod-01` (critical=True)
- **User**: `root`
- **Tags**: `cible critique, source externe`

## Raison du score
- IP source publique (potentionellement externe): +25
- Cible critique: +30
- Utilisateur cible privilégié (root): +20
- Sévérité de l'alerte (medium): +15

## Actions recommandées
- Vérifier les logs associés sur l'asset cible
- Corréler avec d'autres alertes récentes pour identifier des patterns
- Chercher des 'Failed password' et 'Accepted password' dans /var/log/auth.log
- Vérifier si le compte ciblé a un comportement anormal
- Notifier immédiatement les responsables de la sécurité
- Proposer d'isoler l'asset cible du réseau pour éviter toute propagation
- Vérifier les accès récents et les modifications système sur l'asset cible

## Assistant IA
**Explication:** Cette alerte indique un événement de type 'Bruteforce SSH' impliquant l'IP source 50.7.14.253 sur l'asset 'srv-prod-01' et le compte 'root'. Le score calculé (90/100) suggère un niveau de risque 'Escalader à l'équipe SOC N2'. Cette analyse est une assistance et doit être validée par un analyste SOC.

**Recommandations:**
- Valider l'alerte via corrélation (même IP, même user, même asset) sur la fenêtre temporelle.
- Rechercher des signes de succès d'authentification, pas uniquement des échecs.
- Si l'asset est critique, prioriser l'investigation et documenter une timeline.
- Envisager une action de containment (blocage IP temporaire) après validation.
- Escalader si suspicion d'accès réussi ou d'activité post-compromission.
- Vérifier /var/log/auth.log et l'historique SSH.
- Vérifier si le compte 'root/admin' est autorisé en SSH et appliquer hardening (MFA).

**Disclaimer:** IA est une assistance. La décision finale appartient à l'analyste SOC.
