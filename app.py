
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("spam_ham_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Spam / Ham Detector",
    page_icon="📩",
    layout="centered"
)

# Heading
st.title("📩 Spam / Ham Detector")
st.write("Enter an SMS message to check whether it is Spam or Ham.")

st.divider()

# Input box
message = st.text_area(
    "Enter your SMS message",
    placeholder="Type your message here...",
    height=150
)

# Prediction button
if st.button("Predict", type="primary", use_container_width=True):

    if not message.strip():
        st.warning("Please enter a message first.")

    else:
        prediction = model.predict([message.strip()])[0]
        prediction = str(prediction).strip().lower()

        st.subheader("Prediction Result")

        if prediction == "spam":
            st.error("🚨 SPAM")
            st.write("This message is classified as Spam.")

        elif prediction == "ham":
            st.success("✅ HAM")
            st.write("This message is classified as Ham.")

        else:
            st.warning(f"Predicted class: {prediction}")
