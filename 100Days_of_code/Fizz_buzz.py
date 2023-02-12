#Fizz number divisible by 3, buzz number divisible by 5 and fizbuzz a number divisible by 15.
for number in range(1,101):
    if number % 15 == 0:
        print("Fizzbuzz")
    elif number % 5== 0:
        print("Buzz")
    elif number %  3== 0:
        print("Fizz")
    else:
        print(number)
        