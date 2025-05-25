# === app.py: Esther's Exact Survey in Streamlit ===

import streamlit as st
import json
import os

st.set_page_config(page_title="Esther's Onboarding Survey", layout="centered")
st.title("Phase 1A: Esther's Onboarding & Profile Creation")

st.header("Demographic Information")

# Student Info
name = st.text_input("Name")
city = st.text_input("City, State, Zip Code")
dob = st.date_input("Date of Birth")
gender = st.selectbox("Gender", ["Male", "Female", "Non-binary/Other"])
email = st.text_input("Email Address")
cell = st.text_input("Cell Phone Number")
race = st.multiselect("Race/Ethnicity", [
    "Hispanic/Latino", "White", "Black or African American", "Asian",
    "American Indian/Alaska Native", "Native Hawaiian/Pacific Islander", "Prefer not to answer"
])

# Parent Info
st.subheader("Parent/Guardian Information")
parent_education = st.selectbox("Highest level of education completed by parent(s)", [
    "High school or less", "Some college or associate degree", "Bachelor’s degree or higher"
])
parent_occupation = st.selectbox("Occupation of parent(s)", [
    "Professional/Technical", "Service/Labor/Skilled Trades", "Unemployed/Not working outside home"
])
home_language = st.selectbox("Language/Primary language spoken at home", ["English", "Spanish", "Other"])

# School Info
st.subheader("School Information")
grade = st.selectbox("Current grade level", ["9th grade", "10th grade", "11th grade", "12th grade"])
school_name = st.text_input("School name and location (City, State)")
school_type = st.selectbox("Type of school", ["Public", "Private", "Charter", "Home school"])

# Socioeconomic
st.subheader("Socioeconomic Information")
free_lunch = st.selectbox("Eligibility for free/reduced-price lunch", ["Yes", "No", "Not Sure"])
income = st.selectbox("Family income (optional)", ["Below $50,000", "$50,000–$100,000", "Above $100,000"])
first_gen = st.selectbox("First-generation college student status", ["Yes", "No", "Not Sure"])

# VALUES
st.header("Values")
career_values = st.multiselect("What matters most to you when thinking about your future career?", [
    "Making a lot of money", "Helping others", "Having job security", "Being creative",
    "Having flexibility or free time", "Being a leader or in charge"
])
impact = st.radio("What kind of impact do you hope to make?", [
    "Solve big problems like climate change or poverty",
    "Improve lives around me",
    "Inspire others through work or art"
])
career_choice = st.radio("Which would you rather have?", [
    "A job that pays well, even if I don’t love it",
    "A job that I love, even if it doesn’t pay the most",
    "A job that gives me time to enjoy life outside of work"
])

# IDENTITY
st.header("Identity")
self_reflection = st.radio("How often do you think about who you are or what makes you special?", [
    "A lot", "Sometimes", "Not really", "Never"
])
uncertainty_response = st.radio("When unsure about who you are, what do you usually do?", [
    "Ignore it", "Talk to someone", "Write/draw/music", "Don't know"
])
identity_challenges = st.multiselect("What makes it hard to understand who you are?", [
    "Act differently around people", "No one asks how I feel", "Don’t see people like me doing big things", "Haven’t thought about it"
])
safety_support = st.selectbox("Who helps you feel safe or accepted?", [
    "A friend", "A family member", "A teacher/counselor/coach", "No one right now"
])
identity_help = st.selectbox("What would help the most when you feel lost?", [
    "Someone really listening", "Learning more about culture/history",
    "Finding stories of people like me", "A space to be myself"
])
adult_understanding = st.multiselect("What do you wish more adults understood?", [
    "We’re going through a lot", "We want to be heard", "We have big dreams", "We need help finding who we are"
])
best_self = st.selectbox("What makes you feel the most like yourself?", [
    "Doing something I love", "Being around people who get me",
    "Talking about dreams", "Still figuring it out"
])
background_effect = st.selectbox("How do you feel when expected to act a certain way because of background?", [
    "Misunderstood", "Try to fit", "Want to show true self", "Don't think about it"
])
discovery_space = st.selectbox("What kind of space would help you discover more about yourself?", [
    "A quiet space", "A sharing group", "A mentor", "Not sure but want to find out"
])
future_message = st.selectbox("If you could tell your future self one thing, what would it be?", [
    "Keep going", "Be proud", "Try new things", "You are not alone"
])

