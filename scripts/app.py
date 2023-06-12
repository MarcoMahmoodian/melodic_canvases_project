import streamlit as st
from streamlit_image_select import image_select
import os


'''
# Final Project
'''


images = []
for image in os.listdir("../melodic_canvases_project/data/images"):
    if image.endswith(".jpg"):
        images.append(f"../melodic_canvases_project/data/images/{image}")
    else:
        continue
img = image_select(
    label="Select a cat",
    images = images,captions=["A", "B", "C", "D", "E", "F", "G", "H", "I", "Q"]
)


    # images=[
    #     "../melodic_canvases_project/data/images/Camille_Pissarro_22.jpg",
    #     "../melodic_canvases_project/data/images/Claude_Monet_57.jpg",
    # ],


st.write(str(img)[:100])
