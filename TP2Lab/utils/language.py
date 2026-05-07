def detect_language(text):
    text = text.lower()

    if "the" in text:
        return "en"

    return "pt"