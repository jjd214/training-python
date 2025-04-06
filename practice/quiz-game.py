# Quiz game

questions = (
    "What is the capital of France?",
    "What is the largest planet in our solar system?",
    "What is the chemical symbol for gold?",
    "What is the largest mammal in the world?",
    "What is the smallest country in the world?",
)

options = (
    ("A. Paris", "B. London", "C. Berlin", "D. Madrid"),
    ("A. Jupiter", "B. Saturn", "C. Mars", "D. Earth"),
    ("A. Au", "B. Ag", "C. Pb", "D. Fe"),
    ("A. Blue Whale", "B. Elephant", "C. Giraffe", "D. Hippopotamus"),
    ("A. Vatican City", "B. Monaco", "C. Nauru", "D. San Marino"),
)

answers = ("A", "A", "A", "A", "A")

guess = []

for i in range(len(questions)):
    print(questions[i])
    for j in range(len(options[i])):
        print(options[i][j], end=" ")
    print()
    temp_guess = input("Enter your answer (A, B, C, D): ").upper()
    guess.append(temp_guess)

show_score = []

count = 1

for i in range(len(answers)):
    if guess[i] == answers[i]:
        show_score.append(f"{count}. correct!")
    else:
        show_score.append(f"{count}. incorrect!")
    count += 1


print("--- Score ---")
for i in show_score:
    print(i)
