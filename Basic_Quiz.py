import random
questions: list = ["What is the chemical formula of water?", "Which planet is known as the Red Planet?", "What is the powerhouse of the cell?", "What gas do plants absorb from the atmosphere?", "What is the boiling point of water at sea level?"]
answers = [
    ["H2O", "CO2", "O2", "NaCl"],
    ["Mars", "Venus", "Jupiter", "Saturn"],
    ["Mitochondria", "Nucleus", "Ribosome", "Chloroplast"],
    ["CO2", "O2", "N2", "H2"],
    ["100°C", "50°C", "150°C", "0°C"]
]

correct_answers = []

for answer_set in answers:
    random.shuffle(answer_set)
    correct_answers.append(chr(answer_set.index("H2O") + 97) if "H2O" in answer_set else 
                           chr(answer_set.index("Mars") + 97) if "Mars" in answer_set else 
                           chr(answer_set.index("Mitochondria") + 97) if "Mitochondria" in answer_set else 
                           chr(answer_set.index("CO2") + 97) if "CO2" in answer_set else 
                           chr(answer_set.index("100°C") + 97))

answers = [[f"{chr(97 + i)}. {opt}" for i, opt in enumerate(ans)] for ans in answers]
if __name__ == "__main__":
    for i in questions:
        print(i)
        for x in answers[questions.index(i)]:
            print(x)
        user_answer = input("Your answer: ")
        if user_answer == correct_answers[questions.index(i)]:
            print("Correct!")
        else:
            print("Incorrect!")