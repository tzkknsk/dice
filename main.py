import streamlit as st
from PIL import Image
import random
import pandas as pd


## ---------- 被験者情報の入力 ---------- ##
answer_dict = {}

ID = st.text_input('被験者番号を入力してください（半角数字）')
answer_dict["ID"] = ID
st.write("")
st.write("")

date_01 = "2022年6月13日"
date_02 = "2022年6月14日"
date = st.radio(
    "実験実施日を選択してください",
    (date_01, date_02)
)

if date == date_01:
    answer_dict["date"] = 20220613
else:
    answer_dict["date"] = 20220614

st.write("")
st.write("")


## dice
# Functions
def dice(input_face_num):
    if input_face_num == 24:
        return random.randint(1, 24)
    else:
        return random.randint(1, input_face_num)

roll_buttom = st.button('サイコロを振る')

roll_6b = 0
roll_6g = 0
roll_6e = 0
roll_6g_color = ""
roll_6e_color = ""
roll_6g_color_en = ""
roll_6e_color_en = ""

if roll_buttom:
    roll_6b = dice(6)
    roll_6g = dice(6)
    roll_6e = dice(6)


#### 【第１部 ― １】
st.header("【第１部 ― １】")
## サイコロ β
st.subheader(f"サイコロ β の出目は {roll_6b} です")
## サイコロ γ
if roll_6g != 0 and roll_6g % 2 == 0:
    roll_6g_color = "緑"
    roll_6g_color_en = "Green"
elif roll_6g != 0 and roll_6g % 2 == 1:
    roll_6g_color = "赤"
    roll_6g_color_en = "Red"

st.subheader(f"サイコロ γ の出目は {roll_6g} です（{roll_6g_color}）")

#### 【第１部 ― 2】
st.header("【第１部 ― ２】")
## サイコロ ε
if roll_6e != 0 and roll_6e % 2 == 0:
    roll_6e_color = "緑"
    roll_6e_color_en = "Green"
elif roll_6e != 0 and roll_6e % 2 == 1:
    roll_6e_color = "赤"
    roll_6e_color_en = "Red"

st.subheader(f"サイコロ ε の出目は {roll_6e} です（{roll_6e_color}）")

st.write("")
st.write("")

## ---------- 回答結果の出力 ---------- ##
answer_dict["dice_beta"]    = roll_6b
answer_dict["dice_gamma"]   = roll_6g
answer_dict["dice_epsilon"] = roll_6e
answer_dict["Q1-1"]         = roll_6g_color_en
answer_dict["Q1-2"]         = roll_6e_color_en


def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

output_dict={}
for k,v in answer_dict.items():   # 一度pd.Seriesに変換
    output_dict[k]=pd.Series(v)

df = pd.DataFrame(output_dict)

def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv(index=False).encode('utf-8')

csv = convert_df(df)

st.download_button(
     label="サイコロの出目を出力(csv)",
     data=csv,
     file_name= f'DiceRoll_{ID}.csv',
     mime='text/csv',
 )
