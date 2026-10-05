import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="About Me Form", page_icon="📝", layout="centered")

st.title("📝 Get to Know Me Quiz")
st.write("Fill out your details and see how well you know me! 😉")

# Optional: Header Meme
st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWdtZzVsbzlobGJsdjl2Ym5vb2s1cDN2MjNyaWp6ZjJoM2d3N3dpdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3NjABnBOieYQE4BpkP/giphy.gif", use_column_width=True)

# --- SECTION 1: RESPONDENT DETAILS ---
st.subheader("📋 Your Details")

email = st.text_input("Email address *", placeholder="example@email.com")
first_name = st.text_input("First Name *")
year_level = st.selectbox("Year Level *", ["1st Year", "2nd Year", "3rd Year", "4th Year", "Other"])
course = st.text_input("Course / Major *", placeholder="e.g. BS Computer Engineering")

st.divider()

# --- SECTION 2: WRITTEN / PERSONAL QUESTIONS ---
st.subheader("💭 Personal Questions")

birth_date = st.text_input("1. When is my birth date?", placeholder="e.g. October 15")
hometown = st.text_input("2. Where am I originally from?", placeholder="City / Province")
fav_hobby = st.text_input("3. What's my favorite hobby or pastime?")

st.divider()

# --- SECTION 3: MULTIPLE CHOICE QUIZ WITH MEMES ---
st.subheader("🎯 Multiple Choice Questions")

score = 0
total_mc_questions = 2

# Meme before Question 1
st.image("https://i.imgflip.com/1ur9b0.jpg", caption="Choose carefully...", width=300)

q1 = st.radio(
    "4. What is my ultimate comfort food?",
    ["Pizza", "Ramen", "Tacos", "Ice Cream"],
    index=None
)
if q1 == "Ramen":  # <-- Change to your actual answer
    score += 1

st.divider()

# Meme before Question 2
st.image("https://i.imgflip.com/26am.jpg", caption="Think fast!", width=300)

q2 = st.radio(
    "5. If I could travel anywhere tomorrow, where would we go?",
    ["Japan", "Italy", "Iceland", "Greece"],
    index=None
)
if q2 == "Japan":  # <-- Change to your actual answer
    score += 1
st.subheader("6. Which of these is my dream pet?")

# Store the selected answer in session state
if "q6_answer" not in st.session_state:
    st.session_state.q6_answer = None

col1, col2 = st.columns(2)

with col1:
    st.image("https://images.unsplash.com/photo-1543466835-00a7907e9de1?w=400", caption="Golden Retriever")
    if st.button("Choose Dog 🐶", key="pet_dog"):
        st.session_state.q6_answer = "Golden Retriever"

with col2:
    st.image("https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=400", caption="Orange Cat")
    if st.button("Choose Cat 🐱", key="pet_cat"):
        st.session_state.q6_answer = "Orange Cat"

# Display selected choice
if st.session_state.q6_answer:
    st.success(f"You selected: {st.session_state.q6_answer}")

st.divider()

# --- SUBMIT BUTTON & FORMSPREE EMAIL LOGIC ---
if st.button("Submit Answers ✨"):
    if not email or not first_name:
        st.error("Please fill in your Email and First Name before submitting!")
    else:
        # PASTE YOUR FORMSPREE ENDPOINT URL HERE
        form_url = "https://formspree.io/f/YOUR_FORMSPREE_ID"
        
        payload = {
            "Email": email,
            "First Name": first_name,
            "Year Level": year_level,
            "Course": course,
            "Birth Date Answer": birth_date,
            "Hometown Answer": hometown,
            "Favorite Hobby Answer": fav_hobby,
            "Q4 Comfort Food": q1,
            "Q5 Travel Spot": q2,
            "Quiz Score": f"{score}/{total_mc_questions}"
        }
        
        try:
            res = requests.post(form_url, data=payload)
            if res.status_code == 200:
                st.balloons()
                st.success("Response recorded! Thanks for filling this out! 🎉")
                
                # Victory Meme on submission
                st.image("https://i.imgflip.com/1bgw.jpg", caption="You made it!")
                st.info(f"Quiz Score: {score}/{total_mc_questions}")
            else:
                st.error("Submission failed. Please check your Formspree endpoint!")
        except Exception as e:
            st.error(f"Error submitting answers: {e}")