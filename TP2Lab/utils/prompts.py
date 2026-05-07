def generate_prompt(text, language="pt"):

    prompts = {

        "pt": f'''
Normaliza o seguinte texto:

- Corrige erros ortográficos
- Mantém significado original
- Remove ruído textual
- Preserva estrutura textual

Texto:
{text}
''',

        "en": f'''
Normalize the following text:

- Correct spelling mistakes
- Preserve original meaning
- Remove textual noise
- Keep text structure

Text:
{text}
'''
    }

    return prompts.get(language, prompts["en"])