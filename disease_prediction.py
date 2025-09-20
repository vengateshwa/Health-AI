import streamlit as st
from shared_model import chatbot

def main():
    st.title("🦠 Disease Prediction")
    st.write("🤖 Enter your symptoms and I'll try to predict the disease.")

    if chatbot is None or not callable(chatbot):
        st.error("❌ AI model not available or not callable.")
        st.stop()

    user_input = st.text_input("📝 Your Symptoms:", placeholder="e.g. fever, cough")

    if st.button("Predict"):
        if not user_input.strip():
            st.warning("⚠ Please enter symptoms.")
            return

        prompt = f"User: My symptoms are {user_input}. What disease could this be?\nAI:"

        with st.spinner("🔍 Predicting..."):
            try:
                result = chatbot(prompt, max_new_tokens=120)
                response = result[0]['generated_text'].strip() if result else "⚠ Couldn't generate a response."
            except Exception as e:
                response = f"❌ Error: {str(e)}"

        st.success(f"🧾 Prediction: {response}")

    st.info("📌 Note: This is an AI-based suggestion. Please consult a doctor for a confirmed diagnosis.")
