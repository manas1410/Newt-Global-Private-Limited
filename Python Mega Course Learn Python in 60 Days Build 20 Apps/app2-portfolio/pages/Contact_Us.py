import streamlit as st

from send_email import send_email

st.header("Contact Information ")

with st.form(key="email_form"):
    username=st.text_input("Your Email Address")

    raw_message=st.text_area("your Message here!!")
    message=f"""New Message from {username}" \
            {raw_message} """
    Button = st.form_submit_button("Submit")
    if Button:
        print("i am pressed")
        send_email(message)
        st.info("email is sent successfully")