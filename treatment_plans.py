import streamlit as st
from shared_model import chatbot

def main():
    st.title("💊 AI-Powered Treatment Plans")
    st.write("📋 Enter a condition and I'll suggest a basic treatment plan.")

    if chatbot is None or not callable(chatbot):
        st.error("❌ AI model not available or not callable.")
        st.stop()

    condition = st.text_input("🩺 Diagnosed Condition:", placeholder="e.g. flu, covid, diabetes")

    if st.button("Suggest Treatment Plan"):
        if not condition.strip():
            st.warning("⚠ Please enter a condition.")
            return

        prompt = f"User: What is the treatment plan for {condition}?\nAI:"
        with st.spinner("💡 Generating plan..."):
            try:
                result = chatbot(prompt, max_new_tokens=120)
                response = result[0]['generated_text'].strip() if result else "⚠ Couldn't generate a response."
            except Exception as e:
                response = f"❌ Error: {str(e)}"

        st.success(f"💡 Suggested Plan:\n\n{response}")
