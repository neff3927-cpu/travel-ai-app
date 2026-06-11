import streamlit as st

st.title("✈️ AI 여행 일정 추천 서비스")

st.write("여행 정보를 입력해주세요.")

destination = st.text_input("여행지")

period = st.selectbox(
    "여행 기간",
    ["1박2일", "2박3일", "3박4일"]
)

budget = st.selectbox(
    "예산",
    ["30만원 이하", "50만원 이하", "100만원 이하", "100만원 이상"]
)

style = st.selectbox(
    "여행 스타일",
    ["자연경관", "맛집탐방", "문화체험", "힐링여행", "가족여행"]
)

if st.button("AI 일정 생성하기"):

    if destination == "":
        st.warning("여행지를 입력해주세요.")

    elif "제주" in destination:

        st.success("AI 여행 일정 생성 완료")

        st.write("""
        ## 1일차
        - 협재해수욕장
        - 애월 카페거리

        ## 2일차
        - 성산일출봉
        - 우도 관광

        ## 3일차
        - 동문시장
        - 공항 이동
        """)

        st.info("제주도는 렌터카 이용을 권장합니다.")

    else:

        st.success("AI 여행 일정 생성 완료")

        st.write(f"""
        여행지 : {destination}

        여행 기간 : {period}

        예산 : {budget}

        여행 스타일 : {style}

        추천 관광지와 맛집 탐방을 권장합니다.
        """)
