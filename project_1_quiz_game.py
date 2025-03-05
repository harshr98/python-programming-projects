print("Welcome to our Computer Quiz Game!")

player_name = input("What is your name? ")
print("Welcome ", player_name)

playing = input("Do you want to play? ")
print(playing)

if playing.lower() != "yes":
    quit()

# Start of the Game
print("okay! lelts Goooooo!")
score = 0

# Question 1
answer = input("1. Question1? ")
if answer.lower() == "answer1":
    print('Correct!')
    score  += 1
else: 
    print("Incorrect! you have SKILL issue!") 
    score -= 1

# Question 2
answer = input("2. Q2? ")
if answer.lower() == "A2":
    print('Correct!')
    score  += 1
else: 
    print("Incorrect! you have SKILL issue!") 
    score -= 1

# Question 3
answer = input("3. Q3 ")
if answer.lower() == "A3":
    print('Correct!')
    score  += 1
else: 
    print("Incorrect! you have SKILL issue!") 
    score -= 1

# Question 4
answer = input("4. Q4? ")
if answer.lower() == "A4":
    print('Correct!')
    score  += 1
else: 
    print("Incorrect! you have SKILL issue!") 
    score -= 1

# Question 5
answer = input("5. Q5? ")
if answer.lower() == "A5":
    print('Correct!')
    score  += 1
else: 
    print("Incorrect! you have SKILL issue!")
    score -= 1

print(player_name, "You got " + str(score) + " Questions correct!")
print(player_name, "You got " + str((score/5) * 100) + " %!")
