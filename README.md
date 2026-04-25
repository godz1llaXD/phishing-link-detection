# Phishing Link Detection using Machine Learning

## Overview

This project presents a **machine learning-based system for detecting phishing URLs** using only **lexical and structural characteristics of URLs**.  

Unlike heavy, network-dependent solutions, this approach is:
- **Offline-capable**
- **Fast and lightweight**
- **Explainable**
- **Practical for real-world deployment**

The system was developed as part of a major academic project and follows a **complete end-to-end ML pipeline**, culminating in a deployed web application.

---

## Objectives

- Build a reliable phishing URL detection model  
- Engineer meaningful, security-relevant features from URLs  
- Compare traditional ML models and select an optimal one  
- Ensure interpretability of predictions  
- Deploy a working interface for real-time usage  

---

## Methodology

### Project Workflow

1.Dataset Collection
2.Dataset Consolidation & Labeling
3.Exploratory Data Analysis (EDA)
4.Feature Engineering (URL-based)
5.Feature Selection
6.Model Training (Traditional ML)
7.Model Evaluation
8.Explainability & Analysis
9.Final Model Selection
10.Deployment / Demo


---

## Dataset

### Phishing URLs
- **Source:** PhishTank  
- **Snapshot:** 29th Dec, ~11:30 PM  
- **Filtering:** Only *verified and active* phishing URLs  
- **Size Used:** ~45,000  

---

### Legitimate URLs
- **Source:** Tranco Top Domains  
- **Snapshot:** 29th Dec, ~11:30 PM  
- **List ID:** `3Q88L`  
- **Processing:** Domains converted to URLs and randomly sampled  
- **Size Used:** ~45,000  

---

### Dataset Strategy

To avoid class imbalance:

- Equal sampling of phishing and legitimate URLs  
- Duplicate removal and normalization  
- Final dataset size: **~90,000 URLs (balanced)**  

---

## Exploratory Data Analysis (EDA)

EDA revealed clear behavioral differences:

- Phishing URLs tend to be **longer**
- Higher **digit and special character usage**
- Greater **subdomain depth**
- Increased **entropy (randomness)**

These insights directly informed feature engineering.

---

## Feature Engineering

Features were extracted using deterministic parsing.

### Key Feature Groups

**Lexical Features**
- URL length  
- Digit count  
- Special character count  
- Dot and hyphen count  
- Presence of `@`  
- HTTPS usage  
- Entropy  

**Structural Features**
- Domain length  
- Path length  
- Query length  
- Subdomain depth  

**Security Indicators**
- IP address in URL  
- Fragment presence  
- Query parameter count  

All features are:
- Lightweight  
- Interpretable  
- Aligned with real phishing behavior  

---

## Models Evaluated

- Logistic Regression (baseline)  
- Random Forest (primary model)  
- Gradient Boosting  
- Support Vector Machine (SVM)  

---

## Evaluation Metrics

- Precision  
- Recall (**priority for phishing detection**)  
- F1-score  
- ROC-AUC  
- Confusion Matrix  

 **Security consideration:**  
Minimizing **false negatives** (missed phishing URLs) is critical.

---

## Final Model

### Random Forest Classifier

**Reason for selection:**
- High phishing recall  
- Robust performance on structured data  
- Strong interpretability  
- Balanced precision vs recall  

---

## Explainability

Model decisions were analyzed using:
- Feature importance  
- (Optional) SHAP analysis  

Top contributing factors:
- URL length  
- Entropy  
- Subdomain depth  
- Dot count  
- Digit count  

These align with known phishing tactics such as:
- URL obfuscation  
- Subdomain abuse  
- Automated link generation  

---

## Deployment

A lightweight frontend was built using **Streamlit**, enabling:

- Real-time URL analysis  
- Confidence scoring  
- Human-readable explanations  

---

## Limitations

- No webpage content analysis  
- No WHOIS/DNS features (kept offline for speed)  
- May struggle with highly sophisticated or zero-day phishing  

---

## Future Scope

- Integrate domain-age and WHOIS features  
- Browser extension for real-time detection  
- API-based deployment  
- Adversarial robustness (e.g., homoglyph attacks)  
- Hybrid URL + HTML analysis  

---

## Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Streamlit  
- Matplotlib / Seaborn  
- SHAP (optional)  

---

## Conclusion

This project demonstrates that **traditional machine learning**, combined with carefully engineered features, can effectively detect phishing URLs while remaining **fast, interpretable, and deployable**.

It reflects a **practical, industry-aligned approach** to solving a real cybersecurity problem.

---

## Portfolio Value

This project showcases:
- End-to-end ML pipeline design  
- Cybersecurity domain understanding  
- Feature engineering expertise  
- Model evaluation and selection  
- Deployment of ML systems  
