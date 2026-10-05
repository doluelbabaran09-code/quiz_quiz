import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="Quizz", page_icon="📝", layout="centered")

# --- HEART ANIMATION FUNCTION ---
def show_heart_animation():
    st.markdown(
        """
        <style>
        @keyframes floatHearts {
            0% { transform: translateY(0vh) scale(0.8); opacity: 1; }
            100% { transform: translateY(-100vh) scale(1.2); opacity: 0; }
        }
        .heart {
            position: fixed;
            bottom: -10vh;
            font-size: 2.5rem;
            animation: floatHearts 3.5s ease-in-out infinite;
            z-index: 9999;
        }
        .h1 { left: 10%; animation-delay: 0s; }
        .h2 { left: 25%; animation-delay: 0.6s; }
        .h3 { left: 40%; animation-delay: 0.2s; }
        .h4 { left: 60%; animation-delay: 0.8s; }
        .h5 { left: 75%; animation-delay: 0.4s; }
        .h6 { left: 90%; animation-delay: 0.7s; }
        </style>
        <div class="heart h1">💖</div>
        <div class="heart h2">❤️</div>
        <div class="heart h3">💕</div>
        <div class="heart h4">💖</div>
        <div class="heart h5">💗</div>
        <div class="heart h6">❤️</div>
        """,
        unsafe_allow_html=True
    )

st.title("📝 Quizz")
st.write("Verification muna Bossing😉")

# --- HEADER MEME ---
st.image("welcome.jpg", use_container_width=True)

# --- SECTION 1: RESPONDENT DETAILS ---
st.subheader("📋 Your Details")
st.warning("⚠️ **Note:** Please put a period (`.`) at the end of your Last Name (e.g., `Dela Cruz.`)!")

email = st.text_input("Email address *", placeholder="example@email.com")
first_name = st.text_input("First Name *")
last_name = st.text_input("Last Name *", placeholder="...")
year_level = st.selectbox("Year Level *", ["1st Year", "2nd Year", "3rd Year", "4th Year", "Other"])
course = st.text_input("Course / Major *", placeholder="e.g. BS Computer Engineering")

st.divider()

# --- SECTION 2: WRITTEN / PERSONAL QUESTIONS ---
st.subheader("💭 Personal Questions")

birth_date = st.text_input("Ano Birthday ko?", placeholder="e.g. October 15")
hometown = st.text_input("Saan ako nakatira rn?", placeholder="City / Address")

st.divider()

# --- SECTION: LOVE LANGUAGES ---
st.subheader("💌 Love Languages")

st.write("**What's your love language in GIVING?** *(Check mo na lang para mas madali! 😉)*")
col_g1, col_g2 = st.columns(2)
with col_g1:
    g_words = st.checkbox("Words of Affirmation 💬", key="g_words")
    g_acts = st.checkbox("Acts of Service 🛠️", key="g_acts")
    g_gifts = st.checkbox("Receiving Gifts 🎁", key="g_gifts")
with col_g2:
    g_time = st.checkbox("Quality Time ⏳", key="g_time")
    g_touch = st.checkbox("Physical Touch 🤝", key="g_touch")

st.write("---")
st.write("**What's your love language in RECEIVING?** *(Check mo na lang para mas madali! 😉)*")
col_r1, col_r2 = st.columns(2)
with col_r1:
    r_words = st.checkbox("Words of Affirmation 💬", key="r_words")
    r_acts = st.checkbox("Acts of Service 🛠️", key="r_acts")
    r_gifts = st.checkbox("Receiving Gifts 🎁", key="r_gifts")
with col_r2:
    r_time = st.checkbox("Quality Time ⏳", key="r_time")
    r_touch = st.checkbox("Physical Touch 🤝", key="r_touch")

st.divider()

# --- SECTION 3: MULTIPLE CHOICE QUIZ ---
st.subheader("🎯 Quiz Time")

score = 0
total_mc_questions = 6

# Question 3: Favorite Artist
q3 = st.radio(
    "Who is my favorite artist?",
    ["Malcolm Todd", "Arthur Nery", "Hev Abi"],
    index=None
)
if q3 == "Malcolm Todd":
    score += 1

st.divider()

# Question 4: Comfort Food
q4 = st.radio(
    "What is my ultimate comfort food?",
    ["Chicken", "Ice cream", "Fries"],
    index=None
)
if q4 == "Ice cream":
    score += 1

st.divider()

# Question 5: What do you want the most?
q5 = st.radio(
    "What do I want the most right now?",
    ["Magkapera", "Maging successful sa illegal", "Kiss mo"],
    index=None
)
if q5 == "Kiss mo":
    st.image("kiss.jpg", caption="Hule Boss?", use_container_width=True)
    score += 1

