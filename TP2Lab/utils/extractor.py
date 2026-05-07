from PyPDF2 import PdfReader
from docx import Document


# =========================
# PDF
# =========================
def extract_pdf(file):
    """
    Extrai texto de PDF.
    """

    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    return text


# =========================
# DOCX
# =========================
def extract_docx(file):
    """
    Extrai texto de DOCX preservando parágrafos.
    """

    doc = Document(file)

    paragraphs = []

    for p in doc.paragraphs:
        paragraphs.append(p.text)

    return "\n".join(paragraphs)


# =========================
# TXT
# =========================
def extract_txt(file):
    """
    Extrai TXT tentando preservar encoding.
    """

    try:
        return file.read().decode("utf-8")

    except UnicodeDecodeError:
        file.seek(0)
        return file.read().decode("latin-1")


# =========================
# DISPATCH (AUTODETECÇÃO)
# =========================
def extract_text(uploaded_file):
    """
    Escolhe automaticamente o extrator.
    """

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):
        return extract_pdf(uploaded_file)

    elif file_name.endswith(".docx"):
        return extract_docx(uploaded_file)

    elif file_name.endswith(".txt"):
        return extract_txt(uploaded_file)

    else:
        raise ValueError("Formato não suportado")