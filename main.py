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

roll_6 = "" 
    
if 'exp01' not in st.session_state:
    st.session_state.exp01 = 0

exp01_buttom = st.button('６面体サイコロを振る')

if exp01_buttom and st.session_state.exp01 == 0:
    roll_6 = dice(6)
    st.session_state.exp01 = roll_6

st.write(roll_6)
    
