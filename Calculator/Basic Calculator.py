def add(num1 , num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

# def calculator():
select = int(input("1. Add \n2. Subtract \n3. Multiply \n4. Divide \nSelect from 1,2,3,4: "))


numb1 = float(input("Enter first number: "))
numb2 = float(input("Enter second number: "))

if select == 1:
    print(numb1, "+", numb2 , "=" , add(numb1,numb2))
elif select == 2:
    print(numb1, "-", numb2 , "=" , subtract(numb1,numb2))
elif select == 3:
    print(numb1, "*", numb2 , "=" , multiply(numb1,numb2))
elif select == 4:
    print(numb1, "/", numb2 , "=" , divide(numb1,numb2))
else:
    print("Invalid Input")

while input("Would you like to do another? (y/n) ").lower() == "y":
        continue