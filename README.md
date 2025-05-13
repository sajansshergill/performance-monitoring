# Data Pipeline for Adaptive Infrastructure Performance Monitoring

## 📌 Summary
Simulate real-time infrastructure sensor data (e.g., power usage, cable load, occupancy) for adaptive high-performance buildings. Build a data pipeline that ingests, cleans, stores, and visualizes this data to monitor trends and alert for threshold breaches. This showcases your ability to work with structured data flows and real-time business systems—exactly what FreeAxez’s modular environments enable.

## 🧱 Project Objectives
- Simulate adaptive infrastructure data from building zones

- Design and run a Python ETL pipeline

- Store data in a PostgreSQL database

- Visualize cable usage, occupancy, or power metrics

- Showcase operational insights via a dashboard

## 🗂️ File & Code Structure

infra_pipeline_project/
├── simulate_data.py            # Generate synthetic sensor data
├── etl_pipeline.py             # ETL: Extract → Transform → Load into DB
├── dashboard.ipynb             # Visualize trends with matplotlib/seaborn
├── db_config.py                # PostgreSQL credentials & connection setup
├── requirements.txt
└── README.md

## 📊 Simulated Infrastructure Data (Sample Schema)
| timestamp           | building\_id | floor | zone | cable\_load\_kw | temperature\_c | occupancy |
| ------------------- | ------------ | ----- | ---- | --------------- | -------------- | --------- |
| 2025-05-13 10:00:00 | BLDG-A       | 2     | Z1   | 2.4             | 21.5           | 5         |
| 2025-05-13 10:00:00 | BLDG-A       | 2     | Z2   | 3.1             | 23.0           | 8         |


## 🧠 Key Learnings
- Designed end-to-end ETL for synthetic infrastructure data

- Simulated real-world energy & cable metrics for smart buildings

- Created insights and alert logic for over-utilization of adaptive zones

- Showcased how infrastructure-aware AI/data systems help businesses like FreeAxez
