import streamlit as st

st.set_page_config(page_title="Nursing Admission Chatbot", page_icon="🤖")
st.title("🤖 Nursing College Admission Chatbot")

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 1
    st.session_state.chat = ["🤖 Bot: Hello! Are you interested in admission to the Nursing College?"]

# Display conversation history
for line in st.session_state.chat:
    st.markdown(line)

# Input
user_input = st.text_input("You:")

if user_input:
    st.session_state.chat.append(f"**You:** {user_input}")
    user_input_lower = user_input.lower()

    # Step 1: Ask for admission interest
    if st.session_state.step == 1:
        if "yes" in user_input_lower:
            bot_reply = "Great! Have you studied Biology in 12th grade?"
            st.session_state.step = 2
        else:
            bot_reply = "Okay! Thank you. Reach out anytime. 😊"
            st.session_state.step = 0  # end
        st.session_state.chat.append(f"🤖 Bot: {bot_reply}")

    # Step 2: Check Biology
    elif st.session_state.step == 2:
        if "yes" in user_input_lower:
            bot_reply = ("Awesome! You are eligible for B.Sc Nursing.\n"
                         "Do you want to know the fee structure?")
            st.session_state.step = 3
        else:
            bot_reply = "Biology is mandatory for B.Sc Nursing admission. You are not eligible."
            st.session_state.step = 0
        st.session_state.chat.append(f"🤖 Bot: {bot_reply}")

    # Step 3: Fee Structure
    elif st.session_state.step == 3:
        if "yes" in user_input_lower:
            bot_reply = ("Fee Structure:\n- Tuition: ₹60,000\n- Bus: ₹10,000\n"
                         "Total: ₹70,000 (Installments: ₹30K, ₹20K, ₹20K)\n"
                         "Do you want to know about hostel & training?")
            st.session_state.step = 4
        else:
            bot_reply = "Okay! Let me know if you want more info."
        st.session_state.chat.append(f"🤖 Bot: {bot_reply}")

    # Step 4: Hostel Info
    elif st.session_state.step == 4:
        if "yes" in user_input_lower:
            bot_reply = ("🏠 Hostel has 24x7 water & electricity, CCTV, warden.\n"
                         "🏥 Hospital training with real patients is included.\n"
                         "Do you want to know about scholarships?")
            st.session_state.step = 5
        else:
            bot_reply = "Alright. Do you want to know about scholarships?"
            st.session_state.step = 5
        st.session_state.chat.append(f"🤖 Bot: {bot_reply}")

    # Step 5: Scholarships
    elif st.session_state.step == 5:
        if "yes" in user_input_lower:
            bot_reply = ("🎓 Scholarships:\n- Post-Matric: ₹18k–₹23k\n"
                         "- Labour Ministry: ₹40k–₹48k (for registered workers)\n"
                         "Do you want to know the eligibility criteria?")
            st.session_state.step = 6
        else:
            bot_reply = "No problem. Do you want to know the eligibility criteria?"
            st.session_state.step = 6
        st.session_state.chat.append(f"🤖 Bot: {bot_reply}")

    # Step 6: Eligibility Summary
    elif st.session_state.step == 6:
        if "yes" in user_input_lower:
            bot_reply = ("✅ Eligibility:\n- 12th with Biology\n- PNT Exam passed\n- Age: 17–35\n"
                         "Thanks for chatting! 😊")
        else:
            bot_reply = "Okay, feel free to ask anything later. 😊"
        st.session_state.step = 0
        st.session_state.chat.append(f"🤖 Bot: {bot_reply}")