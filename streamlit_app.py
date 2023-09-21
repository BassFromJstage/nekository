# Streamlitライブラリをインポート
import streamlit as st
import random

st.title('2023最新の幸運を入手')

if st.button('抽選'):
    results=["大吉","中吉","小吉","吉","凶","大凶"]
    result=random.choice(results)
    st.write(f"結果:{result}")
 



