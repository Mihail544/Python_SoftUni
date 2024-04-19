# 2. Grades

def grades_calculator():
    scores = float(input())

    if scores < 3.00:
        return "Fail"
    if (scores >= 3.00) and (scores < 3.50):
        return "Poor"
    if (scores >= 3.50) and (scores < 4.50):
        return "Good"
    if (scores >= 4.50) and (scores < 5.50):
        return "Very Good"
    if scores >= 5.5:
        return "Excellent"


print(grades_calculator())
