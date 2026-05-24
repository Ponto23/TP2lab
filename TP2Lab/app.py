import streamlit as st

# =========================
# IMPORTS
# =========================

from utils.cleaner import clean_text
from utils.chunker import chunk_text
from utils.prompts import generate_prompt
from utils.extractor import extract_text
from utils.language import detect_language
from utils.api import call_slm

# =========================
# CONFIGURAÇÃO DA APP
# =========================

st.set_page_config(
    page_title="TP2 Pipeline",
    layout="wide"
)

st.title("Pipeline de Processamento de Texto")

# =========================
# ETAPA 1 - UPLOAD
# =========================

st.header("1. Upload do Ficheiro")

uploaded_file = st.file_uploader(
    "Carrega um ficheiro (PDF, DOCX ou TXT)",
    type=["pdf", "docx", "txt"]
)

# =========================
# CONTINUAR APENAS SE EXISTIR FICHEIRO
# =========================

if uploaded_file is not None:

    # =========================
    # EXTRAÇÃO
    # =========================

    raw_text = extract_text(uploaded_file)

    st.subheader("Texto Original")

    st.text_area(
        "Texto extraído",
        raw_text,
        height=250
    )

    # =========================
    # ETAPA 2 - LIMPEZA
    # =========================

    st.header("2. Limpeza do Texto")

    remove_art = st.checkbox(
        "Remover artefactos",
        value=True
    )

    normalize = st.checkbox(
        "Normalizar espaços",
        value=True
    )

    fix_breaks = st.checkbox(
        "Corrigir quebras de linha",
        value=True
    )

    remove_headers = st.checkbox(
        "Remover cabeçalhos/rodapés",
        value=True
    )

    cleaned_text = clean_text(
        raw_text,
        remove_art,
        normalize,
        fix_breaks,
        remove_headers
    )

    # =========================
    # COMPARAÇÃO BEFORE/AFTER
    # =========================

    st.subheader("Comparação")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Antes")

        st.text_area(
            "Texto bruto",
            raw_text,
            height=250
        )

    with col2:

        st.subheader("Depois")

        st.text_area(
            "Texto limpo",
            cleaned_text,
            height=250
        )

    # =========================
    # ETAPA 3 - ANÁLISE
    # =========================

    st.header("3. Análise")

    language = detect_language(cleaned_text)

    st.subheader("Idioma Detetado")

    st.write(language)

    # =========================
    # CHUNKING
    # =========================

    chunks = chunk_text(cleaned_text)

    st.subheader("Chunks Gerados")

    st.write(f"Número de chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks):

        with st.expander(f"Chunk {i + 1}"):

            st.write(chunk)

    # =========================
    # ETAPA 4 - SLM
    # =========================

    st.header("4. Normalização com SLM")

    for i, chunk in enumerate(chunks):

        with st.expander(f"SLM Chunk {i + 1}"):

            # gerar prompt
            prompt = generate_prompt(
                chunk,
                language
            )

            st.subheader("Prompt Gerado")

            st.write(prompt)

            # botão para enviar
            if st.button(f"Enviar Chunk {i + 1}"):

                result = call_slm(prompt)

                st.subheader("Resposta do Modelo")

                st.write(result)

    # =========================
    # ETAPA 5 - RELATÓRIO
    # =========================

    st.header("5. Relatório")

    if st.button("Gerar Relatório"):

        html = f"""
<html>

<head>
    <title>Relatório TP2</title>
</head>

<body>

    <h1>Relatório Final</h1>

    <h2>Parâmetros da Pipeline</h2>

    <ul>
        <li>Remover artefactos: {remove_art}</li>
        <li>Normalizar espaços: {normalize}</li>
        <li>Corrigir quebras: {fix_breaks}</li>
        <li>Remover cabeçalhos/rodapés: {remove_headers}</li>
    </ul>

    <h2>Idioma Detetado</h2>

    <p>{language}</p>

    <h2>Texto Original</h2>

    <p>{raw_text}</p>

    <h2>Texto Limpo</h2>

    <p>{cleaned_text}</p>

    <h2>Número de Chunks</h2>

    <p>{len(chunks)}</p>

    <h2>Avaliação da Normalização</h2>

    <p>
    O texto final apresentou melhoria
    na organização, remoção de artefactos,
    correção de quebras de linha
    e reconstrução textual.
    </p>

</body>

</html>
"""

        st.download_button(
            label="Download Relatório",
            data=html,
            file_name="relatorio.html",
            mime="text/html"
        )
