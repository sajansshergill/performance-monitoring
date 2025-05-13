# 🏢 Adaptive Infrastructure Performance Monitoring Dashboard

This project is an AI- and data-powered dashboard for monitoring performance metrics across adaptive building environments. It simulates and visualizes real-time data such as cable load, occupancy, and temperature — enabling early detection of bottlenecks or overloads in modular infrastructure setups.

> ✅ Built with: **Streamlit**, **PostgreSQL (Supabase)**, **Python**, **Pandas**, **Matplotlib**

---

## 📊 Live Demo (GIF)

![Dashboard Demo](assets/infra_dashboard_demo.gif)

---

## 🧩 Features

- Upload and simulate adaptive infrastructure data
- Store and manage data in a live **Supabase PostgreSQL** instance
- Monitor:
  - ⚡ Cable Load (kW)
  - 🌡️ Temperature (°C)
  - 👥 Occupancy
- Interactive filters by floor and zone
- Automated alerts for cable load > 4.5 kW
- KPI cards and time-based trend visualizations
- Easy deployment using Streamlit

---

## 🛠️ Tech Stack

| Layer        | Tech Used                     |
|--------------|-------------------------------|
| UI           | Streamlit                     |
| Backend DB   | Supabase PostgreSQL           |
| Processing   | Python, Pandas                |
| Visualization| Matplotlib, Streamlit Charts |
| Secrets      | `.env` + `python-dotenv`      |

---

## 📁 File Structure

infra_pipeline_project/
├── streamlit_dashboard.py # Streamlit dashboard
├── db_config.py # PostgreSQL connection logic
├── simulate_data.py # Sensor data generator
├── etl_pipeline.py # Upload to Supabase
├── .env # DB credentials (not committed)
├── requirements.txt # Python packages
├── README.md # This file
└── assets/
└── infra_dashboard_demo.gif


---

## 🌐 Supabase Setup

  1. Create a [Supabase](https://supabase.com) account and project
    2. Go to **SQL Editor → Run this:**

  ```sql
  CREATE TABLE infra_data (
      timestamp TIMESTAMP,
      building_id TEXT,
      floor INT,
      zone TEXT,
      cable_load_kw FLOAT,
      temperature_c FLOAT,
      occupancy INT
  );

  3. In Settings → Database, copy your credentials and paste into .env:

  DB_HOST=db.your-supabase.supabase.co
  DB_PORT=5432
  DB_NAME=postgres
  DB_USER=postgres
  DB_PASSWORD=your_password
