import streamlit as st
import random

st.set_page_config(
    page_title="AI 여행 일정 추천 서비스",
    page_icon="✈️"
)

st.title("✈️ AI 여행 일정 추천 서비스")
st.write("여행지와 여행 스타일을 입력하면 AI가 맞춤 일정을 추천합니다.")

destination = st.text_input("🌍 여행지")

period = st.selectbox(
    "📅 여행 기간",
    ["1박2일", "2박3일", "3박4일", "4박5일"]
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

    # 여행 스타일별 일정
    style_schedule = {
        "맛집탐방": [
            "현지 유명 맛집 방문",
            "야시장 먹거리 투어",
            "현지 카페 탐방",
            "전통 음식 체험"
        ],
        "자연경관": [
            "대표 자연 관광지 방문",
            "전망대 관람",
            "해변 또는 산책로 탐방",
            "사진 명소 방문"
        ],
        "문화체험": [
            "박물관 관람",
            "전통시장 방문",
            "역사 유적지 탐방",
            "문화 체험 프로그램 참여"
        ],
        "힐링여행": [
            "스파 체험",
            "카페 휴식",
            "공원 산책",
            "여유로운 자유시간"
        ],
        "가족여행": [
            "테마파크 방문",
            "동물원 또는 수족관",
            "체험형 관광지",
            "가족 사진 촬영"
        ]
    }

    budget_score = {
        "30만원 이하": "★★☆☆☆",
        "50만원 이하": "★★★☆☆",
        "100만원 이하": "★★★★☆",
        "100만원 이상": "★★★★★"
    }

    satisfaction = random.randint(82, 98)

    st.success("AI 여행 일정 생성 완료!")

    st.subheader("🎯 AI 여행 성향 분석")

    st.write(
        f"""
사용자는 **{style}** 중심 여행을 선호합니다.

입력한 예산은 **{budget}** 수준이며,
AI는 해당 조건에 맞는 여행 일정을 추천했습니다.
"""
    )

    st.subheader("📅 추천 일정")

    activities = style_schedule[style]

    if period == "1박2일":
        days = 2
    elif period == "2박3일":
        days = 3
    elif period == "3박4일":
        days = 4
    else:
        days = 5

    for day in range(1, days + 1):

        st.markdown(f"### {day}일차")

        st.write(
            f"""
- {destination} 대표 관광지 방문
- {activities[(day-1) % len(activities)]}
- 현지 인기 명소 탐방
"""
        )

    st.subheader("💰 예상 여행 비용")

    if budget == "30만원 이하":
        cost = "약 25~30만원"
    elif budget == "50만원 이하":
        cost = "약 40~50만원"
    elif budget == "100만원 이하":
        cost = "약 80~100만원"
    else:
        cost = "100만원 이상"

    st.write(
        f"""
예산 적합도 : {budget_score[budget]}

예상 총 비용 : {cost}

포함 항목:
- 교통비
- 숙박비
- 식비
- 관광비
"""
    )

    st.subheader("⭐ AI 만족도 예측")

    st.metric(
        label="예상 만족도",
        value=f"{satisfaction}점"
    )

    st.subheader("💡 여행 팁")

    st.write(
        f"""
1. {destination}의 날씨를 미리 확인하세요.
2. 현지 교통수단을 사전에 조사하세요.
3. 여행자 보험 가입을 권장합니다.
4. 주요 관광지는 사전 예약을 추천합니다.
"""
    )