st.divider()

# Question 6: Games I Play
st.subheader("🎮 Games that I play the most?")

games_choice = st.radio(
    "Select the games:",
    ["Mobile Legends (ML) & CODM", "Valorant & Roblox", "Genshin Impact"],
    index=None
)
if games_choice == "Mobile Legends (ML) & CODM":
    score += 1

st.divider()

# Question 7: Who is my crush? (Her Pictures)
st.subheader("Sino crush ko?")
st.write("😉")

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
    score += 1

st.divider()

# Question 8: Sino Pinakapogi?
st.subheader("🌟 Sino pinakapogi?")
st.write("Pumili ka sa mga options sa ibaba! 😉")

pogi_col1, pogi_col2, pogi_col3 = st.columns(3)

with pogi_col1:
    st.image("me1.jpg", use_container_width=True)
    st.markdown("<h4 style='text-align: center;'>Dwight Ramos</h4>", unsafe_allow_html=True)

with pogi_col2:
    st.image("me2.jpg", use_container_width=True)
    st.markdown("<h4 style='text-align: center;'>Joshua Garcia</h4>", unsafe_allow_html=True)

with pogi_col3:
    st.image("me3.jpg", use_container_width=True)
    st.markdown("<h4 style='text-align: center;'>Choi Hyun-wook</h4>", unsafe_allow_html=True)

pogi_choice = st.radio(
    "Sino ang pinakapogi para sa'yo?",
    ["Dwight Ramos", "Joshua Garcia", "Choi Hyun-wook"],
    index=None
)

if pogi_choice in ["Dwight Ramos", "Joshua Garcia"]:
    st.image("nailong.jpg", caption="Nays choice", use_container_width=True)
    score += 1
elif pogi_choice == "Choi Hyun-wook":
    st.image("fist.jpg", caption="ah okay lng, ano bang palag ko jan?", use_container_width=True)
    score += 1

st.divider()

# --- SECTION 4: QUESTION FOR HER ---
st.subheader("🌸 Question Ko Sa'yo")

st.write("**Kung mag-first move ako ng kiss, papayag ka ba?**")

st.image("lord_meme.jpg", use_container_width=True)

kiss_permission = st.radio(
    "Sagot mo:",
    ["Yes!", "No!"],
    index=None
)

st.divider()

# --- SUBMIT BUTTON & FORMSPREE EMAIL LOGIC ---
if st.button("Submit Answers ✨"):
    if not email or not first_name:
        st.error("Please fill in your Email and First Name before submitting!")
    else:
        form_url = "https://formspree.io/f/mqpekvqk"
        
        # Build Love Language Giving String
        giving_list = []
        if g_words: giving_list.append("Words of Affirmation")
        if g_acts: giving_list.append("Acts of Service")
        if g_gifts: giving_list.append("Receiving Gifts")
        if g_time: giving_list.append("Quality Time")
        if g_touch: giving_list.append("Physical Touch")
        giving_str = ", ".join(giving_list) if giving_list else "None selected"

        # Build Love Language Receiving String
        receiving_list = []
        if r_words: receiving_list.append("Words of Affirmation")
        if r_acts: receiving_list.append("Acts of Service")
        if r_gifts: receiving_list.append("Receiving Gifts")
        if r_time: receiving_list.append("Quality Time")
        if r_touch: receiving_list.append("Physical Touch")
        receiving_str = ", ".join(receiving_list) if receiving_list else "None selected"

        payload = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "year_level": year_level,
            "course": course,
            "birth_date": birth_date,
            "hometown": hometown,
            "love_language_GIVING": giving_str,
            "love_language_RECEIVING": receiving_str,
            "favorite_artist": q3,
            "comfort_food": q4,
            "what_i_want_most": q5,
            "games_played": games_choice,
            "crush_choice": crush_choice,
            "pinakapogi_choice": pogi_choice,
            "kiss_permission": kiss_permission,
            "quiz_score": f"{score}/{total_mc_questions}"
        }
        
        try:
            res = requests.post(form_url, data=payload)
            if res.status_code == 200:
                st.balloons()
                show_heart_animation()  # Correct function call
                st.success("Response recorded! Thanks You BEBE! 🎉")
                st.info(f"Quiz Score: {score}/{total_mc_questions}")
            else:
                st.error(f"Formspree Error (Status {res.status_code}): Please check if reCAPTCHA is disabled in Formspree settings!")
        except Exception as e:
            st.error(f"Error submitting answers: {e}")