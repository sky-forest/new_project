import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import altair as alt

from main import run_home_app
from data_table import run_maxmin_app
from data_chart import run_heatmap_app

def main():
    
    st.title('인천시 군구별 근로시간에 따른 월 가구소득 비교')

    menu = ['메인화면', '표 데이터', '데이터 분석']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == '메인화면':
        run_home_app()
    elif choice == '표 데이터' :
        run_maxmin_app()
    elif choice == '데이터 분석' :
        run_heatmap_app()

if __name__ == '__main__' :
    main()