# === app.py: Esther's Exact Survey in Streamlit ===

import streamlit as st
import json
import os
import smtplib
from email.message import EmailMessage

st.set_page_config(page_title="Esther's Onboarding Survey", layout="centered")

# === Welcome Message and Branding ===
st.image("https://your-logo-url.com/logo.png", width=120)  # Optional logo
st.title("Welcome to the Esther AI Journey Platform")
st.markdown("""
#### Phase 1A: Onboarding & Profile Creation  
Thank you for beginning your journey with us. This survey helps us understand who you are, what you care about, and how we can support your goals.  
Once completed, our system will generate a personalized plan and notify your support team.
""")

st.header("Demographic Information")

# ... (ALL SURVEY FIELDS REMAIN UNCHANGED)

# === Helper function to send counselor notification ===
def notify_counselor(profile_path):
    try:
        with open(profile_path, "r") as f:
            profile = json.load(f)

        # Simulated counselor email logic (replace with actual in production)
        msg = EmailMessage()
        msg['Subject'] = f"New Student Survey Submitted: {profile.get('name', 'Unknown')}"
        msg['From'] = "no-reply@estherai.org"
        msg['To'] = "counselor@example.com"
        msg.set_content(f"A new survey was submitted. View the profile at: {profile_path}")

        # This example skips sending actual email — SMTP config needed for real use
        print("Email prepared to notify counselor.")

    except Exception as e:
        print("Notification error:", e)

# === Save to file and trigger post-submission flow ===
if st.button("Submit Survey"):
    data = locals()
    os.makedirs("data", exist_ok=True)
    profile_path = "data/esther_profile.json"
    with open(profile_path, "w") as f:
        json.dump({k: v for k, v in data.items() if not k.startswith("st")}, f, indent=2)

    st.success("✅ Survey submitted successfully. Esther’s journey starts here!")

    # === Notify Counselor and Start AI Planning ===
    notify_counselor(profile_path)
    st.info("📬 A notification has been sent to your counselor. Your AI-guided profile is being reviewed.")
    st.markdown("""
    Next steps:
    - You will receive a personalized dashboard link.
    - Your counselor and family will be provided tailored guidance to support your growth.
    - A mentor will be invited to help once your path becomes more defined.
    """)

    # === Dashboard Preview Placeholder ===
    st.subheader("🔍 Preview: Your Future Dashboard")
    st.markdown("""
    - **Profile Summary**: Shows your interests, goals, and values.
    - **Career Suggestions**: AI-recommended fields and education paths.
    - **Resources**: Videos, mentors, scholarships, and learning tools.
    - **Your Support Team**: Family, teachers, and future mentors.
    """)
