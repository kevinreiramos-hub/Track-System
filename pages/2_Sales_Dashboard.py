import streamlit as st
from streamlit_geolocation import streamlit_geolocation
from database.db import Session, GPSLog
import datetime

st.title('Sales Person View')
location = streamlit_geolocation()

if location:
    lat, lng = location['latitude'], location['longitude']
    st.write(f'Current GPS: {lat}, {lng}')
    
    if st.button('Log Position'):
        session = Session()
        new_log = GPSLog(username='sales1', lat=lat, lng=lng, timestamp=datetime.datetime.now())
        session.add(new_log)
        session.commit()
        st.success('Location logged!')
