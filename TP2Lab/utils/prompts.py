def generate_prompt(text, language="pt"):

    # português
    if language == "pt":

        return f"""
Normaliza o seguinte texto:
- Corrige erros ortográficos
- Mantém o significado original
- Remove ruído textual
- Preserva a estrutura textual

Texto:
{text}
"""

    # inglês
    else:

        return f"""
Normalize the following text:
- Correct spelling mistakes
- Preserve original meaning
- Remove textual noise
- Keep text structure

Text:
{text}
"""