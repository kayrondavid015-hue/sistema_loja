import streamlit as st
import pandas as pd
import plotly.express as px

# criar a tela do sistema
st.write("# Sistema de vendas")

tabela = pd.read_csv("vendas.csv")

# criar o fomulario de cadastro
st.sidebar.write("## Cadastrar venda")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
botao = st.sidebar.button("Cadastrar venda")

# salvar a venda na base de dados
if botao:
    nova_venda = [data, vendedor, produto, quantidade, valor]
    tabela.loc[len(tabela)] = nova_venda
    tabela.to_csv("vendas.csv", index=False)
    st.success("Venda cadastrada!")
    
# Mostrar a base de dados na tela
st.write("## Vendas cadastrada")
st.dataframe(tabela)

# Criar o dashboard
st.write("## Dashboard")
soma = tabela["valor"].sum()
st.metric("Faturamento total", f"R${soma}")

grafico = px.bar(tabela, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico)

grafico2 = px.pie(tabela, names="produto", values="valor")
st.plotly_chart(grafico2)