rain = input("I see you're all psyched up for work with this unpredictable weather.\nIs it raining? Yes or no: ").lower()
if rain == 'yes':
    umbrella = input("Do you have an umbrella? Yes or no: ")
    if umbrella == 'yes':
        print("You can go outside, have a lovely day. END!")
    elif umbrella == 'no':
        print("Wait fahm!")
    else:
        print("Invalid bruv!")
else:
    print("You lucky m*therf**ker! Have a great one! END")