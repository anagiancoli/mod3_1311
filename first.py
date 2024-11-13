import streamlit as st
st.write("Hello World")
respgenero = st.radio('Selecione seu gênero',['Masculino','Feminino'])
respgen = st.selectbox('Selecione seu gênero',['Masculino','Feminino'])
respdep = st.multiselect('Escolha um departamento',['DCS', 'DE', 'DIR'])
st.write(respgenero)
st.write(respgen)
st.write(respdep)
