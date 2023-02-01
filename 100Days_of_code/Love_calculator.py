# Typical Ms Angela
# Based on the words TRUE LOVE, enter your name and your crush's name and have the program check for
# how many times the letters T, R, U, E, L, O, V and E appear in your names.
name1 = input("Enter your name: ")
name2 = input("Enter your name: ")
name_total = name1+name2
name_total.lower()

t = name_total.count("t") 
r = name_total.count("r")
u = name_total.count("u")
e = name_total.count("e")
l = name_total.count("l")
o = name_total.count("o")
v = name_total.count("v")
e = name_total.count("e")

name_tens = (t + r + u + e )
name_ones = (l + o + v + e)

name_tens_str = str(name_tens)
name_ones_str = str(name_ones)
score = name_tens_str+name_ones_str
score_int = int(score)

print(f"T occurs {t} times, R {r} times, U {u} times and E {e} times.")
print(f"L occurs {l} times, O {o} times, V {v} times and E {e} times.")
if score_int <=10 or score_int >= 90:
    print(f"Your score is {score}, you go together like Life and Death.")
elif score_int >= 40 and score_int <=50:
    print(f"Your score is {score}, you're alright together")
else:
    print(f"Your score is {score}.")
