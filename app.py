import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="Get to Know Me Quiz", page_icon="📝", layout="centered")

st.title("📝 Get to Know Me Quiz")
st.write("Fill out your details and see how well you know me! 😉")

# --- HEADER MEME ---
st.image("welcome.jpg", use_container_width=True)

# --- SECTION 1: RESPONDENT DETAILS ---
st.subheader("📋 Your Details")

email = st.text_input("Email address *", placeholder="example@email.com")
first_name = st.text_input("First Name *")
year_level = st.selectbox("Year Level *", ["1st Year", "2nd Year", "3rd Year", "4th Year", "Other"])
course = st.text_input("Course / Major *", placeholder="e.g. BS Computer Engineering")

st.divider()

# --- SECTION 2: WRITTEN / PERSONAL QUESTIONS ---
st.subheader("💭 Personal Questions")

birth_date = st.text_input("1. Ano Birthday ko?", placeholder="e.g. October 15")
hometown = st.text_input("2. Saan ako nakatira rn?", placeholder="City / Address")

st.divider()

# --- SECTION 3: MULTIPLE CHOICE QUIZ ---
st.subheader("🎯 Quiz Time")

score = 0
total_mc_questions = 5

# Question 3: Favorite Artist
q3 = st.radio(
    "3. Who is my favorite artist?",
    ["Malcolm Todd", "Arthur Nery", "Hev Abi"],
    index=None
)
if q3 == "Arthur Nery":  # <-- Adjust to your actual answer if needed
    score += 1

st.divider()

# Question 4: Comfort Food
q4 = st.radio(
    "4. What is my ultimate comfort food?",
    ["Chicken", "Ice cream", "Fries"],
    index=None
)
if q4 == "Chicken":  # <-- Adjust to your actual answer if needed
    score += 1

st.divider()

# Question 5: What do you want the most?
q5 = st.radio(
    "5. What do I want the most right now?",
    ["Magkapera", "Maging successful sa illegal", "Kiss mo"],
    index=None
)
if q5 == "Kiss mo":  # <-- Adjust to your actual answer if needed
    score += 1

st.divider()

# Question 6: Games I Play
st.subheader("🎮 6. Games that I play the most?")

games_choice = st.radio(
    "Select the games:",
    ["Mobile Legends (ML) & CODM", "Valorant & Roblox", "Genshin Impact"],
    index=None
)
if games_choice == "Mobile Legends (ML) & CODM":  # <-- Adjust to your main games
    score += 1

st.divider()

# Question 7: Who is my crush? (Her Pictures)
st.subheader("😳 7. Sino crush ko?")
st.write("Clue: Pumili ka sa mga pictures sa ibaba! 😉")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image("her1.jpg", caption="Option A", use_container_width=True)

with col2:
    st.image("her2.jpg", caption="Option B", use_container_width=True)

with col3:
    st.image("her3.jpg", caption="Option C", use_container_width=True)

with col4:
    st.image("kiss.jpg", caption="All of the above! ❤️", use_container_width=True)

crush_choice = st.radio(
    "Alin diyan ang crush ko?",
    ["Option A", "Option B", "Option C", "All of the above! ❤️"],
    index=None
)
if crush_choice is not None:
    score += 1  # Automatic point since all pictures are her!

st.divider()

# --- SECTION 4: QUESTION FOR HER ---
st.subheader("🌸 Question Ko Sa'yo")

st.write("**Kung mag-first move ako ng kiss, papayag ka ba?**")

# Your uploaded meme image here!
st.image("lord_meme.jpg", use_container_width=True)

kiss_permission = st.radio(
    "Sagot mo:",
    ["Yes", "No way! 😜"],
    index=None
)

st.divider()

# --- SUBMIT BUTTON & FORMSPREE EMAIL LOGIC ---
if st.button("Submit Answers ✨"):
    if not email or not first_name:
        st.error("Please fill in your Email and First Name before submitting!")
    else:
        # ⚠️ PASTE YOUR FORMSPREE ENDPOINT URL HERE ⚠️
        form_url = "https://formspree.io/f/YOUR_FORMSPREE_ID"
        
        payload = {
            "--- RESPONDENT DETAILS ---": "----------------",
            "Email": email,
            "First Name": first_name,
            "Year Level": year_level,
            "Course": course,
            "--- PERSONAL QUESTIONS ---": "----------------",
            "Birth Date Answer": birth_date,
            "Where I Live Answer": hometown,
            "--- QUIZ ANSWERS ---": "----------------",
            "Favorite Artist Choice": q3,
            "Comfort Food Choice": q4,
            "What I Want Most": q5,
            "Games Selected": games_choice,
            "Crush Choice": crush_choice,
            "--- HER ANSWER TO YOU ---": "----------------",
            "First Move Kiss Permission": kiss_permission,
            "Quiz Score": f"{score}/{total_mc_questions}"
        }
        
        try:
            res = requests.post(form_url, data=payload)
            if res.status_code == 200:
                st.balloons()
                st.success("Response recorded! Thanks for filling this out! 🎉")
                st.info(f"Quiz Score: {score}/{total_mc_questions}")
            else:
                st.error("Submission failed. Make sure you replaced YOUR_FORMSPREE_ID with your Formspree link!")
        except Exception as e:
            st.error(f"Error submitting answers: {e}")