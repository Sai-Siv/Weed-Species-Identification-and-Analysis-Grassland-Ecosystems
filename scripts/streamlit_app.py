import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import os

# Load the trained model
MODEL_PATH = r"C:\Users\saisi\Downloads\Weed-Species-Identification-and-Analysis-Grassland-Ecosystems\models\vgg16_epochs_10.h5"
model = load_model(MODEL_PATH)

# Define class names (update as per your dataset)
class_names = ['CELOSIA_ARGENTEA_L', 'CROWFOOT_GRASS', 'PURPLE_CHLORIS']

st.title('Weed Species Identification')
st.write('Upload an image of a grassland weed to identify its species.')

uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert('RGB')
    st.image(img, caption='Uploaded Image', use_column_width=True)
    st.write('')
    st.write('Classifying...')

    # Preprocess the image
    img = img.resize((224, 224))
    x = image.img_to_array(img)
    x = x / 255.0
    x = np.expand_dims(x, axis=0)

    # Predict
    preds = model.predict(x)
    pred_class = class_names[np.argmax(preds)]
    confidence = np.max(preds)

    st.write(f'**Prediction:** {pred_class}')
    st.write(f'**Confidence:** {confidence:.2f}')
