# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    user_input=int(input("Enter a number b/w 1 and 10: "))
    if user_input >= 1 and user_input <= 10:
        print("Thanks❤")
        break
    else:
        print("Invalid input , Please try again!")
       