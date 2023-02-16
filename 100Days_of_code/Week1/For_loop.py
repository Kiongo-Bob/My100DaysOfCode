# # lisit = [344,453,345,345,3453,42,4]
# # for num in lisit:
# #     print(num)
    
# # for i, num in enumerate(lisit):
# #     print(i+1, num)
    
# student_heights = input("Enter the student heights: ").split()

# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
    
# total_height = 0
# total_students = 0
# for height in student_heights:
#     total_height += height
#     total_students += 1

# mean_height = round(total_height/total_students)
# print(f"The mean height of students is: {mean_height}.")

# # For Loop without usig max and min functions --> Output the greatest value
numbers = input("Enter the numbers you want to check: ").split()
highest_number = 0

for n in range(0, len(numbers)):
    numbers[n] = int(numbers[n])
for num in numbers:
    if num > highest_number:
        highest_number = num
print(highest_number)