def classify(cleaned_text, categories):
    words = cleaned_text.split()
    best_score = 0
    best_category = None
    for category_name,category_data in categories.items():
        score = 0