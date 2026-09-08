from categories import categories
from categories import general_response
def classify(cleaned_text, categories):
    words = cleaned_text.split()
    best_score = 0
    best_category = None
    for category_name,category_data in categories.items():
        score = 0
        for keyword in category_data["keywords"]:
            if keyword in words:
                score += 1

        if score > best_score:
            best_score = score
            best_category = category_name
            
    if best_category is None:
        return general_response
    else:
        return best_category

print(classify("my computer has an error", categories))
