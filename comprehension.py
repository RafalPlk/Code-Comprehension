import random # importing external module - in this case - a collection of functions responsible for number generation

guesses_taken = 0 # variable guess_taken is set to 0

print('Hello! What is your name?') # function print prints in the console provided string
myName = input() # variable myName is set to user input

number = random.randint(1, 20) # variable number is set to value generated between (1, 20) via function randint() imported through random module
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') # function print(), prints two strings provided in it and variable myName between them

while guesses_taken < 6: # loop while is initialised when variable guesses_taken is less then 6
    print('Take a guess.') # function print prints provided string
    guess = input() # variable guess is set to user input via input function
    guess = int(guess) # new value is assign to variable guess, in this case it is converted to an integer

    guesses_taken += 1 # variable guesses_taken is increased by 1

    if guess < number: # if guess variable is less then variable number then interperter go to the next line of code
        print('Your guess is too low.') # function print, prints provieded string in console

    if guess > number:  # if guess variable is greater then number which user inputted then interperter go to the next line of code
        print('Your guess is too high.') # function print, prints provieded string in console

    if guess == number: # if variable guess equal variable number then interperter go to the next line of code
        break # while loop stops in this line

if guess == number: # if variable guess equal variable number then interperter go to the next line of code
    guesses_taken = str(guesses_taken) # variable guesses_taken is convert to string via str function
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!')  # function print(), prints three strings provided in it and vairable myName and guesses_taken between them

if guess != number: # if variable guess not equal variable number then interpreter go to the next line of code
    number = str(number) # variable number is convert to its string equivalent
    print('Nope. The number I was thinking of was ' + number) # function print prints string provided in it and adds variable number to it
