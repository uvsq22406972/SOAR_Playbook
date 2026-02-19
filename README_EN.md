# SOAR_Playbook  
Automation of a SOC alert using an automation engine integrating an AI-based analysis component

## Objective  
This project presents the implementation of a mini-SOC capable of automatically detecting, analyzing, and documenting security alerts.  
The goal is to reproduce a simple but realistic incident-handling workflow, from the arrival of a security event to the generation of a report usable by a SOC analyst.

## How it works  
The project relies on the integration of several components inspired by a real environment.  
A security event is first sent to Splunk through the HTTP Event Collector (HEC).  
Detection is then performed by regularly querying the Splunk REST API using a Python script.  
When an alert is found, a webhook is triggered to a local service that executes the SOAR playbook.  
This playbook parses the alert, computes a priority score, applies a decision logic, and automatically generates an incident report.  
An AI-based analysis component is included to help interpret the alert and improve the readability of the generated report.

This simulates a complete processing chain:  
security event -> SIEM (Splunk) -> detection -> webhook -> SOAR playbook -> incident report.

## Execution  

Start the webhook server:

```bash
python -m serveur.webhook
```

Then start the Splunk detection script:
```bash
python -m caller_splunk.py
```

Once both services are running, injecting a test event into Splunk (using curl) will automatically trigger alert processing and generate a report inside the `rapports/` directory.