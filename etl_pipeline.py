import pandas as pd
from db_config import get_db_connection

def load_data_to_postgres(csv_path):
    df = pd.read_csv(csv_path)
    conn = get_db_connection()
    cur = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS infra_data (
        timestamp TIMESTAMP,
        building_id TEXT,
        floor INT,
        zone TEXT,
        cable_load_kw FLOAT,
        temperature_c FLOAT,
        occupancy INT
    );
    """
    cur.execute(create_table_query)
    conn.commit()

    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO infra_data (timestamp, building_id, floor, zone, cable_load_kw, temperature_c, occupancy)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, tuple(row))
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Data loaded into PostgreSQL")

if __name__ == "__main__":
    load_data_to_postgres("sensor_data.csv")
