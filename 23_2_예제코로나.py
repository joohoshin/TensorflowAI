# 코로나 분석 파일

# data.go.kr api 활용
# https://data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15043376
# XML

import requests
import pandas as pd
import xmltodict
import streamlit as st

start = '20200101'
pageNo = 1
numOfRows=1000

apikey='7qije2BqVky4RqxYN%2F9Y8RIJ%2BRptWy2b2LTkH%2F%2BohgqcWERlIo%2BtnVTlr5NNHmnouP93F%2BYETALrAfup%2BJClsA%3D%3D'
url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'
params ='?ServiceKey={}&startCreateDt={}&pageNo={}&numOfRows={}'.format(apikey, start, pageNo, numOfRows)

@st.cache(allow_output_mutation=True)
def get_data():
    print(url+params)
    res = requests.get(url+params, timeout=5)
    res_dict = xmltodict.parse(res.text)
    items = res_dict['response']['body']['items']['item']
    df = pd.DataFrame(items)
    return df

raw_df = get_data()

raw_df.columns = ['누적환진률','누적검사수','누적검사완료수','치료중환자수',
              '격리해제수','등록일시분초','사망자수','확진자수',
              '검사진행수','결과음성수','고유값', '기준일', '기준시간', 
              '수정일시분초'              
              ]

numeric_cols = ['누적환진률','누적검사수','누적검사완료수','치료중환자수',
              '격리해제수','사망자수','확진자수',
              '검사진행수','결과음성수','고유값'
              ]
raw_df[numeric_cols]= raw_df[numeric_cols].apply(lambda col: pd.to_numeric(col), axis = 1)
raw_df['기준일'] = pd.to_datetime(raw_df.기준일)
raw_df = raw_df.dropna()
raw_df = raw_df.set_index('기준일')

st.title('코로나 국내 현황')
today = raw_df.index.max().date()
st.write(today)

options = ("치료 중 환자수", "누적 사망자수", "확진자수", '누적환진률')
select= st.sidebar.selectbox(
    "보고싶은 것은? ", options  
)


if select == options[0]:  
    st.subheader('치료중 환자수')
    st.line_chart(raw_df[['치료중환자수']])
    st.write(raw_df[['치료중환자수']],use_container_width=True )
elif select == options[1]:  
    st.subheader('누적 사망자수')
    st.line_chart(raw_df[['사망자수']])
    st.write(raw_df[['사망자수']] ,use_container_width=True)
elif select == options[2]:  
    st.subheader('확진자수')
    st.line_chart(raw_df[['확진자수']])
    st.write(raw_df[['확진자수']] ,use_container_width=True)
elif select == options[3]:  
    st.subheader('누적환진률')
    st.line_chart(raw_df[['누적환진률']])
    st.write(raw_df[['누적환진률']] ,use_container_width=True)