# CAREER/EDUCATION/GOALS/PLANS
st.header("Career, Education, Goals, and Plans")
career_interest = st.selectbox("Which of these careers sounds the most interesting to you?", [
    "HealthTech", "FinTech", "Computing", "EdTech", "Urban Agriculture"
])
favorite_subject = st.selectbox("Which school subject do you enjoy most?", [
    "Science or health", "Math or business", "Computers or coding",
    "Education or writing", "Environmental science or biology"
])
ed_path = st.selectbox("What type of education do you think you’ll need?", [
    "Certificate", "Community college", "Bachelor’s degree", "I’m not sure"
])
highschool_action = st.selectbox("What’s one thing you’d want to do in high school?", [
    "Health science classes", "Learn finance/business apps", "Computer science",
    "Use tech to help others", "Join garden or science project"
])
technology_use = st.selectbox("How do you want to use technology?", [
    "To help people stay healthy", "To manage money",
    "To build apps/games", "To make learning easier", "To grow food/protect environment"
])
skills = st.multiselect("Which skills do you already have or want to grow?", [
    "Working with tools", "Solving math problems", "Writing code",
    "Helping others learn", "Gardening/earth care"
])
custom_class = st.selectbox("If your school could offer one class, which would you pick?", [
    "Intro to Medical Tech", "Finance & Money Apps", "Coding", "Learning Tech", "Urban Farming"
])
career_learning = st.multiselect("Where would you like to learn more about careers like these?", [
    "From someone in the career", "In class/project", "Field trip/job shadow",
    "Summer/after-school program", "I want to explore more"
])
career_question = st.selectbox("What’s your biggest question about your future career?", [
    "What classes do I need?", "How much money can I make?", "What is the day-to-day like?",
    "What degree or training do I need?", "Can I find a job like that near me?"
])
career_support = st.multiselect("What would help you feel ready for a career you care about?", [
    "A mentor", "A list of steps", "A hands-on class", "Paid internship", "Someone who believes in me"
])

# Ecosystem of Care
st.header("Ecosystem of Care: Student Voice Questions")
trusted_advisor = st.selectbox("Who do you trust for advice or support?", [
    "Family member", "Teacher or counselor", "Mentor or coach", "Friend or peer", "No one"
])
info_channel = st.selectbox("Best way to receive info about college/jobs?", [
    "Text message", "Social media", "In-person", "Email/school app", "Flyers/posters"
])
learning_env = st.selectbox("Where do you feel most comfortable learning about careers?", [
    "School class", "Community center", "Job site", "Online", "Group with shared culture"
])
connection_factors = st.multiselect("What helps you feel connected to people who care?", [
    "They listen and don’t judge", "They come from my background",
    "They check in", "They show real options", "Still waiting to find someone"
])
support_barriers = st.multiselect("What gets in the way of getting support?", [
    "Don’t know who to ask", "No one checks in", "Don’t see role models",
    "Lack of access (transport/internet)", "Busy helping at home"
])
career_ease = st.multiselect("What would make it easier to explore your future?", [
    "Paid internships", "Neighborhood workshops",
    "One-on-one support", "Black/Latinx leaders", "Peer program"
])
school_improvement = st.multiselect("What’s one thing schools could do better?", [
    "Talk to us", "Offer real skills", "Let us lead", "Include culture/voices", "Be consistent"
])

# Save to file
if st.button("Submit Survey"):
    data = locals()
    os.makedirs("data", exist_ok=True)
    with open("data/esther_profile.json", "w") as f:
        json.dump({k: v for k, v in data.items() if not k.startswith("st")}, f, indent=2)
    st.success("Survey submitted successfully. Esther’s journey starts here!")
