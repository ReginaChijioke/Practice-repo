vowel = ["a", "e", "i", "o", "u"]
word = "REgInA"
count = 0
for character in word:
    if character in vowel:
        count += 1
print(count)

vowel = ["a", "e", "i", "o", "u"]
word = "REgInA"
char = word.lower()
count = 0
for character in char:
    if character in vowel:
        count += 1
print(count)

vowel = ["a", "e", "i", "o", "u"]
word = "REgInA".lower()
count = 0
for character in word:
    if character in vowel:
        count += 1
print(count)