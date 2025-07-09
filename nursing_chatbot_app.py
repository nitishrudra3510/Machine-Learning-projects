import streamlit as st

st.set_page_config(page_title="Nursing Admission Chatbot", page_icon="🤖")
st.title("🤖 Nursing College Admission Chatbot")

# Initialize session state on first load
if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.chat = ["🤖 Bot: Hello! Are you interested in admission to the Nursing College?"]

# Display chat history
for line in st.session_state.chat:
    st.markdown(line)

# Keep input box always available
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
            st.session_state.chat.append("🤖 Bot: Okay! Thank you. Reach out anytime. 😊")
            st.session_state.step = -1  # end

    # Step 2: Biology check
    elif st.session_state.step == 2:
        if "yes" in user_input:
            st.session_state.chat.append("🤖 Bot: Awesome! You're eligible. Do you want to know the fee structure?")
            st.session_state.step = 3
        else:
            st.session_state.chat.append("🤖 Bot: Biology is mandatory for admission. You're not eligible.")
            st.session_state.step = -1

    # Step 3: Fee info
    elif st.session_state.step == 3:
        if "yes" in user_input:
            st.session_state.chat.append("🤖 Bot: Fee is ₹70,000 (Tuition: ₹60K + Bus: ₹10K) in 3 installments.\nDo you want hostel/training info?")
            st.session_state.step = 4
        else:
            st.session_state.chat.append("🤖 Bot: Okay. Do you want hostel/training info?")
            st.session_state.step = 4

    # Step 4: Hostel + Training
    elif st.session_state.step == 4:
        if "yes" in user_input:
            st.session_state.chat.append("🤖 Bot: Hostel has 24x7 water, CCTV, warden. Hospital training with real patients is included.\nWant to know about scholarships?")
            st.session_state.step = 5
        else:
            st.session_state.chat.append("🤖 Bot: Alright. Want to know about scholarships?")
            st.session_state.step = 5

    # Step 5: Scholarship info
    elif st.session_state.step == 5:
        if "yes" in user_input:
            st.session_state.chat.append("🤖 Bot: Scholarships:\n- Post-Matric: ₹18k–₹23k\n- Labour Ministry: ₹40k–₹48k (for registered workers)\nWant to know eligibility?")
            st.session_state.step = 6
        else:
            st.session_state.chat.append("🤖 Bot: No worries. Want to know eligibility?")
            st.session_state.step = 6

    # Step 6: Eligibility
    elif st.session_state.step == 6:
        if "yes" in user_input:
            st.session_state.chat.append("🤖 Bot: Eligibility:\n- 12th with Biology\n- PNT Exam pass\n- Age 17–35\nThanks for chatting! 😊")
            st.session_state.step = -1
        else:
            st.session_state.chat.append("🤖 Bot: Okay! Feel free to ask anytime later. 👋")
            st.session_state.step = -1

    # Step -1: End of chat
    elif st.session_state.step == -1:
        st.session_state.chat.append("🤖 Bot: The conversation is complete. Refresh the page to start over.")

    # Rerun to refresh chat display and input box
    
    st.rerun()