import streamlit as st
from streamlit_image_select import image_select
import os
from PIL import Image

# from streamlit_modal import Modal
from io import StringIO
from streamlit.components.v1 import html

from streamlit_option_menu import option_menu

import extra_streamlit_components as stx

from  prediction import artpredictor, load_da_model
from apis import *
    
#session vars
if 'tab_nr' not in st.session_state:
    st.session_state['tab_nr'] = 1
if 'img' not in st.session_state:
    st.session_state['img'] = None
if 'imgart' not in st.session_state:
    st.session_state['imgart'] = 3

# with st.spinner('Loading model in progress - wait for it...'):
model =  load_da_model()
    
#sidebar
st.sidebar.markdown(
    """
    <style>
         [data-testid=stSidebar] [data-testid=stImage] > img{
            text-align: center;
            display: block;
            margin-left: auto;
            --margin-right: auto;
            width: 80%;
        }
        [data-testid=stSidebar] [data-testid=stMarkdownContainer] > div > h1{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
    </style>
    """, unsafe_allow_html=True
)
st.sidebar.markdown(
    """
    <style>
        [data-testid=column] {background-color: rgba(232,242,252,255);}
    </style>
    """, unsafe_allow_html=True
)
st.sidebar.markdown(
    """
    <style>
        section > div > div > [data-testid=stVerticalBlock] {background-color: #f1f5f9; border: 1px solid rgba(232,242,252,255);}
    </style>
    """, unsafe_allow_html=True
)
st.sidebar.markdown(
    """
    <style>
        section > div > div > [data-testid=stVerticalBlock] > div > [class=stAlert] > div > div > div> div > [data-testid=stMarkdownContainer] > p {
            font-size: 20px;
            font-weight: bold;
            text-align: center !important;}
    </style>
    """, unsafe_allow_html=True
)
with st.sidebar:
    st.sidebar.image("https://lewagon.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ffe03270b-e175-406a-a223-7d362fb51bd4%2Fnest.png?table=block&id=5590833d-acb5-43ac-ba73-353ac22399d7&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=250&userId=&cache=v2", use_column_width=False)
    st.sidebar.title("Artist prediction")
    selected = option_menu("Main Menu", ["Home", 'Artist prediction', "Methodology", "Art generation", "Music generation", "References"], 
        icons=['house', 'broadcast'], menu_icon="cast", default_index=1)
    masel = selected

# Define your javascript
my_js = """
alert("Hola mundo");
"""

# Wrapt the javascript as html code
my_html = f"<script>{my_js}</script>"

st.success(masel)

if masel == 'Home':
   tab10, tab11 = st.tabs(["Artist prediction", "About"])
   with st.container():
    with tab10:
        st.write("Creation of art is among the highest form of expression of human mind and imagination. The ability of communicating imagination sets us apart from all other beings. Painting, being an expression of visual language, have attracted and connected the brilliant human minds since the dawn of civilization - from early drawings on walls of caves to paper or glass paintings of modern times, from charcoals in prehistoric times to water, oil, or pastel colors of today. We have travelled a long way, and have finally reached a stage where not only humans but computers, another brilliant creation of human minds, is creating paintings.")
        st.write("For an enthusiast of arts, identifying the paintings of her favorite artists is not that difficult, given years of careful practice and research. Given a painting, she can easily identify if it was painted by a painter she is passionate about. But can a computer do the same? Can a machine without emotions identify who the genius is behind a mindblowing painting?")
        st.write("In this part of the project, let us try to explore that direction, using techniques of deep learning.")
        st.write("Our model has been trained on the masterpieces by 11 famous artists: Vincent_van_Gogh, Edgar_Degas, Pablo_Picasso, Pierre-Auguste_Renoir, Albrecht_Dürer, Paul_Gauguin, Francisco_Goya, Rembrandt, Alfred_Sisley, Titian, Marc_Chagall")
  
if masel == 'Methodology':
    tab31, tab32, tab33 = st.tabs(["Convolutional neural network", "Transfer learning", "Variational Autoencoder"])
    with st.container():      
        with tab31:
            st.write("In deep learning, a convolutional neural network (CNN) is a class of artificial neural network most commonly applied to analyze visual imagery. CNNs use a mathematical operation called convolution in place of general matrix multiplication in at least one of their layers. They are specifically designed to process pixel data and are used in image recognition and processing.")
        with tab32:
            st.write("Transfer learning (TL) is a research problem in machine learning (ML) that focuses on applying knowledge gained while solving one task to a related task. For example, knowledge gained while learning to recognize cars could be applied when trying to recognize trucks. This topic is related to the psychological literature on transfer of learning, although practical ties between the two fields are limited. Reusing/transferring information from previously learned tasks to new tasks has the potential to significantly improve learning efficiency.")
        with tab33:
            st.write("Variational autoencoders are probabilistic generative models that require neural networks as only a part of their overall structure. The neural network components are typically referred to as the encoder and decoder for the first and second component respectively.")

