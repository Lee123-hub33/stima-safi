# ⚡ Stima-Safi (Power-Pesa)
### *The Comrade's Energy Orchestrator*

A dual-mode energy management tool designed for Kenyan university students to bridge the gap between on-campus hostel safety and off-campus utility budgeting.

---

## 🚀 The Problem
University students in Kenya face a unique "Energy Gap":
* **Off-Campus:** High KPLC tariffs (approx. 28.45 KES/unit) lead to "blackout anxiety" where students run out of tokens mid-study.
* **On-Campus:** "Free" electricity leads to the use of high-wattage appliances (Electric Coils/Kettles), causing fire hazards and overloading old hostel wiring.

## 🛠️ The Solution
**Stima-Safi** acts as a Decision-Support System (DSS) with two specialized modules:

1. **Token Survival Mode (Off-Campus):** Converts remaining KPLC units into "Hours of Power" based on active appliances.
2. **Safety Monitor (On-Campus):** Flags high-wattage devices that exceed the 800W hostel safety threshold to prevent electrical fires.

## 🧰 Tech Stack
* **Language:** Python 3.x
* **Framework:** Streamlit (Web UI)
* **Data Handling:** Pandas (Appliance profiling)
* **Environment:** GitHub Codespaces / Docker-ready

## 📈 Future Roadmap (Phase 2)
As a Data Engineering project, the next steps involve:
* **IoT Integration:** Connecting via API to smart plugs (Sonoff/Tuya) for real-time wattage ingestion.
* **Predictive Analytics:** Using historical usage data to predict exactly when tokens will run out.
* **University Dashboard:** A central hub for hostel managers to monitor energy "hotspots" for maintenance.

---
*Developed during the 2026 Campus Hackathon.*