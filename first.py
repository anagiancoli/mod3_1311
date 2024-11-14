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

st.slider('Grau de satisfação', 1998,2024)

df = pd.DataFrame({
    'nomeServidor': ['Adriana', 'Thais', 'Samara'],
    'salario': [10000, 25000, 20000]
})

st.write("Criando uma tabela")
st.write(df)

opcao = st.selectbox(
    'Qual servidor você gostaria de selecionar?',
    options=["Selecione..."] + df['nomeServidor'].tolist()
)
