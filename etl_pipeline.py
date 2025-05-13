import pandas as pd
from db_config import get_db_connection

def load_data_to_postgres(csv_path):
    df = pd.read_csv(csv_path)
    conn = get_db_connection()
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO infra_data (timestamp, building_id, floor, zone, cable_load_kw, temperature_c, occupancy)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, tuple(row))
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Data loaded to Supabase DB.")

if __name__ == "__main__":
    load_data_to_postgres("sensor_data.csv")
