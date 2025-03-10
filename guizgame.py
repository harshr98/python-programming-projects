print("Welcome to my choice based game")

name = input("Please give us your name. What should we call you? ")
print(f"Welcome to the game {name}")

choice = input("Do you want to play this game? ")
if choice.lower() == "yes":
    print("Thank you", name, "!")
else: print(f"sad noices, {name}!")

score = 0

# Game logic 

# Round 1
print(f"1. What is the largest continent on the earth {name}?")
print("A. Asia B. Europe C. North America D. Africa")
print(f"your current score: {score}") 

answer = input("put your answer here: ").lower()
if answer == "asia" or answer == "a":
    print(f"correct answer {name}!, you received 1 point!")
    score += 1
else: 
    score -= 1
    print(f"Wront answer {name}, you lost 1 point.")

print(f"After the end of round 1, your score is {score}")
print(f"in terms of total result by percentage, you have scored: {(score/1)*100}%")

# Round 2
print(f"2. What is the largest country in the world {name}?")
print("A. United States B. Russia C. China D. India ")
print(f"your current score: {score}") 

answer = input("put your answer here: ").lower()
if answer == "russia" or answer == "b":
    print(f"correct answer {name}!, you received 1 point!")
    score += 1
else: 
    score -= 1
    print(f"Wront answer {name}, you lost 1 point.")

print(f"After the end of round 2, your score is {score}")
print(f"in terms of total result by percentage, you have scored: {(score/2)*100}%")

# Round 3
print(f"3. Which country is the largest in the continent of Europe {name}?")
print("A. Ukraine B. Russia C. Germany D. Spain")
print(f"your current score: {score}") 

answer = input("put your answer here: ").lower()
if answer in "b" or answer == "russia":
    print(f"correct answer {name}!, you received 1 point!")
    score += 1
else: 
    score -= 1
    print(f"Wront answer {name}, you lost 1 point.")

print(f"After the end of round 3, your score is {score}")
print(f"in terms of total result by percentage, you have scored: {(score/3)*100}%")

# Round 4
print(f"4. What is the Capital city of the United States {name}?")
print("A. New York B. Washington DC C. Boston D. Salt lake city")
print(f"your current score: {score}") 

answer = input("put your answer here: ").lower()
if answer in "b" or answer == "washington dc":
    print(f"correct answer {name}!, you received 1 point!")
    score += 1
else: 
    score -= 1
    print(f"Wront answer {name}, you lost 1 point.")

print(f"After the end of round 4, your score is {score}")
print(f"in terms of total result by percentage, you have scored: {(score/4)*100}%")


# Round 5
print(f"5. What is the Largest Economy in the World in terms of PPP {name}?")
print("A. United States B. Russia C. China D. India")
print(f"your current score: {score}") 

answer = input("put your answer here: ").lower()
if answer == "c" or answer == "china":
    print(f"correct answer {name}!, you received 1 point!")
    score += 1
else: 
    score -= 1
    print(f"Wront answer {name}, you lost 1 point.")

print(f"After the end of round 5, your score is {score}")
print(f"in terms of total result by percentage, you have scored: {(score/5)*100}%")

# Round 6
print(f"6. What is the Largest Ocean in the World {name}?")
print("A. Arabic B. Atlantic C. Pacific D. Indian")
print(f"your current score: {score}") 

answer = input("put your answer here: ").lower()
if answer == "c" or answer == "pacific":
    print(f"correct answer {name}!, you received 1 point!")
    score += 1
else: 
    score -= 1
    print(f"Wront answer {name}, you lost 1 point.")

print(f"After the end of round 6, your score is {score}")
print(f"in terms of total result by percentage, you have scored: {(score/6)*100}%")

# Round 7
print(f"7. What is the largest country by population {name}?")
print("A. United States B. Russia C. China D. India")
print(f"your current score: {score}") 

answer = input("put your answer here: ").lower()
if answer == "d" or answer == "india":
    print(f"correct answer {name}!, you received 1 point!")
    score += 1
else: 
    score -= 1
    print(f"Wront answer {name}, you lost 1 point.")

print(f"After the end of round 7, your score is {score}")
print(f"in terms of total result by percentage, you have scored: {(score/7)*100}%")

print(f"Thank you for playing with us {name}, This is he end of the game, You got {score} points and your current score is {(score/7)*100}%")
