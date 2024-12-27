logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
repetition = True
while repetition :

# TODO-1: Ask the user for input
    name=input("Enter your name")
    bids= int(input("Enter the Bills "))
    print("\n"*20)

# TODO-2: Save data into dictionary {name: price}
    data = {name : bids}


# TODO-3: Whether if new bids need to be added





    check = input("Whether there is more person 'yes' or 'no' ")
    print("\n"*20)
    if check == 'no':
        repetition = False
max=0
person =""
# TODO-4: Compare bids in dictionary
for key in data:
        price = data[key]
        if price > max :
            max = price
            person=key
print(f"Winner is {person} whose bid is {max}")

