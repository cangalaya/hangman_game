import os
import random
import time

def read_data(path):
    data = []
    with open(path ,"r", encoding="utf-8") as f:
        for line in f:
            line = line.replace("\n","").upper()
            data.append(line)
    return data

def replace_capital_letters(word):
    capital_letters =  [
        ['Á','A'],
        ['É','E'],
        ['Í','I'],
        ['Ó','O'],
        ['Ú','U']]
    
    for letters in capital_letters:
        if letters[0] in word:
            word = word.replace(letters[0], letters[1])

    return word
        

def run():
    random_target = random.choice(read_data("./data/data.txt"))
    random_target =  replace_capital_letters(random_target)
    
    hidden_word = ["_" for x in range(len(random_target))]


    while (True):
        os.system("clear")
        print('BIENVENIDO A HANGMAN GAME \n\n', " ".join(hidden_word))

        if "".join(hidden_word) == random_target:
            print('\nGANASTE!!')
            break

        try:
            letter = input('\nDigite una letra: ').upper()
            if len(letter) == 0 or len(letter) > 1:
                raise ValueError('\n ----- > Digite solo una letra')
            elif letter.isnumeric():
                raise ValueError('\n ----- > No se admiten números')
        except ValueError as ve:
            print(ve)
            time.sleep(2)
            continue
        
        index_fn = 0
        list_index = []
        if letter in random_target:
            for i in random_target:
                if i == letter:
                    list_index.append(index_fn)
                index_fn += 1
        
        for i in list_index:
            hidden_word[i] = letter

        
                
if __name__ == "__main__":
    run()