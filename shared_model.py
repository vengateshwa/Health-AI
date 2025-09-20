from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import streamlit as st
import os

@st.cache_resource
def load_model():
    try:
        model_path = os.path.join(os.getcwd(), "granite")

        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForCausalLM.from_pretrained(model_path)
        chatbot_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer, device=-1)

        return chatbot_pipeline
    except Exception as e:
        st.error(f"❌ Failed to load model: {e}")
        return None

chatbot = load_model()
