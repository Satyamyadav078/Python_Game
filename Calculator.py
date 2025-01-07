logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
def add( n1,  n2):
    return n1 + n2
def sub(n1,n2):
    return n1 -n2
def mul(n1,n2) :
    return  n1*n2
def div(n1,n2):
    return n1/n2

operations ={
    "+": add ,
    "-": sub ,
    "/": div ,
    "*": mul
}
def calculator() :
  num1 = int(input("Write the first number "))
  for symbol in operations:
      print(symbol)
  operation_symbol = input("select the operation :")
  cond=True
  while cond :



    num2= int(input("Write the second number"))
    out=operations[operation_symbol](num1,num2)
    print(out)
    choice=input(f"Type 'y' to continue calculating with {out} or type 'n' to start a new calculation:")
    if choice =='y':
        num1=out
    else:
        cond = False
        calculator()


calculator()







