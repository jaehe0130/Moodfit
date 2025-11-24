import streamlit as st
import time

st.set_page_config(page_title="MoodFit", page_icon="🏋️", layout="centered")

# 이미지 중앙 배치
st.markdown("<div style='height:12vh;'></div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("assets/home_fitness.jpg", width=350)

st.markdown("""
<h1 style="text-align:center; margin-top:15px; font-size:42px; font-weight:900;">
🏋️ MoodFit
</h1>
""", unsafe_allow_html=True)

# ----------------------
# Redirect Logic (Python)
# ----------------------
if "redirected" not in st.session_state:
    st.session_state.redirected = True
    time.sleep(2)
    st.experimental_rerun()  # rerun 발생

else:
    st.switch_page("1_user_info2")

