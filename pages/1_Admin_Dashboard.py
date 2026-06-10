import streamlit as st
import folium
from streamlit_folium import st_folium
from database.db import Session, GPSLog

st.title('Admin: Live Sales Tracker')
session = Session()
logs = session.query(GPSLog).order_by(GPSLog.timestamp.desc()).limit(10).all()

m = folium.Map(location=[14.5995, 120.9842], zoom_start=13)
for log in logs:
    folium.Marker([log.lat, log.lng], popup=log.username).add_to(m)

st_folium(m, width=800, height=400)
