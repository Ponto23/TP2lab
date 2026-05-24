import re

def clean_text(
    text,
    remove_artifacts=True,
    normalize_spaces=True,
    fix_breaks=True,
    remove_headers=True
):

    # =========================
    # REMOVER ARTEFACTOS
    # =========================

    if remove_artifacts:

        text = re.sub(r'[^\w\s.,!?;:\-\n]', '', text)

    # =========================
    # CORRIGIR QUEBRAS
    # =========================

    if fix_breaks:

        # junta linhas partidas
        text = re.sub(r'\n(?=[a-z])', ' ', text)

    # =========================
    # NORMALIZAR ESPAÇOS
    # =========================

    if normalize_spaces:

        # remover espaços repetidos
        text = re.sub(r'[ ]+', ' ', text)

        # manter linhas organizadas
        text = re.sub(r'\n+', '\n', text)

    # =========================
    # REMOVER HEADERS
    # =========================

    if remove_headers:

        lines = text.splitlines()

        cleaned_lines = []

        for line in lines:

            line = line.strip()

            # ignorar linhas pequenas típicas
            if line.lower().startswith("pagina"):
                continue

            if line.lower().startswith("capitulo"):
                continue

            cleaned_lines.append(line)

        text = "\n".join(cleaned_lines)

    return text.strip()