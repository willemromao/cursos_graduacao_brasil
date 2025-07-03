import streamlit as st
import requests

st.set_page_config(
    page_title="ANÁLISE DE RISCO DE EXTINÇÃO DE CURSO",
    layout="centered",
)

st.markdown("""
    <style>
        /* Centraliza o título */
        .title-container {
            text-align: center;
            font-size: 30px;
            font-weight: bold;
        }

        /* Aumenta o texto de instrução */
        .instructions {
            text-align: center;
            font-size: 18px;
            margin-bottom: 2em;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-container">🏛️ ANÁLISE DE RISCO DE EXTINÇÃO DE CURSO 🏛️</div>', unsafe_allow_html=True)
st.markdown('<div class="instructions">Preencha os parâmetros abaixo e clique em <strong>Obter Previsão</strong>.</div>', unsafe_allow_html=True)

grau = st.selectbox("🎓 Grau", ["Bacharelado", "Licenciatura", "Tecnológico"])

modalidade = st.selectbox("🖥️ Modalidade", ["Educação a Distância", "Educação Presencial"])

regiao = st.selectbox("📍 Região", ["SUDESTE", "NORDESTE", "SUL", "CENTRO-OESTE", "NORTE"])

categoria = st.selectbox(
    "🏢 Categoria Administrativa",
    ["Privada com fins lucrativos", "Privada sem fins lucrativos", 
     "Pública Municipal", "Pública Estadual", "Pública Federal"]
)

organizacao = st.selectbox(
    "🏫 Organização Acadêmica",
    ["Centro Universitário", "Universidade", "Faculdade", 
        "Instituto Federal de Educação, Ciência e Tecnologia", 
        "Centro Federal de Educação Tecnológica"]
)

vagas = st.selectbox(
        "🎫 Vagas autorizadas",
        ["Até 50", "51-100", "101-200", "201-500", "501-1000", "Mais de 1000"]
    )
carga = st.selectbox(
    "⏳ Carga horária",
    ["Até 1000h", "1001-2000h", "2001-3000h", 
     "3001-4000h", "4001-5000h", "Mais de 5000h"]
)

submitted = st.button("🚀 Obter Previsão")

if submitted:
    input_data = {
        "GRAU": grau,
        "MODALIDADE": modalidade,
        "REGIAO": regiao,
        "CATEGORIA_ADMINISTRATIVA": categoria,
        "ORGANIZACAO_ACADEMICA": organizacao,
        "QT_VAGAS_AUTORIZADAS": vagas,
        "CARGA_HORARIA": carga
    }

    with st.spinner("🔍 Carregando previsão..."):
        try:
            resp = requests.post("http://api:8000/predict", json=input_data, timeout=5)
            resp.raise_for_status()
            result = resp.json()
            label = result["extincao_predita"]
            prob = result["probabilidade"]
        except Exception as e:
            st.error(f"⚠️ Erro ao obter previsão: {e}")
        else:
            if label == "Sim" and prob > 0.6:
                st.warning("🚨 Atenção: alto risco de extinção!")
            elif label == "Sim":
                st.info("⚠️ Risco moderado de extinção.")
            else:
                st.success("✅ Baixo risco de extinção.")