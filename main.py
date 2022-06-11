import streamlit as st
from PIL import Image
import random


## dice
# Functions
def dice(input_face_num):
    if input_face_num == 24:
        return random.randint(1, 24)
    else:
        return random.randint(1, input_face_num)

if st.button('6面体サイコロを振る'):
     dice6 = dice(6)
     st.write(dice6)

if st.button('24面体サイコロを振る'):
     dice24 = dice(24)
     st.write(dice24)