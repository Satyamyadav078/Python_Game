import random
rock ="""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
   """
scissiors= """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
           """
choice_of_man=int(input("What do you choose? Type 0 for Rock , 1 for Paper or 2 for Scissors. "))
choice_of_computer=random.randint(0,2)
if choice_of_man == 0 and choice_of_computer == 1 :
    print("YOURS Choice :-"+rock+"Computer's Choice :-"+paper)
    print("YOU Win")
elif choice_of_man == 0  and choice_of_computer == 2 :
    print("YOURS Choice :-"+rock+"Computer's Choice :-"+scissiors)
    print("YOU Win")
elif choice_of_man == 1 and choice_of_computer == 0 :
    print("YOURS Choice :-"+paper+"Computer's Choice :-"+rock)
    print("YOU Loose")
elif choice_of_man == 1 and choice_of_computer == 2 :
    print("YOURS Choice :-"+paper+"Computer's Choice :-"+scissiors)
    print("YOU Loose")
elif choice_of_man == 2 and choice_of_computer == 0 :
    print("YOURS Choice :-"+scissiors+"Computer's Choice :-"+rock)
    print("YOU Loose")
elif choice_of_man == 2 and choice_of_computer == 1 :
    print("YOURS Choice :-"+scissiors+"Computer's Choice :-"+paper)
    print("YOU Win")
elif choice_of_man == 0 and choice_of_computer == 0 :
    print("YOURS Choice :-"+rock+"Computer's Choice :-"+rock)
    print("Play Again")
elif choice_of_man == 1 and choice_of_computer == 1 :
    print("YOURS Choice :-"+paper+"Computer's Choice :-"+paper)
    print("Play Again")
elif choice_of_man == 2 and choice_of_computer == 2 :
    print("YOURS Choice :-"+scissiors+"Computer's Choice :-"+scissiors)
    print("Play Again")
else :
    print("Write the correct number")