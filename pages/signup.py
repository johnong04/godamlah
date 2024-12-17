import streamlit as st

def show():
    st.title("Sign Up")

    email = st.text_input("Email")
    password = st.text_input("Password", type='password')

    if st.button("Sign Up"):
        if email and password:  # Basic validation
            st.session_state.user_email = email
            st.session_state.page = "identity"
            st.rerun()
        else:
            st.error("Please fill in all fields")
