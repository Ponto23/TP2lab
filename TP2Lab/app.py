import streamlit as st

# =========================
# IMPORTS DA PIPELINE
# =========================
from utils.cleaner import clean_text
from utils.chunker import chunk_text
from utils.prompts import generate_prompt
from utils.extractor import extract_text
from utils.language import detect_language


# =========================
# CONFIGURAÇÃO APP
# =========================
st.set_page_config(page_title="TP2 Pipeline", layout="wide")

st.title("Pipeline de Processamento de Texto")


# =========================
# UPLOAD + EXTRAÇÃO
# =========================
st.header("1. Input do Ficheiro")

uploaded_file = st.file_uploader(
    "Carrega um ficheiro (PDF, DOCX ou TXT)",
    type=["pdf", "docx", "txt"]
)

raw_text = ""

if uploaded_file is not None:
    raw_text = extract_text(uploaded_file)

    st.subheader("Texto Extraído")
    st.text_area("Preview", raw_text, height=200)


# =========================
# ETAPA 2 - LIMPEZA
# =========================
st.header("2. Limpeza do Texto")

st.subheader("Configuração da Pipeline")

remove_art = st.checkbox("Remover artefactos", value=True)
normalize = st.checkbox("Normalizar espaços", value=True)
fix_breaks = st.checkbox("Corrigir quebras de linha", value=True)
remove_headers = st.checkbox("Remover cabeçalhos/rodapés", value=True)

cleaned_text = clean_text(
    raw_text,
    remove_art,
    normalize,
    fix_breaks,
    remove_headers
)

st.subheader("Texto Limpo")
st.text_area("Resultado", cleaned_text, height=250)


# =========================
# ETAPA 3 - ANÁLISE
# =========================
st.header("3. Análise")

language = detect_language(cleaned_text)

st.subheader("Idioma Detetado")
st.write(language)

chunks = chunk_text(cleaned_text)

st.subheader("Chunks Gerados")
st.write(f"Número de chunks: {len(chunks)}")


# =========================
# ETAPA 4 - PROMPTS
# =========================
st.header("4. Geração de Prompts")

for i, chunk in enumerate(chunks):
    with st.expander(f"Chunk {i + 1}"):

        st.write(chunk)

        prompt = generate_prompt(chunk, language)

        st.subheader("Prompt Gerado")
        st.code(prompt)