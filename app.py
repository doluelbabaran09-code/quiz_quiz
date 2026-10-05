import streamlit as st

# Custom styling for mobile
st.set_page_config(page_title="How Well Do You Know Me?", page_icon="💖", layout="centered")

st.title(" How Well Do You Know Me?")
st.subheader("Time to return the favor! Let's see how many you get right. ")

# Track the score
score = 0
total_questions = 4

# Question 1
q1 = st.radio(
    "1. What is my ultimate comfort food?",
    ["Pizza", "Ramen", "Tacos", "Ice Cream"],
    index=None
)
if q1 == "Ramen":  # <-- Change "Ramen" to your actual answer
    score += 1

# Question 2
q2 = st.radio(
    "2. If I could travel anywhere tomorrow, where are we going?",
    ["Japan", "Italy", "Iceland", "Greece"],
    index=None
)
if q2 == "Japan":  # <-- Change to your answer
    score += 1

# Question 3
q3 = st.radio(
    "3. What's my biggest pet peeve?",
    ["People walking slow", "Chewing loudly", "Being late", "Unread notifications"],
    index=None
)
if q3 == "Chewing loudly":  # <-- Change to your answer
    score += 1

# Question 4
q4 = st.text_input("4. Bonus Question: What's one thing that always makes me smile?")

# Submit Button
if st.button("Submit Answers ✨"):
    st.divider()
    st.header(f"Your Score: {score}/{total_questions}!")
    
    if score == total_questions:
        st.balloons()
        st.success("Perfect score! You really know me well. Coffee on me next time? ☕")
    elif score >= 2:
        st.info("Not bad at all! You passed with flying colors. ")
    else:
        st.warning("Uh oh! Looks like we need to hangout more so you can study up. ")
        
    if q4:
        st.write(f"*Your answer to the bonus question:* \"{q4}\" — *(Saved!)*")