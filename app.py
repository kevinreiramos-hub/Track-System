import streamlit as st
import streamlit_authenticator as stauth
import yaml
from database.db import init_db

# Initialize DB
init_db()

# Load config
with open('config.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'], 
    config['cookie']['name'], 
    config['cookie']['key'], 
    config['cookie']['expiry_days']
)

st.title('Sales Route Management System')

# CORRECTED LOGIN LOGIC:
# 1. Call the login method without assigning it to variables
authenticator.login('Login', 'main')

# 2. Access the status and user details from session_state
if st.session_state["authentication_status"]:
    st.sidebar.write(f"Welcome, {st.session_state['name']}")
    authenticator.logout('Logout', 'sidebar')
    st.write('Please select a dashboard from the sidebar.')

elif st.session_state["authentication_status"] is False:
    st.error('Invalid credentials')

elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
