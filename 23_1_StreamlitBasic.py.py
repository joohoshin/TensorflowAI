import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 텍스트 출력
st.title('Streamlit Practice')
st.header('이것은 header입니다. ')
st.subheader('이것은 subheader입니다.')
st.write('이것은 write입니다. ')

# 데이터 출력
iris = sns.load_dataset('iris')

st.subheader('st.write()으로 데이터 출력')
st.write(iris)

# Chart 출력
summary = pd.pivot_table(iris, values='sepal_length', index=['species'],
                    aggfunc='mean')

st.subheader('matplotlib 라이브러리 활용')
summary.plot.bar()
st.pyplot()

st.subheader('streamlit 차트 활용')
st.bar_chart(summary)

### user input

# button
button = st.button('Say Hello')
if button:
    st.write('button clicked')
else:
    st.write('button not clicked')

# checkbox    
if st.checkbox('I agree'):
    st.write('thanks')
    
# dropdown
option = st.selectbox('좋아하는 색상은?', 
                      ['Red', 'Green', 'Blue'])
st.write('you selected', option)
    
# multiselect
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])
st.write('You selected:', options)

# slider
age = st.slider('How old are you?', 0, 130, 25) #최소, 최대, 기본값
st.write("I'm ", age, 'years old')