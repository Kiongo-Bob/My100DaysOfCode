#Factorial using a while loop
num = int(input("Enter a number whose factorial you're calculating: "))
in_num = num
factorial = 1
while num > 1:
    factorial *= num
    num -= 1
print(f"({in_num}!) which is read as {in_num} factorial is equal to {factorial}.")