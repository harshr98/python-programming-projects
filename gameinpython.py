print("Welcome to my choice based game")

name = input("Please give us your name. What should we call you? ")
print(f"Welcome to the game {name}")

choice = input("Do you want to play this game? ")
if choice.lower() == "yes":
    print("Thank you", name, "!")
else: print(f"sad noices, {name}!")


# Game Logic starts below:

question1 = input("You look at the sky and see sun, what is it? a day or night? ")
if question1.lower() == "day":
    print(f"That's correct anwer {name}!")
elif question1.lower() == "night":
    print(f"Correct! {name}")
else: print("incorrect answer! you have skill issue {name}!")
   
question2 = input(f"What is your favorite sport {name}? ").lower()

if question2 == "football":
    print("yes man!")
elif question2 == "american Rugby":
    print("not bad, not bad at all {name}!")
elif question2 == "baseball":
    print == ("Noiceeee!")
else: print("Good luck with your life man! you need to watch some real sports my friend!")

# Copy the structure of top two questions and list more questions below.

# End

print (f"Well my friend here is the end of the game, I hope you enjoyed our little game {name}") 
print("Do come to play more tho.")