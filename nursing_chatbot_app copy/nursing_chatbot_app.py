import streamlit as st

st.set_page_config(page_title="Nursing Admission Chatbot", page_icon="🤖")
st.title("🤖 Nursing College Admission Chatbot")

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.chat = ["🤖 Bot: Hello! Are you interested in admission to the Nursing College?"]

# Display previous conversation
for line in st.session_state.chat:
    st.markdown(line)

# Input for current turn
user_input = st.text_input("You:", key=st.session_state.step)

if user_input:
    user_input = user_input.lower()
    st.session_state.chat.append(f"**You:** {user_input}")

    # Step 1: Admission interest
    if st.session_state.step == 1:
        if "yes" in user_input:
            st.session_state.chat.append("🤖 Bot: Great! Have you studied Biology in 12th grade?")
            st.session_state.step = 2
        else:
            st.session_state.chat.append("🤖 Bot: No problem. Thank you! If you ever need assistance with admission, feel free to contact us. 🙏")
            st.session_state.step = -1

    # Step 2: Biology check
    elif st.session_state.step == 2:
        if "yes" in user_input:
            st.session_state.chat.append("🤖 Bot: Awesome! You're eligible for B.Sc Nursing. Do you want to know the fee structure?")
            st.session_state.step = 3
        else:
            st.session_state.chat.append("🤖 Bot: Biology in 12th is mandatory for B.Sc Nursing. You're not eligible.")
            st.session_state.step = -1

    # Step 3: Fee Structure
    elif st.session_state.step == 3:
        if "yes" in user_input:
            st.session_state.chat.append("🤖 Bot: Fee Structure:\n- Tuition: ₹60,000\n- Bus: ₹10,000\nTotal: ₹70,000 (Installments: ₹30K, ₹20K, ₹20K)\nWould you like to know about hostel & training facilities?")
            st.session_state.step = 4
        else:
            st.session_state.chat.append("🤖 Bot: No worries. Would you like to know about hostel & training facilities?")
            st.session_state.step = 4

    # Step 4: Hostel & Training Facilities
    elif st.session_state.step == 4:
        if "yes" in user_input:
            st.session_state.chat.append("🤖 Bot:\n🏠 Hostel Facilities:\n- 24x7 water & electricity\n- CCTV surveillance\n- On-site warden\n🏥 Hospital training is included, where students will work with real patients.\nWould you like to know about college location?")
            st.session_state.step = 5
        else:
            st.session_state.chat.append("🤖 Bot: Okay. Would you like to know about college location?")
            st.session_state.step = 5

    # Step 5: College Location
    elif st.session_state.step == 5:
        if "yes" in user_input:
            st.session_state.chat.append("🤖 Bot: The college is located in Delhi. Would you like to know about recognition and accreditation?")
            st.session_state.step = 6
        else:
            st.session_state.chat.append("🤖 Bot: Alright. Would you like to know about recognition and accreditation?")
            st.session_state.step = 6

    # Step 6: Recognition
    elif st.session_state.step == 6:
        if "yes" in user_input:
            st.session_state.chat.append("🤖 Bot: The college is recognized by the Indian Nursing Council (INC), Delhi. Want to know about clinical training locations?")
            st.session_state.step = 7
        else:
            st.session_state.chat.append("🤖 Bot: Okay. Want to know about clinical training locations?")
            st.session_state.step = 7

    # Step 7: Clinical Training Locations
    elif st.session_state.step == 7:
        if "yes" in user_input:
            st.session_state.chat.append("🤖 Bot: Clinical Training happens at:\n- District Hospital (Backundpur)\n- Community Health Centers\n- Regional Hospital (Chartha)\n- Ranchi Neurosurgery & Allied Science Hospital (Jharkhand)\nWould you like to know about scholarships?")
            st.session_state.step = 8
        else:
            st.session_state.chat.append("🤖 Bot: Alright. Would you like to know about scholarships?")
            st.session_state.step = 8

    # Step 8: Scholarships
    elif st.session_state.step == 8:
        if "yes" in user_input:
            st.session_state.chat.append("🤖 Bot:\n🎓 Available Scholarships:\n- Government Post-Matric Scholarship: ₹18,000 – ₹23,000\n- Labour Ministry Scholarship: ₹40,000 – ₹48,000 (requires labour registration)\nWould you like to know about total seats?")
            st.session_state.step = 9
        else:
            st.session_state.chat.append("🤖 Bot: Okay. Would you like to know about total seats?")
            st.session_state.step = 9

    # Step 9: Seats Available
    elif st.session_state.step == 9:
        if "yes" in user_input:
            st.session_state.chat.append("🤖 Bot: There are a total of 60 seats available in the B.Sc Nursing program.\nWould you like to know the eligibility criteria again?")
            st.session_state.step = 10
        else:
            st.session_state.chat.append("🤖 Bot: Alright. Would you like to know the eligibility criteria?")
            st.session_state.step = 10

    # Step 10: Eligibility Criteria
    elif st.session_state.step == 10:
        if "yes" in user_input:
            st.session_state.chat.append("🤖 Bot: Eligibility Criteria:\n- Biology in 12th grade\n- Must pass the PNT Exam\n- Age: 17 to 35 years\n\nThanks for chatting! 🙏")
        else:
            st.session_state.chat.append("🤖 Bot: No problem. Thank you! If you ever need assistance, feel free to ask. 🙏")
        st.session_state.step = -1  # End

    elif st.session_state.step == -1:
        st.session_state.chat.append("🤖 Bot: Chat has ended. Please refresh the page to start again.")

    # Rerun the app to show the next input box
    st.rerun()