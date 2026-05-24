from PyPDF2 import PdfReader
from docx import Document

# =========================
# EXTRAÇÃO PDF
# =========================

def extract_pdf(file):

    text = ""

    try:

        reader = PdfReader(file)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    except Exception as e:

        text = f"Erro ao ler PDF: {e}"

    return text


# =========================
# EXTRAÇÃO DOCX
# =========================

def extract_docx(file):

    text = ""

    try:

        doc = Document(file)

        for para in doc.paragraphs:

            text += para.text + "\n"

    except Exception as e:

        text = f"Erro ao ler DOCX: {e}"

    return text


# =========================
# EXTRAÇÃO TXT
# =========================

def extract_txt(file):

    try:

        # tentar UTF-8
        text = file.read().decode("utf-8")

    except:

        try:

            # fallback latin-1
            file.seek(0)

            text = file.read().decode("latin-1")

        except Exception as e:

            text = f"Erro ao ler TXT: {e}"

    return text


# =========================
# EXTRAÇÃO AUTOMÁTICA
# =========================

def extract_text(uploaded_file):

    file_name = uploaded_file.name.lower()

    # PDF
    if file_name.endswith(".pdf"):

        return extract_pdf(uploaded_file)

    # DOCX
    elif file_name.endswith(".docx"):

        return extract_docx(uploaded_file)

    # TXT
    elif file_name.endswith(".txt"):

        return extract_txt(uploaded_file)

    # inválido
    else:

        return "Formato não suportado."