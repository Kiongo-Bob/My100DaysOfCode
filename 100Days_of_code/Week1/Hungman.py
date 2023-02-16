import random as rd
word_list = ['function', 'generates', 'word', 'specified', 'length','repeatedly', 'selecting','random', 'letter', 'from', 'letters', 'string', 'concatenating', 'result']
chosen_word = rd.choice(word_list)
print(chosen_word)
print(type(chosen_word))
guess_letter = input("Enter a letter: ").lower()
hidden_word = ""
i = 0

while True:
    for i in range(len(chosen_word)): 
        hidden_word += '_'
        hidden_word = list(hidden_word)
        indx = int(chosen_word.index(guess_letter))
        word = hidden_word.insert(indx,guess_letter)
    print(hidden_word)
    break
    # if guess_letter in (chosen_word):
    #     print("Correct")
    # print("Wrong")