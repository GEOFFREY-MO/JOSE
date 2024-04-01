import PIL
import streamlit as st 
from tensorflow.keras.preprocessing import image
import numpy as np

def get_model_output(model , processor) : 

    image = PIL.Image.open('Uploaded_file.jpg')

    inputs = processor(images = image , return_tensors = 'pt')
    outputs = model(**inputs)
    results = processor.post_process_object_detection(
        outputs , 
        target_sizes = torch.tensor([image.size[: : -1]]) , 
        threshold = 0.9)[0]

    if len(results['labels']) == 0 : return False 
    for label in results['labels'] : 

        if model.config.id2label[label.item()] in [
            'cow' , 'buffalo' 
        ] : return True 

    return False


def preprocess_image(image_path) : 

    img = image.load_img(image_path , target_size = (224 , 224)) 
    
    img_array = image.img_to_array(img) 
    img_array = np.expand_dims(img_array , axis = 0) 
    
    return img_array

def get_label(classifier_model , bb_model , processor) : 

    c_label = None
    counter = 0
    cattles = True

    if get_model_output(bb_model , processor) : 


        preprocessed_image = preprocess_image('Uploaded_file.jpg')
        predictions = classifier_model.predict(preprocessed_image)

        if predictions[0][0] >= 0.25 : return 0
        return 1
    return 2
