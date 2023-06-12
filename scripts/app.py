import streamlit as st
from streamlit_image_select import image_select
import os

from streamlit_modal import Modal

from streamlit_option_menu import option_menu


from streamlit.components.v1 import html

if "selected_tab" not in st.session_state:
        st.session_state.selected_tab = 0
    
#sidebar
st.sidebar.title("Menu")
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Artist prediction', "Methodology", "Art generation", "Music generation"], 
        icons=['house', 'broadcast'], menu_icon="cast", default_index=1)
    masel = selected
'''

'''
# def callmodal(pimg):
#     modal = Modal(key="Demo Key",title="selected image")
#     open_modal = st.button(key="123", label='button')
#     #open_modal = pimg is not None
#     if open_modal:
#         with modal.container():
#             st.markdown(st.image(pimg))
# show images

# blank html to be used later 

# Define your javascript
my_js = """
alert("Hola mundo");
"""

# Wrapt the javascript as html code
my_html = """

"""

st.write(masel)

if masel == 'Home':
   with st.container():
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

if masel == 'Artist prediction':
    tab1, tab2 = st.tabs(["Pictures", "Predictions"])
    #selected_tab = st.radio("Select a tab", st.tabs, index=st.session_state.selected_tab)

    # Update the selected tab index
    #st.session_state.selected_tab = st.tabs.index(selected_tab)
    
    with tab1:
        tab1.subheader("Choosing data for prediction")
        with st.container():
            #if st.button('predict the author'):
                # routine for the prediction
            st.button("redict the author", on_click=lambda: st.markdown("Switching to Tab 2...") or st.experimental_rerun() or st.markdown("Tab 2 content"))
            
        with st.expander("Sselect a picture to predict", expanded=True):
            images = []
            for image in os.listdir("../melodic_canvases_project/data/images"):
                if image.endswith(".jpg"):
                    images.append(f"../melodic_canvases_project/data/images/{image}")
                else:
                    continue
            img = image_select(
            label="Select a picture",
            images = images,
            )
            st.write(img)

    with tab2:
        tab2.subheader("Prediction")
        st.write("selected picture")
        st.image(img, width=600)

if masel == 'Methodology':
   with st.container():
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

if masel == 'Art generation':
   with st.container():
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
 
if masel == 'Music generation':
   with st.container():
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")   
    

# Execute your app
#st.title("Javascript example")
#html(my_html)


#callmodal(img)
# st.write(str(img)[:100])
#st.destroyAllWindows()
#st.imshow('Final', img)
#st.image(img)
