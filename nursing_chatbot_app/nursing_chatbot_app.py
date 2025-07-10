import streamlit as st

st.set_page_config(page_title="Nursing Admission Chatbot")
st.title("Nursing College Admission Chatbot")

# Alias session_state with a custom name
chatflow = st.session_state

if "step" not in chatflow:
    chatflow.step = 1
    chatflow.chat = ["Bot: Hello! Are you interested in admission to the Nursing College?"]

for line in chatflow.chat:
    st.markdown(line)

user_input = st.text_input("You:", key=chatflow.step)

if user_input:
    user_input = user_input.lower()
    chatflow.chat.append(f"You: {user_input}")

    if chatflow.step == 1:
        if "yes" in user_input:
            chatflow.chat.append("Bot: Great! Have you studied Biology in 12th grade?")
            chatflow.step = 2
        else:
            chatflow.chat.append("Bot: No problem. Thank you! If you need assistance later, feel free to contact us.")
            chatflow.step = -1

    elif chatflow.step == 2:
        if "yes" in user_input:
            chatflow.chat.append("Bot: You're eligible for B.Sc Nursing. Do you want to know the fee structure?")
            chatflow.step = 3
        else:
            chatflow.chat.append("Bot: Biology in 12th is mandatory. You're not eligible.")
            chatflow.step = -1

    elif chatflow.step == 3:
        if "yes" in user_input:
            chatflow.chat.append("Bot: Fee Structure:\n- Tuition: ₹60,000\n- Bus: ₹10,000\nTotal: ₹70,000 in 3 parts.\nWould you like to know about hostel and training?")
            chatflow.step = 4
        else:
            chatflow.chat.append("Bot: Alright. Would you like to know about hostel and training?")
            chatflow.step = 4

    elif chatflow.step == 4:
        if "yes" in user_input:
            chatflow.chat.append("Bot: Hostel Facilities:\n- Water & electricity 24x7\n- CCTV\n- Warden present\nAlso includes hospital training with real patients.\nWant to know about college location?")
            chatflow.step = 5
        else:
            chatflow.chat.append("Bot: Okay. Want to know about college location?")
            chatflow.step = 5

    elif chatflow.step == 5:
        if "yes" in user_input:
            chatflow.chat.append("Bot: The college is in Delhi. Want to know about recognition and accreditation?")
            chatflow.step = 6
        else:
            chatflow.chat.append("Bot: Okay. Want to know about recognition and accreditation?")
            chatflow.step = 6

    elif chatflow.step == 6:
        if "yes" in user_input:
            chatflow.chat.append("Bot: Recognized by Indian Nursing Council (INC), Delhi.\nWant to know clinical training locations?")
            chatflow.step = 7
        else:
            chatflow.chat.append("Bot: Okay. Want to know clinical training locations?")
            chatflow.step = 7

    elif chatflow.step == 7:
        if "yes" in user_input:
            chatflow.chat.append("Bot: Clinical Training at:\n- District Hospital (Backundpur)\n- Community Health Centers\n- Regional Hospital (Chartha)\n- Ranchi Neurosurgery Hospital\nWant scholarship info?")
            chatflow.step = 8
        else:
            chatflow.chat.append("Bot: Okay. Want scholarship info?")
            chatflow.step = 8

    elif chatflow.step == 8:
        if "yes" in user_input:
            chatflow.chat.append("Bot: Scholarships:\n- Post-Matric: ₹18k–₹23k\n- Labour Ministry: ₹40k–₹48k (requires registration)\nWant to know about seat availability?")
            chatflow.step = 9
        else:
            chatflow.chat.append("Bot: Okay. Want to know about seat availability?")
            chatflow.step = 9

    elif chatflow.step == 9:
        if "yes" in user_input:
            chatflow.chat.append("Bot: Total 60 seats in B.Sc Nursing.\nWant to know eligibility again?")
            chatflow.step = 10
        else:
            chatflow.chat.append("Bot: Okay. Want to know eligibility again?")
            chatflow.step = 10

    elif chatflow.step == 10:
        if "yes" in user_input:
            chatflow.chat.append("Bot: Eligibility:\n- Biology in 12th\n- PNT Exam pass\n- Age: 17 to 35\nThank you for chatting with us.")
        else:
            chatflow.chat.append("Bot: Thank you! Have a nice day.")
        chatflow.step = -1

    elif chatflow.step == -1:
        chatflow.chat.append("Bot: Chat has ended. Please refresh the page to restart.")

    st.rerun()