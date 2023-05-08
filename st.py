import streamlit as st
import pandas as pd

st.write("YOLO")


video_file = open('./myvideo.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

webPlayerHTMLFile = open('./cwasa.html', 'r')
cwasaHTML = webPlayerHTMLFile.read()

st.components.v1.html(cwasaHTML, width=None, height=500)
