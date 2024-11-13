import streamlit as st
st.write("Hello World")
respgenero = st.radio('Selecione seu gênero',['Selecione', 'Masculino','Feminino'])
respgen = st.selectbox('Selecione seu gênero',['Selecione','Masculino','Feminino'])
respdep = st.multiselect('Escolha um departamento',['Selecione','DCS', 'DE', 'DIR'])
st.write(respgenero)
st.write(respgen)
st.write(respdep)

if respgen == 'Masculino':
  st.success("Você conseguiu!")

numero = st.slider('Selecione um número', min_value = 0, max_value = 100)
st.text("Seu número é " + str(numero))
  
