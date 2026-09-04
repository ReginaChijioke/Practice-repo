sentence = "the quick brown fox"
Sentence = sentence.split(" ")
full_sentence = []
for word in Sentence:
    capitalized = word[0].upper() + word[1:]
    full_sentence.append(capitalized)
result = " ".join(full_sentence)
print(result)
