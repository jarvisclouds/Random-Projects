user_name = input("Name: ")
print("Welcome", user_name +"!")
while True:
    user_choice = input("Choose a number or type 'done' to exit: ")
    if user_choice == "done":
        break
    elif float(user_choice) % 2 == 0:
        print(float(user_choice), "is an even number.")
    elif float(user_choice) % 2 == 1:
        print(float(user_choice), "is an odd number.")