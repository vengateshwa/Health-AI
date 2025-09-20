import streamlit as st
import pandas as pd
from shared_model import chatbot

def main():
    st.title("📊 Health Analytics + AI Insights")
    st.write("📈 View health data trends and ask questions to your AI assistant.")

    if chatbot is None or not callable(chatbot):
        st.error("❌ AI model not available or not callable.")
        st.stop()

    data = {
        "Date": pd.date_range(start="2025-06-01", periods=7),
        "Heart Rate": [78, 80, 76, 85, 79, 77, 81],
        "Blood Pressure": [120, 122, 121, 119, 123, 124, 120],
        "Blood Sugar": [95, 98, 105, 110, 102, 97, 100]
    }

    df = pd.DataFrame(data).set_index("Date")

    st.subheader("❤ Heart Rate")
    st.line_chart(df["Heart Rate"])

    st.subheader("💉 Blood Pressure")
    st.line_chart(df["Blood Pressure"])

    st.subheader("🍬 Blood Sugar")
    st.line_chart(df["Blood Sugar"])

    st.markdown("---")
    st.subheader("🤖 Ask AI about your health data")

    query = st.text_input("Ask a question:", placeholder="e.g. Is my BP trend normal?")
    if st.button("Ask AI"):
        if not query.strip():
            st.warning("⚠ Please enter a question.")
            return

        prompt = f"User: Based on my health data, {query}\nAI:"
        with st.spinner("🔍 Analyzing..."):
            try:
                result = chatbot(prompt, max_new_tokens=120)
                response = result[0]['generated_text'].strip() if result else "⚠ Couldn't generate a response."
            except Exception as e:
                response = f"❌ Error: {str(e)}"

        st.success(f"🧠 AI Insight: {response}")
