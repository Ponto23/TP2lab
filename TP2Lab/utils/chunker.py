from langdetect import detect


def detect_language(text):

    try:
        return detect(text)

    except:
        return "unknown"


def chunk_text(text, chunk_size=500):

    words = text.split()

    chunks = []

    current_chunk = []
    current_size = 0

    for word in words:

        current_chunk.append(word)
        current_size += len(word) + 1

        if current_size >= chunk_size:

            chunks.append(" ".join(current_chunk))

            current_chunk = []
            current_size = 0

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks