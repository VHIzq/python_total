from random import choice

words = ['movies', 'car', 'lolipoop', 'smartband', 'developer']

select_word = choice(words)
print(select_word)

play = True

def check_letter():
    lifes = 6
    has_letter = ask in select_word
    if not has_letter:
        lifes -= 1
    print(f'lifes: {lifes}')
def change_spaces():


while play:
    ask = input('Enter a guess letter: ').lower()
    check_letter()


