print("Decision Quiz Starter")
score = 0

answer = input("Which keyword starts a decision in Python? " ).strip().lower()
if answer == "if":
    score += 1
    print("Correct.")
else:
    print("Review conditionals.")

print("Score:", score)
