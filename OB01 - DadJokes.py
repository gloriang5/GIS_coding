import random

all_list = []
prompts =[]
answers = []

def PrintRandomJoke(p, a, rand_int):
    print(p[rand_int])
    answer = str(input(f"Enter your reply:\n"))
    if answer == a[rand_int]:
        print("Correct!")
    else:
        print(a[rand_int])


def Constructor(list):
    for i in range(len(list)):
        if i % 2 == 1:
            answers.append(list[i])
        else:
            prompts.append(list[i])

with open("pythonchallenges/As level/Dad Joke/DadJokes.txt", "r") as file:
    all_list.extend(line.strip() for line in file.readlines())

Constructor(all_list)

index = random.randint(0, len(prompts))
PrintRandomJoke(prompts, answers, index)


