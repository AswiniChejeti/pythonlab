#Infinite loop + break
while True:          # infinite loop
    user_input = input("Type 'stop' to end: ")

    if user_input == "stop":
        break        # exits the loop

    print("Looping...")
