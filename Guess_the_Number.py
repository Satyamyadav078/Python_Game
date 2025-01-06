import random

def number():
    choice =0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    level=input("Choose a difficulty. Type 'easy' or 'hard':")


    if level == 'easy' :
        print("Easy")
        print("You have 10 choice ")
        choice = 10
    elif level == 'hard':
        print("hard")
        print("you have 5 choices")
        choice= 5



    guess = True
    random_number= random.randint(1, 101)
    while guess :

      if choice != 0:

        num = int(input("Guess the number"))
        if num > random_number:
          print("You guess Too High ")

        elif num < random_number:
            print("You guessed too low ")

        elif num == random_number :
            print ("you guess it correctly ! You Win ")
            guess = False


        choice-=1
        print(f"You Have Left {choice} lives")
      else :
           print("You Loose")
           guess = 0

cart = True
while chr :
    number()
    yes_or_no=input("Do You Want To Play Again")
    if yes_or_no == 'no':
        cart = False

