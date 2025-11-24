import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="추천 평가", page_icon="📊", layout="centered")

st.title("📊 추천운동 평가")

# ===== 추천 결과 전달받기 =====
# recommendation 페이지에서 session_state에 저장했다고 가정
recommended = st.session_state.get("recommended_workouts", ["운동1", "운동2", "운동3"])

st.write("📍 오늘 추천받은 운동:")
for r in recommended:
    st.markdown(f"- **{r}**")

st.markdown("---")

# ===== 사용자 입력 폼 =====
st.subheader("📝 추천 운동 평가 입력")

ratings = {}
for r in recommended:
    ratings[r] = st.slider(f"{r} 적합도 평가", 1, 5, 3)

overall = st.radio("전체 추천 만족도", ["👍 좋았어요", "🙂 보통", "👎 별로예요"])
comment = st.text_area("개선 의견이 있다면 작성해주세요 (선택 사항)")

if st.button("💾 평가 저장하기", use_container_width=True):
    # Save to CSV
    data = {
        "timestamp": datetime.now(),
        "추천1": recommended[0],
        "추천2": recommended[1],
        "추천3": recommended[2],
        "전체만족도": overall,
        "코멘트": comment,
    }
    for r in recommended:
        data[f"{r}_점수"] = ratings[r]

    df = pd.DataFrame([data])

    # Save or append
    if os.path.exists("evaluation_results.csv"):
        df.to_csv("evaluation_results.csv", mode="a", header=False, index=False)
    else:
        df.to_csv("evaluation_results.csv", index=False)

    st.success("🎉 평가가 저장되었습니다! 감사합니다.")
