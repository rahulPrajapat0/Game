print("Game Start!")

computer=["water","snake","gun"]
x=input("Enter your choice (water, snake, gun): ")
if x == "water":
    print("You chose water.")
elif x == "snake":
    print("You chose snake.")
elif x == "Gun":
    print("You chose Gun.")

import random
computer=random.choice(computer)
print(f"Computer chose: {computer}")


if x=="water" and computer=="gun":
    print("You win!")
elif x=="snake" and computer=="water":
    print("You win!")
elif x=="gun" and computer=="snake":
    print("You win!")
elif x == computer:
    print("It's a tie!")
elif (x == "water" and computer == "snake") or \
     (x == "snake" and computer == "gun") or \
     (x == "gun" and computer == "water"):
    print("You lose!")
else:
    print("Invalid choice. Please choose water, snake, or gun.")