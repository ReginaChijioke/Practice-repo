def passing_scores(scores):
    passed = []
    for index in range(len(scores)):
        if scores[index] >= 50:
            passed.append(scores[index])
    return passed
print(passing_scores([49, 50, 80, 65]))

"""
Defect 1 (range): loses 65 (the last element is never checked)
Defect 2 (> instead of >=): loses 50 (the boundary value is excluded)
"""

"""
ASSERTIONS 

assert passing_scores([49, 50, 80, 65]) == [50, 80, 65]
assert passing_scores([49, 80]) == [80]
assert passing_scores([]) == []
"""

