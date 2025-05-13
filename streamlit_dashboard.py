import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from db_config import get_db_connection

# Page settings
st.set_page_config(page_title="Infra Monitoring Dashboard", layout="wide")
st.title("🏢 Adaptive Infrastructure Performance Monitoring")

# Load and cache data
conn = get_db_connection()

@st.cache_data(ttl=300)
def load_data():
    df = pd.read_sql("SELECT * FROM infra_data", conn)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df

df = load_data()
conn.close()

# Sidebar filters
with st.sidebar:
    st.header("🔎 Filter by:")
    selected_floors = st.multiselect("Floor", sorted(df["floor"].unique()), default=df["floor"].unique())
    selected_zones = st.multiselect("Zone", sorted(df["zone"].unique()), default=df["zone"].unique())

# Filter data
filtered_df = df[df["floor"].isin(selected_floors) & df["zone"].isin(selected_zones)]

# Aggregate numeric metrics
agg_df = (
    filtered_df.set_index("timestamp")
    .resample("6H")
    .agg({
        "cable_load_kw": "mean",
        "temperature_c": "mean",
        "occupancy": "mean"
    })
)

# KPI metrics
avg_cable = round(filtered_df["cable_load_kw"].mean(), 2)
max_cable = round(filtered_df["cable_load_kw"].max(), 2)
avg_temp = round(filtered_df["temperature_c"].mean(), 1)
avg_occ = round(filtered_df["occupancy"].mean(), 1)

st.markdown("### 📊 Key Metrics")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("⚡ Avg Cable Load", f"{avg_cable} kW")
kpi2.metric("⚠️ Peak Load", f"{max_cable} kW")
kpi3.metric("🌡️ Avg Temp", f"{avg_temp} °C")
kpi4.metric("👥 Avg Occupancy", f"{avg_occ}")

# Visualizations
st.markdown("---")
st.markdown("### 📈 Trends Over Time")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Cable Load (kW)")
    fig1, ax1 = plt.subplots()
    agg_df["cable_load_kw"].plot(ax=ax1, color="dodgerblue")
    ax1.set_ylabel("kW")
    ax1.grid(True)
    st.pyplot(fig1)

with col2:
    st.subheader("Occupancy")
    fig2, ax2 = plt.subplots()
    agg_df["occupancy"].plot(ax=ax2, color="darkgreen")
    ax2.set_ylabel("People")
    ax2.grid(True)
    st.pyplot(fig2)

st.markdown("---")
st.subheader("🚨 High Cable Load Alerts (> 4.5 kW)")
alert_df = filtered_df[filtered_df["cable_load_kw"] > 4.5]
if alert_df.empty:
    st.success("No high-load zones detected.")
else:
    st.warning(f"{len(alert_df)} alerts found.")
    st.dataframe(alert_df[["timestamp", "floor", "zone", "cable_load_kw"]])
