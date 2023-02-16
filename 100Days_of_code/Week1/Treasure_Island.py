#Treasure Island Game
#numpy random integers for choices --> TBC
print(''' *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* ''')
direction_LR = input("You're at a crosscroad choose where you want to go Left or Right: ")
direction_LR_uniform = direction_LR.lower()

if direction_LR_uniform == "left":
    swim_boat =input("You arrive at a shore, choose whether to 'swim' across the lake or 'wait': ")
    swim_boat_uniform = swim_boat.lower()
    if swim_boat_uniform == 'wait':
        print("After a long wait, a boat arrives and take you across where you see a house with three doors.")
        door = input("\nChoose one door among the three: Yellow, Redor Green: ")
        door_uniform = door.lower()
        if door_uniform == 'yellow':
            print("CONGRATULATIONS! YOU found the treasure!")
        elif door_uniform == 'blue':
            print("You're taken captive with other treasure hunters! GAME OVER!")
        elif door_uniform == 'red':
            print("You feill for the booby trap! What a bloodwash! GAME OVER BITCH!!!")
        else:
            print("Invalid IDIOT!")
    elif swim_boat_uniform == "swim":
        print("Your impatience makes you a meal to the catfish! GAME OVER!!!")
    else:
        print("Invalid TRY AGAIN!!!")
elif direction_LR_uniform == "right":
    print("You're kidnapped for trespassing! GAME OVER!")   
else:
    print("Invalid! Try again!!!")