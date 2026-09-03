import string 
def clean_input(raw_text):
    low = raw_text.lower()
    clean = low.strip()
    punctuation = clean.maketrans("", "", string.punctuation)
    cleaned_text = clean.translate(punctuation)
    return cleaned_text
print(clean_input("  kosy,, "))

