import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI 여행 일정 추천 서비스")

st.title("✈️ AI 여행 일정 추천 서비스")
st.write("AI가 여행 일정, 예상 비용, 만족도, 여행 팁을 추천합니다.")

# Streamlit Secrets에 저장된 API Key 사용
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

destination = st.text_input("🌍 여행지")

period = st.selectbox(
    "📅 여행 기간",
    ["1박2일", "2박3일", "3박4일", "4박5일", "5박6일"]
)

budget = st.selectbox(
    "💰 예산",
    ["30만원 이하", "50만원 이하", "100만원 이하", "100만원 이상"]
)

style = st.selectbox(
    "🎯 여행 스타일",
    ["맛집탐방", "자연경관", "문화체험", "힐링여행", "가족여행"]
)

if st.button("🤖 AI 일정 생성하기"):

    if destination == "":
        st.warning("여행지를 입력해주세요.")
        st.stop()

    with st.spinner("AI가 여행 계획을 생성하고 있습니다..."):

        prompt = f"""
당신은 전문 여행 플래너입니다.

다음 조건에 맞는 여행 계획을 작성하세요.

여행지: {destination}
여행기간: {period}
예산: {budget}
여행스타일: {style}

반드시 아래 형식으로 답변하세요.

# AI 여행 분석 결과

## 여행 성향 분석

## 추천 일정
(일차별 상세 일정)

## 예상 여행 비용
- 항공권
- 숙박
- 식비
- 교통비
- 총 예상비용

## 만족도 예측
100점 만점 기준

## 여행 팁
3개 이상

한국어로 작성하고 보기 좋게 작성하세요.
"""

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "당신은 전문 여행 플래너입니다."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.8
        )

        result = response.choices[0].message.content

        st.success("AI 여행 일정 생성 완료!")

        st.markdown(result)
