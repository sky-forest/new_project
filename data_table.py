import streamlit as st
import pandas as pd

def run_maxmin_app():
    df= pd.read_csv('군구별_근로시간과 가구소득', index_col=0)
    
    st.subheader('전체 데이터 표')
    st.dataframe(df.iloc[: , : 5])
    st.dataframe(df.iloc[: , 6: ])
    st.text('(단위: %)')

    img_url= 'https://cdn.press.uos.ac.kr/news/photo/202109/12807_6970_5031.jpg'
    st.image(img_url)

    st.subheader('항목별 최대, 최소 데이터를 갖는 군/구 확인하기')

    columns_list= df.columns

    seleced_column= st.selectbox('확인할 데이터를 선택하세요.', columns_list)

    df_max = df.loc[ df[seleced_column] ==  df[seleced_column].max(), ]
    df_min = df.loc[ df[seleced_column] ==  df[seleced_column].min(), ]

    st.text('최대 데이터(단위: %)')
    st.dataframe(df_max.iloc[: , : 6])
    st.dataframe(df_max.iloc[: , 6: ])

    st.text('최소 데이터(단위: %)')
    st.dataframe(df_min.iloc[: , : 6])
    st.dataframe(df_min.iloc[: , 6: ])
