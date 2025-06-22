# Inside Teen Minds: Global Mental Health Segmentation

This project analyzes global survey data on teen mental health, screen time, AI usage, and wellness habits. The goal was to identify at-risk student segments using a clean, modular Python workflow — all without Power BI, Tableau, or SQL.

---

## 🎯 Objective

**Identify Risk Profiles for Social Media Addiction and Emotional Strain Among Students**, using:
- Mood, stress, and behavioral data
- Sleep patterns
- Self-reported support and wellness habits
- AI usage indicators

---

## 🧰 Tools Used

- Python 3 (via Jupyter Notebook)
- `pandas` for data wrangling
- `seaborn` / `matplotlib` for visualization
- macOS Terminal for automation and file management

---

## 📁 Project Structure


---

## 📊 Key Insights

- **Stress is more widely spread** than mood — many teens report high stress levels even if their mood appears stable.
- **Sleep < 6 hours is a strong indicator** of high stress and low mood.
- **AI usage** shows no clear correlation with improved emotional states.
- **Support feeling ratings** are tied closely to emotional wellness — those who feel unsupported score higher in stress and lower in mood.

---

## 🔍 Segmentation Logic

Each student received a custom risk score based on:

- `+2` points for high stress  
- `+1` point for low mood (≤ 3)  
- `+1` point for sleeping less than 6 hours  
- `+1` point for feeling low support (≤ 2)

**Risk Levels:**

| Risk Score | Label        |
|------------|--------------|
| 4+         | High Risk    |
| 2–3        | Moderate     |
| 0–1        | Low Risk     |

Segmented results were exported to `data/cleaned/mental_health_segmented.csv`.

---

## 📁 Final Deliverables

- [✅ Notebook: `eda_overview.ipynb`](notebooks/eda_overview.ipynb)
- [✅ Final HTML Report](outputs/reports/eda_risk_report.html)
- [✅ Segmented CSV](data/cleaned/mental_health_segmented.csv)
- [✅ Charts as .jpgs](outputs/charts/)

---

## 🔗 Project Status

✅ Complete  
📤 Uploaded as part of a senior-level data analyst portfolio  
🔒 100% done using open-source Python + Jupyter — no Tableau, no SQL, no drag-and-drop GUIs


