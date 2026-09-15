import streamlit as st

st.title("🛡️ ScamShield")
st.subheader("Scam Message Detector")

message = st.text_area("Enter your message:")

if st.button("Check Message"):

    if message.strip() == "":
        st.warning("Please enter a message")

    else:
        scam_words = [
            "won", "prize", "lottery", "urgent",
            "click", "verify", "kyc", "blocked",
            "cashback", "bank details", "free",
            "otp", "claim", "reward"
        ]

        text = message.lower()
        found = []

        for word in scam_words:
            if word in text:
                found.append(word)

        if len(found) >= 2:
            st.error("🚨 SCAM MESSAGE")
            st.write("Risk Level: HIGH")
            st.write("Suspicious words:", ", ".join(found))
            st.warning("⚠️ Do not click links or share personal details.")

        else:
            st.success("✅ SAFE MESSAGE")
            st.write("Risk Level: LOW")
            st.write("No suspicious pattern detected.")