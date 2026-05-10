import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Mechanical Toolset", layout="centered")

# --- Header & User Info ---
st.title("MECHANICAL UNIT CONVERTER & MATERIAL DENSITY CHECKER")
st.markdown(f"""
### Developer Information
*   **Name:** SAJJAD AHMED
*   **Roll No:** 25-ME-76
---
""")

# --- Sidebar Navigation ---
option = st.sidebar.selectbox("Select a Tool", ["Unit Converter", "Material Density Checker"])

# --- Tool 1: Unit Converter ---
if option == "Unit Converter":
    st.header("⚙️ Mechanical Unit Converter")
    
    category = st.selectbox("Select Category", ["Length", "Force", "Pressure", "Energy"])
    
    col1, col2 = st.columns(2)
    
    if category == "Length":
        units = {"Meters (m)": 1.0, "Millimeters (mm)": 1000.0, "Inches (in)": 39.3701, "Feet (ft)": 3.28084}
    elif category == "Force":
        units = {"Newtons (N)": 1.0, "KiloNewtons (kN)": 0.001, "Pound-force (lbf)": 0.224809}
    elif category == "Pressure":
        units = {"Pascal (Pa)": 1.0, "Bar": 1e-5, "PSI (lb/in²)": 0.000145038, "MegaPascal (MPa)": 1e-6}
    elif category == "Energy":
        units = {"Joules (J)": 1.0, "KiloJoules (kJ)": 0.001, "Calories": 0.239006, "BTU": 0.000947817}

    with col1:
        input_val = st.number_input("Enter Value", value=1.0)
        from_unit = st.selectbox("From", list(units.keys()))
    
    with col2:
        to_unit = st.selectbox("To", list(units.keys()))
        # Conversion logic: (Value / Base_of_From) * Base_of_To
        result = (input_val / units[from_unit]) * units[to_unit]
        st.metric("Result", f"{result:.4f} {to_unit}")

# --- Tool 2: Material Density Checker ---
elif option == "Material Density Checker":
    st.header("🧪 Material Density Checker")
    
    # Density Data (kg/m^3)
    densities = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Brass": 8500,
        "Cast Iron": 7200,
        "Titanium": 4506,
        "Concrete": 2400,
        "Water": 1000,
        "Stainless Steel (304)": 8000
    }
    
    material = st.selectbox("Select Material", list(densities.keys()))
    density_val = densities[material]
    
    st.info(f"The density of **{material}** is approximately **{density_val} kg/m³**.")
    
    # Simple Mass Calculator
    st.subheader("Mass Calculator")
    volume = st.number_input("Enter Volume (m³)", min_value=0.0, value=1.0, step=0.1)
    mass = volume * density_val
    st.success(f"Estimated Mass: **{mass:,.2f} kg**")

# --- Footer ---
st.markdown("---")
st.caption("Developed for Mechanical Engineering Applications.")
