print("Welcome to Treasure Island \n Your mission is to find the treasure.")
step1=str(input("Left o right"))
if step1 == "left" :
  step2= str(input("Swim OR Wait"))
  if step2 == "wait" :
      step3=str(input("Which Door You want to select: Red ,YEllow, Blue"))
      if step3 == "blue":
          print("attacked by trout;\nGame Over ")
      if step3 == "red" :
          print("Burned by Fire.\n Game ove")
      if step3 == "yellow":
          print("YOU WIN !")

  else:
    print("Attacked by a Crocodile \n Game Over")
else:
 print("Fall in a Hole .\n Game Over")

