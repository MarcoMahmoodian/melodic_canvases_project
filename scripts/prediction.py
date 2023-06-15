import tensorflow.keras as keras
import streamlit as st
import keras.utils as image
import imageio.v2 as imageio
import cv2
import numpy as np
import matplotlib.pyplot as plt

from keras.models import load_model
from keras.utils.data_utils import get_file

# Load the saved model
@st.cache_resource(ttl=None)
def load_da_model():
    #model = keras.models.load_model('./models/final_model_cnn_11.h5')
    # Load the locally saved model
    #model = keras.models.load_model('../models/final_model_cnn_11.h5')
    # Alternatively load the model from GCP bucket
    murl = 'gs://art_classification_model/final_model_cnn_11.h5'
    model = load_model(murl)
    # check if the model was actually loaded
    # model.summary()
    return model

def artpredictor(model, url):
    # model =  load_da_model()
    n_classes = 11
    train_input_shape = (224, 224, 3)
    labels = {0: 'Vincent_van_Gogh',
          1: 'Edgar_Degas',
          2: 'Pablo_Picasso',
          3: 'Pierre-Auguste_Renoir',
          4: 'Albrecht_Dürer',
          5: 'Paul_Gauguin',
          6: 'Francisco_Goya',
          7: 'Rembrandt',
          8: 'Alfred_Sisley',
          9: 'Titian',
          10: 'Marc_Chagall'}

    #url = 'https://www.gpsmycity.com/img/gd/2081.jpg' # titian
    #url = 'https://s3-eu-west-1.amazonaws.com/kooness-stage-bucket/uploads/archive/Pablo_Picasso__Head_of_a_woman.jpg' #picasso rare
    #url = 'https://cdn.shopify.com/s/files/1/1551/3581/files/Artist_Thumbnail_-__0004_PICASSO_b1073_jacqueline_in_a_straw_hat_lipic1073sc_un1.jpg?v=1659989054`'
    #url = '../raw_data/images/validation_set/painting/0124.jpg'
    #url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Fragonard%2C_The_Reader.jpg/800px-Fragonard%2C_The_Reader.jpg'
    #url = 'https://de.artsdot.com/ADC/Art-ImgScreen-2.nsf/O/A-5ZKC9M/$FILE/Edgar-degas-the-star.Jpg'

    sample_image = imageio.imread(url)
    sample_image = cv2.resize(sample_image, dsize=train_input_shape[0:2], )
    sample_image = image.img_to_array(sample_image)
    sample_image /= 255.
    sample_image = np.expand_dims(sample_image, axis=0)

    prediction = model.predict(sample_image)
    prediction_probability = np.amax(prediction)
    prediction_idx = np.argmax(prediction)
    predicted_artist = labels[prediction_idx].replace('_', ' ')
    prediction_probability = round(prediction_probability*100, 2)
    # plt.imshow(imageio.imread(url))
    # plt.title(f'{predicted_artist}, {prediction_probability}%')
    # plt.axis('off')
    # plt.savefig(f'../output/example_prediction_{predicted_artist}_{prediction_probability}.png')
    # plt.show()
    #print(predicted_artist)
    #print(prediction_probability)
    return predicted_artist, prediction_probability

# artist, prob = artpredictor("blablabla")
# print(artist)
