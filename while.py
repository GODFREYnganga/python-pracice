win_value = 9
Guess_count = 0
Guess_times = 3

while Guess_count < Guess_times:
    Guess = int(input("Guess: "))
    Guess_count +=1
    if Guess == win_value:
        print("You won!")
        break
else:
        print("You lose!")

    

