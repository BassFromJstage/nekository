# Streamlitライブラリをインポート
import streamlit as st
import random

st.title('おみくじアプリ')

if st.button('2023最新の幸運を入手'):
    results=["大吉","中吉","小吉","吉","凶","大凶"]
    result=random.choice(results)
    st.write(f"結果:{result}")
 



