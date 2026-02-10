# Ocular-Surface-Analysis-Tool
Python tools for image preprocessing and quality assessment in dry eye disease research

# Automated Meibomian Gland Atrophy Quantification (MGD-Quant)

## 📌 Project Overview
This repository contains a Python-based pipeline for the automated segmentation and quantification of Meibomian Gland Dysfunction (MGD). 
The tool calculates the atrophy ratio by comparing the eyelid area with the functional gland area, following the **Keio University (Japan) Meiboscore standards**.

## 🚀 Key Features
* **Automated Batch Processing:** Processes large datasets (e.g., MGD1-k) in seconds.
* **Precise Quantification:** Uses morphological operations and pixel-counting to calculate atrophy percentages.
* **Clinical Grading:** Automatically classifies results into Meiboscores (Grade 0 to 3).
* **Data Visualization:** Generates statistical distributions of atrophy across patient populations.

## 🛠️ Technical Stack
* **Language:** Python 3.x
* **Libraries:** OpenCV (Image Processing), Pandas (Data Management), Matplotlib (Visualization).

## 📊 Results & Performance
The algorithm was tested on the MGD1-k dataset (1000+ images). Below is the distribution of atrophy grades obtained during our latest run:

![Atrophy Distribution](atrophy_distribution.png) 
*(Note: Upload your 'my_research_results.png' image to GitHub and rename it as shown here to see it appear)*

## 🔬 Scientific Context
This work aims to reduce inter-observer variability in MGD diagnosis. By automating the **Meiboscore** system, we provide clinicians with an objective metric to track disease progression.

---
**Contact:** *Severin Didjeu Nkengne* *PhD Researcher - University of Yaoundé 1*
