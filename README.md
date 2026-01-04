# Weekend Getaway Ranker

A Python-based recommendation engine that ranks the top weekend travel destinations
in India based on tourist ratings, popularity, and visit-time efficiency.

This project is part of a Data Engineering technical assessment.

---

## 📌 Project Overview
The system takes a **Source City** as input and recommends the best weekend getaway
destinations using:
- Average Google review ratings
- Popularity (number of reviews)
- Time efficiency (suitable for short trips)

Since the dataset does not contain explicit distance information, visit-time efficiency
is used as a proxy for weekend feasibility.

---

## 🛠️ Technologies Used
- Python 3.x
- Pandas

---

## 📂 Repository Structure
Weekend-Getaway-Ranker/
│── weekend_getaway_ranker.py
│── travel_data.csv
│── requirements.txt
│── sample_output.txt
│── README.md