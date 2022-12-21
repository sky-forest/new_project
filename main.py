import streamlit as st

def run_home_app():
    st.subheader('환영합니다.')
    st.text('인천시 군/구별 일 평균 근무시간과 월 평균 가구소득 데이터의 확인 및 비교를 위해 만들어졌으며,')
    st.text('2021년도 자료를 기반으로 작성되었습니다.')

    img_url= 'https://img.freepik.com/premium-vector/mechanical-scales-with-dollar-coin-and-hourglass-time-and-money-balance-comparison-work-and-value-financial-profit-annual-revenue-future-income-cash-and-watch-on-weight-scale_458444-185.jpg'

    st.image(img_url)
