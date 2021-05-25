# Guessing number project on python
# Balvinder Singh and Sehajpreet Kaur

# 1. random number generator library function
import random


# 2. greetings to user
print("Hello! What is your name? By The Way, I hope your day went well")

# 3. user input
myName = input()


print("Nice to meet you, " + myName + ", lets play a guessing game")
l = int(input("Enter a lower limit: "))
u = int(input("Enter a upper limit: "))
number = random.randint(l,u)
print("I am thinking of a number between", l, "and" , u  ," you have to guess it in within 5 guesses , or you will loose the game\n")

# 4. initialising myguess to 0 and will increase after guessing the  number
myguess = 0
score = 0


# 5. count is keeping a check to warn and pressurize the user to use his/her mind smartly :)
#    making it more challenging
count = 5


# 6. conditons for guessing
while myguess <= 5:
    print("Take a guess, beware only", count , "guesses left") 
    guess = int(input())

    # 7. increasing my guess count to break it after 5
    myguess += 1

    # 8. condition for guessing the  game
    #  this condition is used to stop the loop at last without going into checking 
    if myguess == 5:        
        break
    if guess < number:
        print("guess is low , think higher number")
        count -= 1
        score = 0
    if guess > number:
        print("Nope too high , think lower number")
        count -=1
        score = 0
    if guess == number: # number is guessed , break from while loop termination
        print("Seriously , you beat me. Wow")
        
        break

# 9. screen display 
if guess == number:
    score += count
    # 10. changing int to string for display
    myguess = str(myguess)
    print("Good job, " + myName + "! You guessed it in " + myguess + " guesses!")
    print("Your total score is " ,score)

    
if guess != number:
    score = 0
    number = str(number)
    print("Nope , you lost the game . The number I had in mind was: " , number, "\nBetter Luck Next Time")
    print("Your total score is " ,score)

