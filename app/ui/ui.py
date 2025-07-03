import streamlit as st
import requests

st.set_page_config(
    page_title="Risco de Extinção de Curso",
    layout="wide"
)

st.title("EXTINÇÃO DE CURSO")
st.write("Preencha os parâmetros abaixo e clique em **Obter Previsão**.")

# ——— Campos em duas colunas ———
col1, col2 = st.columns(2)
with col1:
    grau = st.selectbox("🎓 Grau", ["Bacharelado", "Licenciatura", "Tecnológico"])
    modalidade = st.selectbox("🖥️ Modalidade", ["Educação a Distância", "Educação Presencial"])
    regiao = st.selectbox("📍 Região", ["SUDESTE", "NORDESTE", "SUL", "CENTRO-OESTE", "NORTE"])
    categoria = st.selectbox(
        "🏢 Categoria Administrativa",
        ["Privada com fins lucrativos", "Privada sem fins lucrativos", 
         "Pública Municipal", "Pública Estadual", "Pública Federal"]
    )
with col2:
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

# ——— CSS para ampliar o botão ———
st.markdown(
    """
    <style>
    div.stButton > button {
        width: 100%;
        height: 3em;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ——— Botão abaixo, colA da esquerda ———
left, _ = st.columns([2, 5])
with left:
    submitted = st.button("🚀 Obter Previsão")

# ——— Lógica de chamada da API ———
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
            c1, c2 = st.columns(2)
            c1.metric("🏷️ Predição", label)
            c2.metric("📊 Probabilidade", f"{prob:.2%}")

            if label == "Sim" and prob > 0.6:
                st.warning("🚨 Atenção: alto risco de extinção!")
            elif label == "Sim":
                st.info("⚠️ Risco moderado de extinção.")
            else:
                st.success("✅ Baixo risco de extinção.")
