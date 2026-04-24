# Adaptive ML System for Detecting & Disrupting Stealthy Data Attacks

## Overview

This project builds a cybersecurity system that goes beyond simple monitoring — it understands network behavior and reacts to threats.

Using Machine Learning (Isolation Forest), the system learns normal traffic patterns, detects anomalies, and actively disrupts suspicious activity through traffic manipulation.

**In simple terms:**

* Detect suspicious activity
* Disrupt it before damage happens

---

## Problem

Modern cyber attacks are increasingly stealthy.

Instead of sending large amounts of data, attackers slowly leak small pieces over time (data exfiltration), making detection difficult for traditional systems.

**Limitations of traditional systems:**

* Rely on predefined rules
* Fail to detect slow and subtle attacks

---

## Solution

This system addresses the problem by:

* Learning what normal network behavior looks like
* Identifying even minor deviations
* Actively interfering with suspicious traffic

This is not just a detection system — it is an active defense mechanism.

---

## Key Features

* Machine Learning-based anomaly detection (Isolation Forest)
* Real-time traffic analysis pipeline
* Behavior-based detection instead of signature-based
* Active camouflage defense mechanism
* Fake traffic injection and delay strategies

---

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Unsupervised Machine Learning

---

## Dataset

* CICIDS 2017 Network Traffic Dataset
* Real-world cybersecurity dataset
* Includes both normal and attack traffic

---

## System Workflow

1. Collect network data
2. Preprocess the data
3. Perform feature engineering
4. Train the model (Isolation Forest)
5. Monitor traffic in real time
6. Trigger defense actions when anomalies are detected

---

## How to Run

```bash
pip install -r requirements.txt
python src/train_model.py
python main.py
```

---

## Summary

Most systems only detect threats.
This system detects and actively responds to them.
