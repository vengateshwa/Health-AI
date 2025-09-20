import streamlit as st
from shared_model import chatbot

def main():
    st.title("💬 AI Health Chat")
    st.write("👋 Ask any health-related question to your AI assistant!")

    if chatbot is None or not callable(chatbot):
        st.error("❌ AI model not available or not callable.")
        st.stop()

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("🧠 Ask your question:", placeholder="e.g. What are the symptoms of diabetes?")

    if st.button("Ask"):
        if not user_input.strip():
            st.warning("⚠ Please enter a question.")
            return

        greetings = ["hi", "hello", "hey", "hlo"]
        if user_input.lower().strip() in greetings:
            response = "Hello! 😊 How can I assist you with your health today?"
        else:
            prompt = f"User: {user_input}\nAI:"
            with st.spinner("🤖 Thinking..."):
                try:
                    result = chatbot(prompt, max_new_tokens=120, return_full_text=False)
                    if result and isinstance(result, list) and 'generated_text' in result[0]:
                        response = result[0]['generated_text'].strip()
                    else:
                        response = "⚠ Model didn't return a valid response."
                except Exception as e:
                    response = f"❌ Error during generation: {e}"

        st.success(response)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("HealthAI", response))

    st.subheader("📜 Chat History")
    for sender, message in st.session_state.chat_history:
        st.markdown(f"{'🧑‍💬' if sender == 'You' else '🤖'} {sender}:** {message}")

    if st.button("🧹 Clear Chat History"):
        st.session_state.chat_history = []
