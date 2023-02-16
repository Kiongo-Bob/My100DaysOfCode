# Small pizza is KShs 350 Size: S
# Medium pizza is Kshs 550 Size: M
# Large pizza is Kshs 750 Size: L
# Extra cheese for any pizza is : Kshs 100
# Add pepporoni for small pizza 100 for medium and large Kshs 200 
# Code to calculate the final bill

pizza_size = input("Hello, which size would you like? \nS, M or L:  ")
bill = 0
wants_cheese = input("Would you like some extra cheese? Y or N: ")
wants_pepporoni = input("While at it, would you like some Pepporoni? Y or N: ")
if pizza_size == "S":
    bill = 350
    print("You've selected 'S' for small.")
elif pizza_size == "M":
    bill = 550
    print("You've selected 'M' for medium.")
elif pizza_size == "L":
    bill = 750
    print("You've selected 'L' for large.")
else:
    print("Invalid, Please try again.")

if pizza_size == "S" and wants_pepporoni == "Y":
    bill += 100   
if pizza_size == "M" or pizza_size == "L" and wants_pepporoni == "Y":
    bill += 200
if wants_cheese == 'Y':
    bill +=100
print(f"Your bill is Kshs {bill}. Enjoy your meal.")
