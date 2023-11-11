#set_up
import random
from ws import word_list
from arts import  stages, logo

#global_variables
#word list + choise + lenght
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
num = int(len(chosen_word))
# '_'
display = []
#game condition
game_end = False

#lives
lives = 6

#user functions
for _ in range(word_length):
    display += "_"

#loop

print(logo)
while game_end == False:
    guess = input("Guess a letter: ").lower()
    
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter
            num -= 1

    if guess in display:
         print(f"You've already guessed {guess}")
    elif guess not in display:
        print('You guessed', guess, ', which is not a letter in the word. You lose a life.')
        lives -= 1
            
    print(display)
    print(stages[lives])

    if '_' not in display:
        game_end = True
        print(f"You win, the word is {' '.join(display)}")
    elif lives == 0:
        game_end = True
        print('You lose, your little man died')

    
    









