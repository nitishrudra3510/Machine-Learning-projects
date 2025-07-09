import streamlit as st

st.set_page_config(page_title="Nursing Admission Chatbot", page_icon="🤖")
st.title("🤖 Nursing College Admission Chatbot")

def respond(user_input):
    user_input = user_input.lower()

    if "biology" in user_input and "no" in user_input:
        return "Biology is mandatory for B.Sc Nursing admission. You are not eligible."
    elif "biology" in user_input and "yes" in user_input:
        return ("Great! You're eligible.\n\n"
            "B.Sc Nursing is a full-time, 4-year program with theory and hospital training.\n"
                "Do you want to know about the fee structure?")
    elif "fee" in user_input or "fees" in user_input:
        return ("Fee Structure:\n- Tuition: ₹60,000\n- Bus: ₹10,000\n"
                "Total: ₹70,000 (Installments: ₹30K, ₹20K, ₹20K)")
    elif "hostel" in user_input or "training" in user_input:
        return ("Hostel has 24x7 water, electricity, CCTV, warden.\n"
                "Hospital training with real patients is included.")
    elif "location" in user_input:
        return "The college is located in Delhi. Want to know about the surrounding area?"
    elif "recognition" in user_input or "accreditation" in user_input:
        return "The college is recognized by the Indian Nursing Council (INC), Delhi."
    elif "clinical" in user_input:
        return ("Clinical Training Locations:\n- District Hospital (Backundpur)\n"
                "- Community Health Centers\n- Regional Hospital (Chartha)\n"
                "- Ranchi Neurosurgery Hospital (Jharkhand)")
    elif "scholarship" in user_input:
        return ("Scholarships:\n- Post-Matric: ₹18k–₹23k\n"
                "- Labour Ministry: ₹40k–₹48k (for registered workers)")
    elif "seats" in user_input:
        return "There are a total of 60 seats available."
    elif "eligible" in user_input:
        return ("Eligibility:\n- Biology in 12th\n- Pass PNT Exam\n- Age: 17 to 35")
    elif "hi" in user_input or "hello" in user_input:
        return "Hello! Are you interested in admission to the Nursing College?"
    elif "no" in user_input:
        return "Okay! Thank you. Reach out anytime. 😊"
    elif "yes" in user_input:
        return "Great! Have you studied Biology in 12th grade?"
    else:
        return "I can help with Nursing admission info like fees, eligibility, scholarships, etc."

# Streamlit UI
st.markdown("Type your question below 👇")

user_query = st.text_input("You:", "")

if user_query:
    response = respond(user_query)
    st.markdown(f"**🤖 Bot:** {response}")