from art import logo
from random import randint

#global variables
#two levels = easy, hard
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

def check_answer(guess, answer, turns):
    # check if our guess > answer: too high
    #if guess<answer: too low
    #Guess = answer : User Wins!
    
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess<answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}. Hurray YOU WON :) ")
    
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
def game():
    print(logo)
    #Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # the final answer
    answer = randint(1, 100)
    # guess would be the guess that user is making
    guess=0
    # turn has the number of attempts left for the user
    turns=set_difficulty()
    while guess!=answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        #Let the user guess a number.
        guess = int(input("Make a guess: "))
        #turns,guess, answer
        #turns=10 answer=50 guess=25
        #turns=9
        turns=check_answer(guess,answer, turns)
        if turns==0:
            print("You've run out of guesses. you lose ..better luck next time!!")
            return
        elif guess!=answer:
            print("Guess again.")
    
game()

