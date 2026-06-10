import streamlit as st
import streamlit_authenticator as stauth
import yaml
from database.db import init_db

init_db()

with open('config.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'], config['cookie']['name'], 
    config['cookie']['key'], config['cookie']['expiry_days']
)

st.title('Sales Route Management System')
name, status, username = authenticator.login('Login', 'main')

if status:
    st.sidebar.write(f'Welcome, {name}')
    authenticator.logout('Logout', 'sidebar')
    st.write('Please select a dashboard from the sidebar.')
elif status == False:
    st.error('Invalid credentials')
