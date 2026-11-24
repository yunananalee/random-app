import pandas as pd
import streamlit as st

# 1. 데이터 구조 (리스트) - 장르별 6권씩 [도서명, 저자, 출판사] 형태로 구성
romance = [
    ["브람스를 좋아하세요...", "프랑수아즈 사강", "민음사"],
    ["첫사랑", "이반 투르게네프", "민음사"],
    ["오만과 편견", "제인 오스틴", "민음사"],
    ["위대한 개츠비", "F. 스콧 피츠제럴드", "민음사"],
    ["노르웨이의 숲", "무라카미 하루키", "민음사"],
    ["미 비포 유", "조조 모예스", "살림"],
]

action = [
    ["헝거 게임", "수잔 콜린스", "북폴리오"],
    ["메이즈 러너", "제임스 대시너", "문학수첩"],
    ["본 아이덴티티", "로버트 러들럼", "열린책들"],
    ["다빈치 코드", "댄 브라운", "문학수첩"],
    ["마션", "앤디 위어", "알에이치코리아"],
    ["셜록 홈즈 전집", "아서 코난 도일", "황금가지"],
]

growth = [
    ["데미안", "헤르만 헤세", "민음사"],
    ["아몬드", "손원평", "창비"],
    ["연금술사", "파울로 코엘료", "문학동네"],
    ["완득이", "김려령", "창비"],
    ["호밀밭의 파수꾼", "J.D. 샐린저", "민음사"],
    ["페인트", "이희영", "창비"],
]

philosophy = [
    ["소피의 세계", "요슈타인 가아더", "현암사"],
    ["정의란 무엇인가", "마이클 샌델", "와이즈베리"],
    ["미움받을 용기", "기시미 이치로", "인플루엔셜"],
    ["니코마코스 윤리학", "아리스토텔레스", "이제이북스"],
    ["명상록", "마르쿠스 아우렐리우스", "현대지성"],
    ["피로사회", "한병철", "문학과지성사"],
]

fantasy = [
    ["해리 포터와 마법사의 돌", "J.K. 롤링", "문학수첩"],
    ["반지의 제왕", "J.R.R. 톨킨", "아르테"],
    ["달러구트 꿈 백화점", "이미예", "팩토리나인"],
    ["나니아 연대기", "C.S. 루이스", "시공주니어"],
    ["어스시의 마법사", "어슐러 K. 르 귄", "황금가지"],
    ["눈물을 마시는 새", "이영도", "황금가지"],
]

essay = [
    ["죽고 싶지만 떡볶이는 먹고 싶어", "백세희", "흔"],
    ["여행의 이유", "김영하", "문학동네"],
    ["언어의 온도", "이기주", "말글터"],
    ["물고기는 존재하지 않는다", "룰루 밀러", "곰출판"],
    ["무소유", "법정", "범우사"],
    ["보통의 존재", "이석원", "달"],
]

non_fiction = [
    ["총, 균, 쇠", "재레드 다이아몬드", "문학사상"],
    ["사피엔스", "유발 하라리", "김영사"],
    ["코스모스", "칼 세이건", "사이언스북스"],
    ["이기적 유전자", "리처드 도킨스", "을유문화사"],
    ["침묵의 봄", "레이첼 카슨", "에코리브르"],
    ["팩트풀니스", "한스 로슬링", "김영사"],
]


# 2. 함수 정의 (def) : 선택된 장르를 받아 표 데이터를 생성하는 핵심 로직
def get_recommended_books(selected_genre):
    # 3. 조건문 (if-elif-else) : 선택한 장르에 맞는 리스트 연결
    if selected_genre == "로맨스":
        target_list = romance
    elif selected_genre == "액션":
        target_list = action
    elif selected_genre == "성장":
        target_list = growth
    elif selected_genre == "철학":
        target_list = philosophy
    elif selected_genre == "판타지":
        target_list = fantasy
    elif selected_genre == "에세이":
        target_list = essay
    elif selected_genre == "비문학":
        target_list = non_fiction
    else:
        target_list = []

    # 4. 반복문 (for) : 리스트의 데이터를 하나씩 꺼내어 표(딕셔너리 리스트) 형태로 가공
    table_data = []
    for book in target_list:
        table_data.append({"도서명": book[0], "저자": book[1], "출판사": book[2]})

    return table_data


# --- 화면 구성 (Streamlit UI) ---

# [제목]
st.title("취향에 따른 베스트셀러 가이드")
st.write("---")

# (1) 장르 선택 : 드롭다운 목록
genres = ["로맨스", "액션", "성장", "철학", "판타지", "에세이", "비문학"]
selected_genre = st.selectbox("(1) 장르 선택 :", genres)

# [버튼 : 분석하기]
if st.button("분석하기"):
    # 함수 호출하여 추천 도서 데이터 가져오기
    result_books = get_recommended_books(selected_genre)

    # 출력 화면 - (텍스트 메시지)
    st.subheader(f"📚 '{selected_genre}'를 고려한 추천 목록입니다.")

    # 출력 화면 - (테이블/표)
    if result_books:
        df = pd.DataFrame(result_books)
        df.index = df.index + 1
        st.table(df)
    else:
        st.warning("해당 장르의 추천 도서 데이터가 없습니다.")
