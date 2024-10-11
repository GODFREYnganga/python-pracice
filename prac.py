command = ""
started = False
while command != True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already Started!")
        else:
            started = True
            print("Car started ... Ready to go !")
    elif command == "stop":
        if not started:
            print("Car is already Stopped!.")
        else:
            started = False
            print("Car Stopped!")

    elif command == "help":
        print("""
Start - to start the car 
stop - to stop the car 
Quit -to exit """)
    else:        
        print("I don't understand that ...")
