import random

def decimal_to_hex(dec):
    return hex(dec)[2:]

def decimal_to_binary(dec):
    return bin(dec)[2:]

def hex_to_decimal(hex_str):
    return int(hex_str, 16)

def binary_to_decimal(bin_str):
    return int(bin_str, 2)

def quiz():
    print("Welcome to the Hex & Binary Quiz!")
    score = 0

    # Generate random quiz questions
    for _ in range(5):
        num = random.randint(0, 255)  # Random number from 0 to 255

        # Randomly choose the type of question
        question_type = random.choice(["decimal_to_hex", "decimal_to_binary", "hex_to_decimal", "binary_to_decimal"])

        if question_type == "decimal_to_hex":
            answer = decimal_to_hex(num)
            user_input = input(f"What is the hexadecimal of {num}? ").lower()
            if user_input == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer was {answer}.")

        elif question_type == "decimal_to_binary":
            answer = decimal_to_binary(num)
            user_input = input(f"What is the binary of {num}? ").lower()
            if user_input == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer was {answer}.")

        elif question_type == "hex_to_decimal":
            hex_num = decimal_to_hex(num)
            answer = str(num)
            user_input = input(f"What is the decimal of hex {hex_num}? ")
            if user_input == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer was {answer}.")

        elif question_type == "binary_to_decimal":
            binary_num = decimal_to_binary(num)
            answer = str(num)
            user_input = input(f"What is the decimal of binary {binary_num}? ")
            if user_input == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer was {answer}.")

    print(f"\nQuiz finished! Your score is {score} out of 5.")

# Run the quiz
quiz()
