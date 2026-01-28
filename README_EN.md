VERSION FRANÇAISE DISPONIBLE SUR README.md

# SOAR_Playbook
Automatise SOC Playbook with AI-assistance.

## Objective
The project demonstrate the use of an automatised playbook with an AI-assistance that is designed to assist alert analysis on triage and response to security alerts.

## Workflow
The workflow consists of creating a fictive alert with some fields that ressembles to a true SOC alert, then I parse the alert based on the fields, add a scoring that shows the alert priority for each alerts, decision making, and create a report. I also add some AI-assistance for each steps of the workflow in order to facilitate alert analysis.

## How to execute?
```bash
python3 src/playbook.py
```