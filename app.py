import streamlit as st 
import os 
import zipfile

from tensorflow.keras.models import load_model


from helper import get_label
from transformers import DetrImageProcessor, DetrForObjectDetection

with zipfile.ZipFile('fmd_detection_model.zip' , "r") as z:
    z.extractall(".")

def prediction() : 

    processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50", revision="no_timm")
    bb_model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50", revision="no_timm")

    model = load_model('fmd_detection_model.h5')

    images = st.sidebar.file_uploader('Upload the Image' , type = ['jpg' , 'jpeg' , 'png' , 'webp'] , accept_multiple_files = True)

    if images : 

        for image_ in images :

            with open('Uploaded_file.jpg' , 'wb') as img : img.write(image_.getbuffer())
            
            label = get_label(model  , bb_model , processor)

            if label == 0 : 
                st.write('The cattle in the Image have FMD')
                st.image('Uploaded_file.jpg')
            elif label == 1 : 
                st.write('The cattle in the image does not have FMD')
                st.image('Uploaded_file.jpg')
            else : 
                st.write('The porvided image is not of a cattle')
                st.image('Uploaded_file.jpg')
                
def home() : st.markdown(open('text.txt').read())


usernames = {
    'Ayush' : 'Joseph'
}


login_container = st.empty()

lc = login_container.container(border = True)
username = lc.text_input('Username') 
password = lc.text_input('Password')

if username != '' and password != '' : 

    if username in usernames.keys() and password == usernames[username] : 
        login_container.empty()
        option = st.sidebar.selectbox(
        'Go to' , 
        [ 
            'Home' , 
            'Prediction'
        ])
        if option == 'Home' : home()
        elif option == 'Prediction' : prediction()
        

    else : st.write('Invalid Username or Pasword')





