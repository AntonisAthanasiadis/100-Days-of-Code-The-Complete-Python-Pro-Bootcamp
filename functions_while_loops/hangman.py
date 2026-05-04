import random
import word_list
import hangman_pics

print(hangman_pics.hangman_logo)

placeholder = ""
#Pick a word
chosen_word = random.choice(word_list.word_list)
for letter in chosen_word:
    placeholder += "_"

game_over = False
correct_letters = []
wrong_letters = []
lives = 6

while not game_over:
    #Guess a letter
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in wrong_letters and guess not in chosen_word:
        lives -= 1
        print("You lost a life! Remaining lives: ", lives)
        print(hangman_pics.hangman_pics[lives])
        wrong_letters.append(guess)

    print(display)
    print(f"Already used letters: {sorted(wrong_letters)}")

    if "_" not in display:
        game_over = True
        print("You win!")
    elif lives == 0:
        game_over = True
        print("You lose!")
