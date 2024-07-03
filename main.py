import streamlit as st



st.sidebar.title('Menu')
paginaSelecionada = st.sidebar.selectbox('Selecione a página', ['Pagina 1', 'Pagina 2'])

if paginaSelecionada == 'Página 1':
    st.title('Exemplo')
    st.selectbox('Selecione uma opção', ['Opção1', 'Opção 2'])
elif  paginaSelecionada == 'Página 2':
    st.title('Você selecionou a pagina 2')