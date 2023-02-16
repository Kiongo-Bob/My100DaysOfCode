import random as rd
choice = input("Welcome!\nThis game allows you to choose between rock: 1, paper: 2 and scissors: 3.")
available_choices = ['gotcha','rock','paper','scissor']
comp_choice = rd.randint(1,3)

available_choices[1] = 'rock'
available_choices[2] = 'paper'
available_choices[3] = 'scissors'


if choice == comp_choice:
    print(f"You chose: {comp_choice}\nThat's a Draw!")
elif choice == 1 and comp_choice ==3:
    print("You crushed 'em scissors!\nYou win!")
elif choice ==2 and comp_choice == 1:
    print("You rendered the rock blind!\nYou win!")
elif choice == 3 and comp_choice == 2:
    print("Mr. shredder!\nYou win!")
else:
    print(f"Computer chose: {comp_choice}You lose, try again!")