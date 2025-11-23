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
        .hero-img {
            width: 65%;
            display: block;
            margin: 0 auto;
            border-radius: 20px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.15);
        }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# 앱 타이틀
# ----------------------------
st.markdown("""
    <div class='fade-in'>
        <h1 style='text-align:center; font-size:45px; font-weight:800;'>
            🏋️ MoodFit
        </h1>
        <p style='text-align:center; font-size:22px; color:#555; margin-top:-15px;'>
            감정 기반 개인 맞춤 운동 추천 서비스
        </p>
    </div>
""", unsafe_allow_html=True)

# ----------------------------
# 로컬 운동 이미지 출력
# ----------------------------
st.image(
    "/mnt/data/2005.i121.015.P.m005.c33.isometric home fitness set.jpg",
    use_column_width=False,
    caption="당신의 감정에 맞춘 최적의 운동을 찾아보세요!"
)

st.markdown("""
    <p style='text-align:center; color:#444; font-size:18px; margin-top:10px;' class='fade-in'>
        오늘의 기분을 선택하고, 맞춤 운동 루틴을 추천받아보세요!
    </p>
""", unsafe_allow_html=True)

# ----------------------------
# 자동 페이지 이동 (2초)
# ----------------------------
time.sleep(2)
st.switch_page("pages/1_user_info2.py")