if masel == 'Artist prediction':
    
    if st.session_state['tab_nr'] == 1:
        st.info("Art gallery: please choose a masterpiece for the prediction")
        
        with st.container():
            if st.button('predict the artist'):
                st.session_state['tab_nr'] = 2
                st.experimental_rerun()
        # if not (st.session_state['img'] is None):
        st.info("selected picture")
        col01, col02 = st.columns(2)
        with col01:  
            imgcontainer = st.container()
        with col02:
            lblcontainer = st.container()
            imgplaceholder = st.image
            
        radio_choice = st.radio(label='', options=["Url", "Gallery"], horizontal=True, index=1)
        if radio_choice == 'Url':
            st.session_state['imgart'] = 1
            with st.expander("Sselect a picture from the url", expanded=True):
                st.info("please paste the url in the field below")
                img1 = st.text_input('Artwork url')
                st.write('the selected masterpiece url is', img1)
                if (img1 is not None) and  (img1 != ""):
                    st.info(img1)
                    st.session_state['img'] = img1
                    st.session_state['imgart'] = 1
                    with lblcontainer:
                        st.write(f"url from internet{img1}")
                    with imgcontainer:
                        imgplaceholder(st.session_state['img'])
            
        #with st.expander("Sselect a picture from the hard drive", expanded=False):
            # st.info("firstselect picture from your hard drive")
            # uploaded_file = st.file_uploader("Choose a file")   
            # st.write(uploaded_file)
            # st.session_state['img'] = uploaded_file
            # # st.session_state['img'] = img
            # st.session_state['imgart'] = 2
            #st.write(st.session_state['img'])
            # with lblcontainer:
            #      st.write(st.session_state['img'])
            # with imgcontainer:
            #      st.image(st.session_state['img'], width=200) 
        if radio_choice == 'Gallery':
            st.session_state['imgart'] = 3         
            with st.expander("Select a picture to predict from the gallery", expanded=True):
                images = []
                for image in os.listdir("./melodic_canvases_project/data/images"):
                    if image.endswith(".jpg"):
                        images.append(f"./melodic_canvases_project/data/images/{image}")
                    else:
                        continue
                img3 = image_select(
                label="Select a picture",
                images = images,
                )
                if st.session_state['imgart'] != 1:
                    if (img3 is not None) and  (img3 != ""):
                        st.session_state['img'] = img3
                        st.session_state['imgart'] = 3
                        #st.write(st.session_state['img'])
                        with lblcontainer:
                            st.write(st.session_state['img'].split('/')[-1].replace('_', ' '))
                        with imgcontainer:
                            imgplaceholder(st.session_state['img'], width=200)     

    if st.session_state['tab_nr'] == 2:
        st.info("Prediction")
        with st.container():
            if st.button('back to the gallery'):
                st.session_state['tab_nr'] = 1
                st.experimental_rerun()
         
        col1, col2 = st.columns(2)
        with col1:
            with  st.container():      
                st.info("selected picture")
                st.image(st.session_state['img'], width=300)

        # prediction
        with col2:
            predictcontainer = st.container()
        
        with st.expander("Autobiography", expanded=True):
            apiautobiography = st.container()
        
        with st.spinner('Prediction in progress - wait for it...'):
            try:
                # model =  load_da_model()
                artist, probability = artpredictor(model, st.session_state['img'])
                # st.info(f"model-predicted artist: {artist},  prediction probability:{probability}")
                # apis info
                abiography, aimage_url = get_artist_info(artist)
                aquote = get_random_quote_by_person(artist)
                with predictcontainer:
                    st.info("prediction results:")
                    st.success(f"Predicted Artist: {artist}  \nPrediction Probability: {probability}")
                    st.info(f"original label: {st.session_state['img'].split('/')[-1].replace('_', ' ')}")
                with apiautobiography:
                    st.info(artist)
                    col21, col22 = st.columns(spec= [0.2, 0.8], gap="small")
                    with col21:
                        st.image(aimage_url, width=100)
                    with col22:
                        st.write(aquote)
                    st.info(abiography)
            except Exception as e:
                with predictcontainer:
                    st.info("prediction results:")
                    st.error(f"Error while processing the image. Please check your image and try again")
                    st.info("")
                with apiautobiography:
                    st.info("")
                    col21, col22 = st.columns(spec= [0.2, 0.8], gap="small")
                    # with col21:
                    # st.image("")
                    with col22:
                        st.write("")
                    st.info("")
                       

if masel == 'References':
   with st.container():
        st.write("1. MusicNet dataset:  https://lewagon-alumni.slack.com/archives/C05AB0ANML7/p1686750933899749")
        st.write("2. Art Images dataset: https://www.kaggle.com/datasets/thedownhill/art-images-drawings-painting-sculpture-engraving")
        st.write("3. https://www.kaggle.com/code/supratimhaldar/deepartist-identify-artist-from-art")
        st.write("4. https://www.kaggle.com/code/speedwagon/variational-autoencoder-dogs-generation")
        st.write("5. https://www.kaggle.com/code/basu369victor/generate-music-with-variational-autoencoder")

if masel == 'Art generation':
   with st.container():
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
 
if masel == 'Music generation':
   with st.container():
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")   
        # tab_options = ["Tab 1", "Tab 2"]
        # selected_tab = st.radio("Select a tab", tab_options)

        # if selected_tab == "Tab 1":
        #     st.markdown("Tab 1 content")
        #     # Add your Tab 1 content here
        # elif selected_tab == "Tab 2":
        #     st.markdown("Tab 2 content")
            
#Execute your app
#st.title("Javascript example")
#html(my_html)


#callmodal(img)
# st.write(str(img)[:100])
#st.destroyAllWindows()
#st.imshow('Final', img)
#st.image(img)
