import streamlit as st
import pandas as pd

# 1. Page Config
st.set_page_config(page_title="Stima-Safi", page_icon="⚡")

# 2. Styling (The "Vibe")
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #fffd01; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ Stima-Safi: Comrade Energy")

# 3. Mode Selection
mode = st.radio("Select Living Mode:", ["Off-Campus (Tokens)", "On-Campus (Hostel Safety)"])

# 4. Sidebar Inputs
st.sidebar.header("Appliance List")
appliances = {
    "LED Bulb (9W)": 9,
    "Laptop (65W)": 65,
    "Subwoofer (100W)": 100,
    "Iron Box (1000W)": 1000,
    "Electric Coil (1500W)": 1500,
    "Electric Kettle (2000W)": 2000
}

selected_apps = []
for app, watts in appliances.items():
    if st.sidebar.checkbox(app):
        selected_apps.append({"Device": app, "Watts": watts})

# 5. Calculations
total_watts = sum([item["Watts"] for item in selected_apps])

if mode == "Off-Campus (Tokens)":
    units = st.number_input("Enter KPLC Units (Tokens):", min_value=0.0, value=5.0)
    if total_watts > 0:
        hours = (units * 1000) / total_watts
        st.metric("Time Remaining", f"{round(hours, 1)} Hours")
        if hours < 5:
            st.error("🚨 Low Energy! Switch to Survival Mode.")
    else:
        st.info("Select appliances to calculate time.")

else:
    st.subheader("Hostel Safety Monitor")
    if total_watts > 800:
        st.error("🚨 Overload Risk: High-wattage detected!")
    elif total_watts > 0:
        st.success("✅ Safe usage for hostel wiring.")
    else:
        st.write("Monitoring...")

# 6. Visuals
if selected_apps:
    df = pd.DataFrame(selected_apps)
    st.bar_chart(df.set_index("Device"))

st.caption("🔄 Status: Simulation Mode (Awaiting IoT Sensor Link)")
