import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from matplotlib import rcParams
import plotly.express as px



def run_heatmap_app():
    df= pd.read_csv('군구별_근로시간과 가구소득', index_col=0, )

    st.subheader('차트로 데이터 확인하기')


    column_list = df.columns

    selected_list1 = st.selectbox('확인할 데이터를 선택하세요.', column_list)

    flg1= px.pie(df, values= selected_list1, names= df.index)
    st.plotly_chart(flg1)


    selected_list2 = st.multiselect('군/구별 근무시간 데이터 확인하기', column_list[:6])
    df_selected = df[selected_list2]
    if len(selected_list2) >= 1:

        st.text('단위: %')
        st.bar_chart(df_selected)


    selected_list3 = st.multiselect('군/구별 가구소득 데이터 확인하기', column_list[6:])
    df_selected = df[selected_list3]
    if len(selected_list3) >= 1:

        st.text('단위: %')
        st.bar_chart(df_selected)


    st.subheader('근무시간과 가구소득 비교하기')

    selected_list4 = st.selectbox('근무시간을 선택해주세요.', column_list[:6])
    selected_list44 = st.selectbox('가구소득을 선택해주세요.', column_list[6:])
    df_selected = df[[selected_list4, selected_list44]]
        
    st.line_chart(df_selected)


    selected_list5 = st.multiselect('상관관계를 확인할 데이터를 선택하세요.', column_list)
    if len(selected_list5) >= 2 :

        df_corr = df[selected_list5].corr()

        fig = plt.figure()
        sb.heatmap(data= df_corr, annot=True, fmt='.2f', cmap='coolwarm', vmin= -1, vmax= 1 , linewidths=0.5 )
        st.pyplot(fig)


    
    







