ENGLISH VERSION AVAILABLE AT README_EN.md  

# SOAR_Playbook  
Automatisation d’une alerte SOC avec un moteur d’automatisation intégrant un composant d’analyse basé sur l’IA

## Objectif  
Ce projet présente la mise en place d’un mini-SOC capable de détecter, analyser et documenter automatiquement des alertes de sécurité.
L’idée est de reproduire un flux simple mais réaliste de traitement d’incident, depuis l’arrivée d’un événement de sécurité jusqu’à la génération d’un rapport exploitable par un analyste SOC.

## Description du fonctionnement  
Le projet repose sur l’intégration de plusieurs éléments inspirés d’un environnement réel. Un événement de sécurité est d’abord envoyé dans Splunk via le mécanisme HTTP Event Collector (HEC). Une détection est ensuite réalisée en interrogeant régulièrement l’API REST de Splunk grâce à un script Python. Lorsqu’une alerte est trouvée, un webhook est déclenché vers un service local qui exécute le playbook SOAR. Ce playbook réalise le parsing de l’alerte, calcule un score de priorité, applique une logique de décision, puis génère automatiquement un rapport d’incident. Une assistance IA est utilisée pour faciliter l’analyse et améliorer la lisibilité du rapport produit.

Ainsi, le projet simule une chaîne complète de traitement :  
événement de sécurité -> SIEM (Splunk) -> détection -> webhook -> playbook SOAR -> rapport d’incident.

## Exécution  
Pour lancer le projet, il faut d’abord démarrer le serveur webhook :

```bash
python -m serveur.webhook
```

Ensuite, il faut démarrer le script de détection Splunk:
```bash
python caller_splunk.py
```
Une fois ces deux services actifs, l’injection d’un événement de test dans Splunk (Avec curl) déclenche automatiquement le traitement de l’alerte et la génération d’un rapport dans le dossier `rapports/`.
