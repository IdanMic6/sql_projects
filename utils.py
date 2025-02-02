def getOnlyNumber(message):
    while True:
        user_input = input("Please enter " + message)
        if user_input.isdigit() and int(user_input) >= 0:
            return int(user_input)  
        else:
            print("Your select: " + user_input + " - should be a non-negative number. Please try again.")
