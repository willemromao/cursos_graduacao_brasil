import streamlit as st
import requests

st.title("PREVEJA O RISCO DE EXTINÇÃO DE UM CURSO DE GRADUAÇÃO :books:")

st.subheader("Preencha os valores abaixo para obter uma previsão:")

categoria_administrativa = st.radio("CATEGORIA ADMINISTRATIVA:", [
    "Privada com fins lucrativos",
    "Privada sem fins lucrativos",
    "Pública Municipal",
    "Pública Federal",
    "Pública Estadual"
])

organizacao_academica = st.radio("ORGANIZAÇÃO ACADÊMICA:", [
    "Centro Universitário",
    "Universidade",
    "Faculdade",
    "Instituto Federal de Educação, Ciência e Tecnologia",
    "Centro Federal de Educação Tecnológica"
])

grau = st.radio("GRAU:", ["Bacharelado", "Licenciatura", "Tecnológico"])

modalidade = st.radio("MODALIDADE:", ["Educação a Distância", "Educação Presencial"])

regiao = st.radio("REGIÃO:", ["SUDESTE", "NORDESTE", "SUL", "CENTRO-OESTE", "NORTE"])

quantidade_vagas = st.number_input("QUANTIDADE DE VAGAS AUTORIZADAS POR ANO OU POR SEMESTRE:", 10, 12000)

carga_horaria = st.number_input("CARGA HORÁRIA DO CURSO:", 1000, 7000)

if st.button("Obter previsão"):
    input_data = {
        "CATEGORIA_ADMINISTRATIVA": categoria_administrativa,
        "ORGANIZACAO_ACADEMICA": organizacao_academica,
        "GRAU": grau,
        "MODALIDADE": modalidade,
        "REGIAO": regiao,
        "QT_VAGAS_AUTORIZADAS": quantidade_vagas,
        "CARGA_HORARIA": carga_horaria
    }

    url = "http://localhost:5000/predict"

    response = requests.post(url, json=input_data)

    if response.status_code == 200:
        prediction = response.json().get('prediction', [])
        st.markdown(f":point_right: **{prediction}**")
    else:
        st.error(f"Erro ao obter previsão: {response.text}")
