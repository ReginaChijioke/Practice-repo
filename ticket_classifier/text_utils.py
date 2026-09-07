import string
def clean_text(text):
    stripped = text.strip().lower()
    punctuations = stripped.maketrans("", "", string.punctuation)
    cleaned_text = stripped.translate(punctuations)
    return cleaned_text



