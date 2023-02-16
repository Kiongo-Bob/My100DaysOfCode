# This program asks for your names and randomly chooses someone to pay the bill.
# import random

# names = input("Each person should enter one name separated with a comma: ").split(",")
# # name_list = [names] Do away with this loc as it creates a list inside a list
# # num_list =len(names)-1
# # rand_num = random.randint(0,num_list)
# # name_sponsor = names[rand_num]
# # print(num_list)
# # print(rand_num)
# name_sponsor = random.choice(names)
# print(f"{name_sponsor} is paying the bill today!")

#Nested list
fruits = ['Strawberries','Nectarines','Apples','Grapes','Peaches','Cherries','Pears']
vegetables = ['Spincah', 'Kale','Tomatoes','Celery','Potatoes']
dirty_dozen = [fruits,vegetables]
print(dirty_dozen[1][2])