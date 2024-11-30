import random
from art import logo, stages
from words import word_list

# _ _ _ _ _ _ =display
# _ _ a _ _
# user makes a guess -> if the user guesses coreectly we fill in the blank
#if user makes an incorrect guess - we decrease life
# continue till game ends
end_of_game=False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
print(logo)
#creating blanks
display=[]
for _ in range (word_length):
    display+="_"
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("You've already guessed this letter!!")
        
    # for checking guess and letters and modifying display
    for position in range (word_length):
        # chose word = bcadb
        # guess by user is a
        # initially display _ _ _ _ _
        # after display _ _ a _ _
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            
    # check if user has made a wrong guess
    if guess not in chosen_word:
        print("You guesses incorrectly. you have lost a life.!!")
        lives -= 1
        if lives == 0:
            end_of_game=True
            print("You have run out of lives. Game over!!")
    
    print(f"{' '.join(display)}") # "separator".join(list)
    if "_" not in display:
        end_of_game=True
        print("You have won!!")
        
    print(stages[lives]) #print the stages of the game