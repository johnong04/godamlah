import streamlit as st

from pages import (
    identity,
    login,
    loginSuccess,
    signup,
    handsign,
    upscale_1,
    results_1,
    bank_statement,
    upscale_2,
    results_2,
    selfie
)

st.set_page_config(
    page_title="SwiftAuth",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "identity"
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None
if "upscaled" not in st.session_state:
    st.session_state.upscaled = False
if "upscaled_image" not in st.session_state:
    st.session_state.upscaled_image = False
if "upscaled_image_path" not in st.session_state:
    st.session_state.upscaled_image_path = False
if "selfied" not in st.session_state:
    st.session_state.selfied = False
if "captured_image" not in st.session_state:
    st.session_state.captured_image = None
if "passport_info" not in st.session_state:
    st.session_state.passport_info = ""
if "statement_info" not in st.session_state:
    st.session_state.statement_info = ""
if "verification_complete" not in st.session_state:
    st.session_state.verification_complete = False
if "user_email" not in st.session_state:
    st.session_state.user_email = None


# Main app logic
def main():
    if st.session_state.page == "login":
        login.show()
    if st.session_state.page == "loginSuccess":
        loginSuccess.show()
    elif st.session_state.page == "signup":
        signup.show()
    elif st.session_state.page == "handsign":
        handsign.show()
    elif st.session_state.page == "identity":
        identity.show()
    elif st.session_state.page == "upscale_1":
        upscale_1.show()
    elif st.session_state.page == "selfie":
        selfie.show()
    elif st.session_state.page == "results_1":
        results_1.show()
    elif st.session_state.page == "bank_statement":
        bank_statement.show()
    elif st.session_state.page == "upscale_2":
        upscale_2.show()
    elif st.session_state.page == "results_2":
        results_2.show()

    # Footer with dark theme
    st.markdown(
        """
    <div style='position: fixed; left: 0; bottom: 0; width: 100%; background-color: #1E1E1E; padding: 10px 0;'>
        <div style='max-width: 800px; margin: 0 auto; text-align: center;'>
            <p style='color: #888888; font-size: 12px; margin: 0;'>© 2024 SwiftAuth v1.0.0 | User Authentication Made Easy</p>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
