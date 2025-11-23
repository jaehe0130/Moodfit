import streamlit as st
import pandas as pd
import os

st.title("회원 등록")

csv_path = "users.csv"

name = st.text_input("이름을 입력하세요")
age = st.number_input("나이", min_value=10, max_value=100, value=25)
gender = st.selectbox("성별", ["남성", "여성"])
height = st.number_input("키 (cm)", min_value=100, max_value=250, value=170)
weight = st.number_input("몸무게 (kg)", min_value=30, max_value=200, value=60)
activity = st.selectbox("평소 활동량", ["낮음", "보통", "높음"])

# 부상 이력
injury_status = st.radio("부상 이력", ["없음", "있음"])
injury_detail = ""
if injury_status == "있음":
    common_injuries = ["무릎", "허리", "어깨", "발목", "손목", "기타"]
    selected_parts = st.multiselect("부상 부위를 선택하세요 (복수 선택 가능)", common_injuries)

    if "기타" in selected_parts:
        other_injury = st.text_input("기타 부상을 입력하세요")
        if other_injury.strip() != "":
            selected_parts.append(other_injury)

    injury_detail = ", ".join(selected_parts) if selected_parts else "있음"

# ===== 인코딩 안전 읽기 함수 =====
def read_csv_robust(path: str) -> pd.DataFrame:
    # 가장 권장: utf-8-sig
    encodings_to_try = ["utf-8-sig", "utf-8", "cp949"]
    last_err = None
    for enc in encodings_to_try:
        try:
            return pd.read_csv(path, encoding=enc)
        except Exception as e:
            last_err = e
    # 모두 실패 시 예외 재발생
    raise last_err

if st.button("등록 완료"):
    if name.strip() == "":
        st.warning("이름을 입력해주세요.")
    else:
        new_data = pd.DataFrame({
            "이름": [name],
            "나이": [age],
            "성별": [gender],
            "키(cm)": [height],
            "몸무게(kg)": [weight],
            "활동량": [activity],
            "부상 이력": [injury_status],
            "부상 상세": [injury_detail]
        })

        if os.path.exists(csv_path):
            try:
                existing = read_csv_robust(csv_path)
            except Exception as e:
                st.error(f"CSV 읽기 중 인코딩 오류가 발생했습니다: {e}")
                st.info("파일을 엑셀로 여신 뒤 '다른 이름으로 저장' → CSV UTF-8(또는 CSV UTF-8(콤마로 분리))로 저장하시면 해결됩니다.")
                st.stop()

            if "이름" in existing.columns and name in existing["이름"].astype(str).values:
                st.warning("이미 등록된 사용자입니다.")
            else:
                updated = pd.concat([existing, new_data], ignore_index=True)
                # 항상 utf-8-sig로 저장 → 엑셀 호환 + 한글 안전
                updated.to_csv(csv_path, index=False, encoding="utf-8-sig")
                st.success("등록이 완료되었습니다.")
        else:
            # 새 파일도 utf-8-sig로 고정
            new_data.to_csv(csv_path, index=False, encoding="utf-8-sig")
            st.success("등록이 완료되었습니다.")
