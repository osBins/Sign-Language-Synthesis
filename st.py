import streamlit as st
import main
import pyperclip

sigml = ""

def copySigml():
    with open("SiGML-output.sigml", 'r') as f:
        sigml = f.read()
        pyperclip.copy(sigml)

st.title("Automated System for Generation of Avatar for Indian Sign Language using HamNoSys and SiGML")
# video_file = open('./myvideo.mp4', 'rb')
uploadedVideo = st.file_uploader('Upload Video')

if uploadedVideo is not None:
    print(uploadedVideo.name)
    bytes_data = uploadedVideo.getvalue()
    st.video(bytes_data)
    st.button("Generate ISL", on_click=main.convert(uploadedVideo.name))
    st.button("Copy SiGML", on_click=copySigml)


webPlayerHTMLFile = open('./cwasa.html', 'r')
cwasaHTML = webPlayerHTMLFile.read()
st.components.v1.html(cwasaHTML, width=None, height=500)

webPlayerHTMLFile.close()