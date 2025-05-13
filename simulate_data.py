import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_sensor_data(start_time, periods, freq="H"):
    timestamps = pd.date_range(start=start_time, periods=periods, freq=freq)
    data = []

    for time in timestamps:
        for floor in [1, 2, 3]:
            for zone in ["Z1", "Z2", "Z3"]:
                data.append({
                    "timestamp": time,
                    "building_id": "BLDG-A",
                    "floor": floor,
                    "zone": zone,
                    "cable_load_kw": round(np.random.uniform(0.5, 5.0), 2),
                    "temperature_c": round(np.random.normal(22, 1.5), 1),
                    "occupancy": np.random.randint(0, 15)
                })

    return pd.DataFrame(data)

if __name__ == "__main__":
    df = generate_sensor_data(datetime.now(), 72)
    df.to_csv("sensor_data.csv", index=False)
    print("✅ Sensor data written to sensor_data.csv")
