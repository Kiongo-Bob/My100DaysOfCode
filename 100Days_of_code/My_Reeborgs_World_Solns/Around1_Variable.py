#A perimeter go around, 4 repetitions
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while is_facing_north() != True:
    turn_right()
turn_right()
l = int(input("Enter the length: "))
w = int(input("Enter the width: "))
p = 2 * (l+w)
i = 1
for i in range(1,p-3):
   print(i)
   if front_is_clear() == True:
        move()
   else:
       turn_left()
       move()     
