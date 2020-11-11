i = 1
while i <= 10:
    #print(i)
    i+=1

#Usecase: Build the sample car game
    # if user input is start - then print that "car started"
    # if user input is stop - then print that 'car stopped"
    # if user input is help - then list these commands
    # quit - to quit

user_input = ""
already_started = True
already_stopped = True
while True:
    user_input = input( " > ").lower()
    if user_input == 'start':
        if not already_started:
            print("car already started")
        else:
            already_started = False
            print("car started")
    elif user_input == 'stop':
        if not already_stopped:
            print("car already stopped")
        else:
            already_stopped = False
            print("car stopped")
    elif user_input == "help":
        print('''
        if user input is start - then print that "car started"
        if user input is stop - then print that 'car stopped"
        if user input is help - then list these commands
        quit - to quit
        ''')
    elif user_input == 'quit':
        break
    else:
        print("Not understanding, try again!")