#A perimeter go around, 4 repetitions
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while is_facing_north() != True:
    turn_right()
turn_right()
i = 1
for i in range(1,5):
   while front_is_clear() == True:
        move()
   turn_left()   
