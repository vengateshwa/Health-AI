# app.py - Streamlit main app for HealthAI

import sys
sys.modules["torch.classes"] = None

import multiprocessing
multiprocessing.set_start_method("spawn", force=True)

import os
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"
os.environ["TORCH_DISABLE_JIT"] = "1"

import streamlit as st

# Streamlit Page Config
st.set_page_config(
    page_title="HealthAI",
    layout="centered",
    initial_sidebar_state="auto",
    page_icon="🩺"
)

# Sidebar background color (sky blue) using custom style
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #81e5fe;
    }
    [data-testid="stSidebar"] .css-1v3fvcr, [data-testid="stSidebar"] .css-1v3fvcr * {
        color:white;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
page = st.sidebar.radio("🔍 Navigate", [
    "🏠 Home",
    "💬 Patient Chat",
    "🦠 Disease Prediction",
    "💊 Treatment Plans",
    "📊 Health Analytics"
])

# Home Page
if page == "🏠 Home":
    st.markdown("""
        <div style='padding:20px; border-radius:10px;'>
            <h1 style='text-align:center; color:green;'>👨‍⚕ Welcome to HealthAI 🏥</h1>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(
        "<p style='text-align:center; font-size:17px; max-width:600px; margin:auto;'>"
        "HealthAI harnesses IBM Watson Machine Learning and Generative AI to provide intelligent healthcare assistance, offering users accurate medical insights."
        "</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <ul style='font-size:16px; max-width:500px; margin:auto;'>
            <li><strong>Patient Chat</strong>: Ask health-related questions and receive clear, empathetic answers.</li>
            <li><strong>Disease Prediction</strong>: Enter symptoms to identify likely conditions and get guidance.</li>
            <li><strong>Treatment Plans</strong>: Get personalized treatment advice for specific conditions.</li>
            <li><strong>Health Analytics</strong>: Visualize and understand your health trends over time.</li>
        </ul>
        """, unsafe_allow_html=True
    )

    st.markdown("<p style='text-align:center; color:light-gray;'>✨ Powered by IBM Granite, Streamlit & ❤ by Liki</p>", unsafe_allow_html=True)

    # Centered updated image
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(
            "https://future-business.org/wp-content/uploads/2022/03/dreamstime_s_155234616.jpg",
            width=750
        )

    # Center the "Click here for tips" button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        show_tips = st.button("💡 Click here for tips", use_container_width=True)

    # Tips display
    if show_tips:
        tips = [
            "🥦 Eat more fruits and vegetables!",
            "💤 Sleep 7-8 hours daily.",
            "🚶‍♀ Walk regularly to reduce BP.",
            "💧 Drink 2-3L water per day.",
            "🧘‍♀ Meditate for stress relief.",
            "🦷 Brush + floss twice a day.",
            "🕒 Keep a regular sleep routine.",
            "📵 Limit screen time at night.",
            "🥗 Avoid junk food.",
            "🏃‍♀ Exercise 30 mins/day.",
            "🧴 Use sunscreen outdoors.",
            "🥤 Reduce sugary drinks."
        ]

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            for tip in tips:
                st.markdown(
                    f"""
                    <div style='background-color:green; color:white; padding:12px 20px;
                                border-radius:8px; margin:6px 0px; width:100%;
                                text-align:center; font-size:16px; font-weight:500;
                                box-shadow:0 2px 5px rgba(0,0,0,0.1);'>
                        {tip}
                    </div>
                    """, unsafe_allow_html=True
                )

# Patient Chat
elif page == "💬 Patient Chat":
    st.header("💬 Patient Chat")
    question = st.text_input("Ask your health question:")
    if question:
        st.info("🤖 Generating response...")
        st.success("Based on your question, it's best to consult a doctor if symptoms persist. Stay hydrated and monitor your health.")

# Disease Prediction
elif page == "🦠 Disease Prediction":
    st.header("🦠 Disease Prediction")
    symptoms = st.text_area("Enter your symptoms (e.g. headache, fatigue, fever):")
    if st.button("Predict Disease") and symptoms:
        st.info("🔎 Analyzing symptoms...")
        st.success("Possible conditions: Viral Infection (70%), Migraine (20%), COVID-19 (10%). Please consult a physician.")

# Treatment Plans
elif page == "💊 Treatment Plans":
    st.header("💊 Personalized Treatment Plan")
    condition = st.text_input("Enter your diagnosed condition:")
    if st.button("Generate Treatment Plan") and condition:
        st.info("📋 Generating plan...")
        st.success(f"Treatment for {condition}:\n- Medication: Paracetamol\n- Rest\n- Drink fluids\n- Follow-up in 3 days")

# Health Analytics
elif page == "📊 Health Analytics":
    st.header("📊 Health Analytics Dashboard")
    st.info("📈 Upload health metrics to visualize trends")
    uploaded_file = st.file_uploader("Upload CSV file (heart rate, BP, glucose)")
    if uploaded_file:
        import pandas as pd
        import altair as alt
        df = pd.read_csv(uploaded_file)
        st.write("📄 Raw Data:", df.head())
        for column in df.columns[1:]:
            chart = alt.Chart(df).mark_line().encode(
                x=alt.X(df.columns[0], title="Date"),
                y=alt.Y(column, title=column),
                tooltip=[df.columns[0], column]
            ).properties(title=f"Trend: {column}")
            st.altair_chart(chart, use_container_width=True)