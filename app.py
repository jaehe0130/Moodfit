import streamlit as st
import time

st.set_page_config(
    page_title="MoodFit",
    page_icon="🏋️",
    layout="centered"
)

# ----------------------------
# Custom CSS (배경 + 애니메이션)
# ----------------------------
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #d2faff, #ffffff);
        }
        .fade-in {
            animation: fadeIn 1.5s ease-in-out;
        }
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(10px); }
            100% { opacity: 1; transform: translateY(0); }
        }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# 앱 타이틀
# ----------------------------
st.markdown("""
    <div class='fade-in'>
        <h1 style='text-align:center; font-size:48px; font-weight:900;'>
            🏋️ MoodFit
        </h1>
        <p style='text-align:center; font-size:22px; color:#555; margin-top:-15px;'>
            감정 기반 개인 맞춤 운동 추천 서비스
        </p>
    </div>
""", unsafe_allow_html=True)

# ----------------------------
# 간단한 문구
# ----------------------------
st.markdown("""
    <p style='text-align:center; color:#333; font-size:18px; margin-top:20px;' class='fade-in'>
        오늘의 기분을 선택하면<br>당신의 감정에 딱 맞는 운동을 추천해드릴게요!
    </p>
""", unsafe_allow_html=True)

# ----------------------------
# 자동 페이지 이동 (2초)
# ----------------------------
time.sleep(2)
st.switch_page("pages/1_user_info2.py")


