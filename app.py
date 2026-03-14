import streamlit as st
import pandas as pd
import numpy as np
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="EduManager Pro | Excellence Edition", page_icon="🚀", layout="wide")

# --- CHIC CUSTOM STYLING (EPFL INSPIRED) ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background-color: #FF0000;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover { background-color: #cc0000; color: white; }
    div[data-testid="stMetricValue"] { font-size: 28px; color: #FF0000; }
    .sidebar .sidebar-content { background-image: linear-gradient(#2e7bcf,#2e7bcf); color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("logo-epfl.png", width=150)
    st.title("Control Center")
    page = st.radio("Navigate Modules", 
                    ["Executive Dashboard", 
                     "Coach-Student Matcher", 
                     "Event ROI Predictor", 
                     "Weekend Ski Logistics"])
    st.divider()
    st.caption("Dominic Thomson | SCIPER 381176")
    

# ==========================================
# MODULE 1: EXECUTIVE DASHBOARD
# ==========================================
if page == "Executive Dashboard":
    st.title("🚀 EduManager Pro")
    st.markdown("### *Data-Driven Leadership for the EPFL Community*")
    
    st.write("---")
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Cohort", "800 Students", "Active")
    c2.metric("Staff Force", "35 Coaches", "Supercoach Program")
    c3.metric("Annual Budget", "3,000 CHF", "Targeted Allocation")

    st.write("---")
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.subheader("Strategic Fund Management")
        budget = st.slider("Simulate Total Budget (CHF)", 1000, 10000, 3000)
        priority = st.select_slider("Organizational Goal", options=["Academic Excellence", "Balanced", "Social Cohesion"])
        
        fixed = 500
        rem = budget - fixed
        weights = {"Academic Excellence": [0.7, 0.3], "Balanced": [0.5, 0.5], "Social Cohesion": [0.3, 0.7]}
        
        st.write(f"**Current Priority:** {priority}")
        st.progress(weights[priority][0])
        st.caption(f"Strategy: {int(weights[priority][0]*100)}% Academic / {int(weights[priority][1]*100)}% Social")

    with col_b:
        st.info("#### Mission Statement\nTo transform the Supercoach experience into a scalable infrastructure, ensuring that social and academic integration is guided by operational excellence.")

# ==========================================
# MODULE 2: COACH-STUDENT MATCHER
# ==========================================
elif page == "Coach-Student Matcher":
    st.title("🤝 Precision Student Partitioning")
    st.write("Equal distribution of real student data across coach groups.")

    col_input, col_settings = st.columns([2, 1])

    with col_input:
        st.subheader("1. Input Student Data")
        # Sample data to make it look real immediately
        sample_data = "Marc, 19\nSophie, 20\nJean, 18\nLucie, 21\nAhmed, 19\nElena, 20\nChloe, 18\nMatteo, 19"
        raw_input = st.text_area("Paste 'Name, Age' list here (one per line):", value=sample_data, height=150)

    with col_settings:
        st.subheader("2. Coach Setup")
        num_coaches = st.number_input("Number of Coach Groups", min_value=1, value=3)
        sort_by_age = st.checkbox("Sort by Age before splitting?")

    if st.button("Run Equal Distribution Algorithm"):
        # Process the input string into a list of tuples
        try:
            lines = [line.strip() for line in raw_input.split('\n') if ',' in line]
            students = []
            for line in lines:
                name, age = line.split(',')
                students.append({'Name': name.strip(), 'Age': int(age.strip())})
            
            df = pd.DataFrame(students)

            if sort_by_age:
                df = df.sort_values(by='Age')
            else:
                df = df.sample(frac=1).reset_index(drop=True) # Shuffle for fairness

            # ALGORITHM: Partitioning into N groups totally equally
            # We use array_split to handle the math (handles remainders automatically)
            groups = np.array_split(df, num_coaches)
            
            st.divider()
            st.success(f"Successfully divided {len(df)} students into {num_coaches} groups.")

            # Display Results in chic columns
            cols = st.columns(min(num_coaches, 4)) # Limit to 4 cols for layout
            for i, group in enumerate(groups):
                with cols[i % 4]:
                    st.markdown(f"**Coach Group {i+1}**")
                    st.dataframe(group, hide_index=True)
                    st.caption(f"Count: {len(group)}")

        except Exception as e:
            st.error(f"Data Format Error: Ensure you use 'Name, Age' format. Error: {e}")
# ==========================================
# MODULE 3: EVENT ROI PREDICTOR
# ==========================================
elif page == "Event ROI Predictor":
    st.title("📊 Predictive Event Analytics")
    st.write("Quantifying the success probability of student integration events.")

    with st.expander("Configure Event Parameters", expanded=True):
        event_name = st.text_input("Event Name", value="Networking Apéro")
        est_attendance = st.slider("Target Attendance", 10, 500, 100)
        cost = st.number_input("Estimated Cost (CHF)", value=400)
        days_to_exams = st.slider("Days Until Midterms/Exams", 0, 60, 30)

    # Logic
    cost_per_head = cost / est_attendance
    timing_score = 100 if days_to_exams > 21 else (days_to_exams / 21) * 100
    efficiency_score = max(0, 100 - (cost_per_head * 5)) 
    success_prob = (timing_score * 0.6) + (efficiency_score * 0.4)

    st.write("---")
    st.subheader(f"Forecast for: {event_name}")
    
    c1, c2 = st.columns(2)
    c1.metric("Efficiency (CHF/Head)", f"{cost_per_head:.2f}")
    c2.metric("Success Probability", f"{success_prob:.1f}%")

    if success_prob > 75:
        st.success("✅ **High Impact Potential.** Strategic alignment confirmed.")
    else:
        st.warning("⚠️ **Risk Identified.** Consider rescheduling to avoid academic conflicts.")

# ==========================================
# MODULE 4: WEEKEND SKI LOGISTICS
# ==========================================
elif page == "Weekend Ski Logistics":
    st.title("🎿 Weekend Ski: High-Complexity Operations")
    st.write("Optimizing the financial and logistical pillars of the major annual event.")

    with st.container():
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Fixed Infrastructure")
            participants = st.number_input("Target Participants", value=50, step=5)
            hotel_cost = st.number_input("Housing (Total CHF)", value=1500)
            bus_cost = st.number_input("Transport (Total CHF)", value=800)
            
        with c2:
            st.subheader("Variable & Risk Factors")
            ski_pass = st.number_input("Ski Pass / Person (CHF)", value=55)
            food_social = st.number_input("Food & Social / Person (CHF)", value=30)
            buffer = st.slider("Safety Margin (%)", 0, 20, 10)

    # The Logistics Engine
    total_fixed = hotel_cost + bus_cost
    total_var = (ski_pass + food_social) * participants
    total_raw = total_fixed + total_var
    total_with_buffer = total_raw * (1 + (buffer / 100))
    break_even = total_with_buffer / participants

    st.divider()
    r1, r2, r3 = st.columns(3)
    r1.metric("Projected Total Cost", f"{total_with_buffer:,.0f} CHF")
    r2.metric("Break-Even Ticket Price", f"{break_even:.2f} CHF")
    r3.metric("Margin for Risk", f"{total_with_buffer - total_raw:,.0f} CHF")

    st.write("---")
    st.subheader("Pricing Strategy & Subsidy")
    subsidy = st.slider("Association Subsidy (CHF)", 0, 1000, 250)
    final_price = (total_with_buffer - subsidy) / participants
    
    st.markdown(f"### **Final Student Price: {final_price:.2f} CHF**")
    
    if final_price < 120:
        st.success("✅ **Accessibility Target Met.** The event is financially inclusive for the cohort.")
    else:
        st.error("🛑 **Accessibility Alert.** Cost exceeds social-integration guidelines. Recommend higher subsidy.")