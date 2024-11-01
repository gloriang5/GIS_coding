import random

def magic_8_ball():
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes – definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]

    print("Welcome to the Magic 8 Ball!")
    while True:
        question = input("\nAsk a yes-or-no question (or type 'quit' to exit): ")
        if question.lower() == "quit":
            print("Goodbye!")
            break
        else:
            answer = random.choice(responses)
            print("The Magic 8 Ball says:", answer)

# Run the Magic 8 Ball program
magic_8_ball()
