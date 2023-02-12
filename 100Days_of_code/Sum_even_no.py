# This prgram adds the even numbers from 1 to 100 inclusive of 1 and 100
sum_even = 0
for num in range(1,101): #rnage(2,101,2)
    if num % 2 == 0:
        sum_even += num
    else:
        pass
print(sum_even)