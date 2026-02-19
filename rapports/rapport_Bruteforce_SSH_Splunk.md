# Rapport SOC: Bruteforce SSH

- **Généré**: 2026-02-19 13:10:14Z
- **Timestamp (alerte)**: 2026-02-19T13:10:14Z
- **Sévérité (initiale)**: low
- **Score**: **30/100**
- **Décision**: **Fermer l'alerte**

## Contexte de l'alerte
- **IP Source**: `` (private=False)
- **Asset**: `localhost:8088` (critical=False)
- **User**: ``
- **Tags**: `ip src invalide, source externe`

## Raison du score
- IP source publique (potentionellement externe): +25
- Sévérité de l'alerte (low): +5

## Actions recommandées
- Vérifier les logs associés sur l'asset cible
- Corréler avec d'autres alertes récentes pour identifier des patterns
- Chercher des 'Failed password' et 'Accepted password' dans /var/log/auth.log
- Vérifier si le compte ciblé a un comportement anormal
- Aucune menace détectée, fermer l'alerte après vérification

## Assistant IA
**Explication:** Cette alerte indique un événement de type 'Bruteforce SSH' impliquant l'IP source  sur l'asset 'localhost:8088' et le compte ''. Le score calculé (30/100) suggère un niveau de risque 'Fermer l'alerte'. Cette analyse est une assistance et doit être validée par un analyste SOC.

**Recommandations:**
- Valider l'alerte via corrélation (même IP, même user, même asset) sur la fenêtre temporelle.
- Rechercher des signes de succès d'authentification, pas uniquement des échecs.
- Si l'asset est critique, prioriser l'investigation et documenter une timeline.
- Vérifier /var/log/auth.log et l'historique SSH.
- Vérifier si le compte 'root/admin' est autorisé en SSH et appliquer hardening (MFA).

**Disclaimer:** IA est une assistance. La décision finale appartient à l'analyste SOC.
