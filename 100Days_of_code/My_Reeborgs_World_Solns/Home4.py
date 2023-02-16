def turn_right():
    turn_left()
    turn_left()
    turn_left()

while is_facing_north() != True:
    turn_right()
    
while at_goal() == False:
    
    if front_is_clear() == True:
        move()
    elif wall_in_front() and wall_on_right() == True:
        turn_left()
        move()
    else:
        turn_right()
        move()
