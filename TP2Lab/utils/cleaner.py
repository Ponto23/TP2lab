import re


def remove_artifacts(text):

    text = re.sub(r"[\\x00-\\x1F\\x7F]", "", text)
    text = re.sub(r"�", "", text)

    return text


def normalize_spaces(text):

    text = re.sub(r"[ \\t]+", " ", text)
    text = re.sub(r"\\n{3,}", "\\n\\n", text)

    return text.strip()


def fix_line_breaks(text):

    lines = text.split("\\n")

    fixed_lines = []

    for line in lines:

        line = line.strip()

        if not line:
            fixed_lines.append("\\n")
        else:
            fixed_lines.append(line)

    text = " ".join(fixed_lines)

    text = re.sub(r"\\s+", " ", text)

    return text


def remove_headers_footers(text):

    lines = text.split("\\n")

    frequency = {}

    for line in lines:

        cleaned = line.strip()

        if cleaned:
            frequency[cleaned] = frequency.get(cleaned, 0) + 1

    repeated = {
        line for line, count in frequency.items()
        if count > 2 and len(line) < 60
    }

    filtered = [
        line for line in lines
        if line.strip() not in repeated
    ]

    return "\\n".join(filtered)


def clean_text(
    text,
    remove_art=True,
    normalize=True,
    fix_breaks=True,
    remove_headers=True
):

    if remove_art:
        text = remove_artifacts(text)

    if remove_headers:
        text = remove_headers_footers(text)

    if fix_breaks:
        text = fix_line_breaks(text)

    if normalize:
        text = normalize_spaces(text)

    return text