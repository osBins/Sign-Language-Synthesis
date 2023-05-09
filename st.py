import streamlit as st
import main


# video_file = open('./myvideo.mp4', 'rb')
uploadedVideo = st.file_uploader('Upload Video')

if uploadedVideo is not None:
    print(uploadedVideo.name)
    bytes_data = uploadedVideo.getvalue()
    st.video(bytes_data)
    st.button("Generate ISL", main.convert(uploadedVideo.name))


webPlayerHTMLFile = open('./cwasa.html', 'r')
cwasaHTML = webPlayerHTMLFile.read()
st.components.v1.html(cwasaHTML, width=None, height=500)

webPlayerHTMLFile.close()