AI-Powered UEBA System for Insider Threat Detection
Overview

This project implements an AI-based User and Entity Behavior Analytics (UEBA) system for detecting anomalous user behavior and potential insider threats.

The system analyzes user activity logs using Machine Learning and assigns risk scores to prioritize security investigations, simulating real-world Security Operations Center (SOC) workflows.

Architecture
User Activity Logs
        ↓
Data Preprocessing
        ↓
Isolation Forest (Anomaly Detection)
        ↓
Risk Scoring Engine
        ↓
Risk Level Classification

Dataset Features

user_id

login_time_hour

login_location_risk

failed_logins

files_accessed

data_download_mb

usb_usage

anomaly_label

The dataset contains approximately 10% anomalous behavior, reflecting realistic cybersecurity scenarios.

Technologies Used

Python

Pandas

Scikit-learn

NumPy

Matplotlib

Model

The project uses Isolation Forest, an unsupervised anomaly detection algorithm that identifies abnormal behavioral patterns without requiring labeled attack data.

Use Cases

Insider threat detection

Compromised account identification

Behavioral anomaly detection

SOC alert prioritization

Collaboration

Mohammed Isaq — AI & ML Engineer

ML model development

Anomaly detection pipeline

Risk scoring implementation

Ayub Ahmed — SOC Analyst

Security workflow design

UEBA behavioral validation

Risk prioritization logic

License

This project is licensed under the MIT License.
