import streamlit as st
from PIL import Image
import random
import pandas as pd



## dice
# Functions
def dice(input_face_num):
    return random.randint(1, input_face_num)


roll_buttom = st.button('サイコロを振る')

if roll_buttom:
    value = dice(6)
    image = Image.open(f'6dice_{value}.png')
    st.image(image)
