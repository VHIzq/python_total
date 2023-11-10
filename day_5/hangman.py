from random import choice
chars = ''


def check_letter(word_, life_):
    has_letter = ask in word_
    if not has_letter:
        life_ -= 1
        print(f'''Wrong! 
        Lost one life! 
        lifes: {life_}''')


def generate_spaces(word_):
    length_spaces = len(word_)
    spaces_char = '_' * length_spaces
    chars = spaces_char
    print(spaces_char)

def replace_spaces(spaces, char):
    chars.replace('_', char)


play = True
lifes = 6
words = ['movies', 'car', 'lolipoop', 'smartband', 'developer']
select_word = choice(words)

print('Welcome to Hangman. Guess the word before your tries run out')
generate_spaces(select_word)
print(select_word)

while play:
    ask = input('Enter a guess letter: ').lower()
    check_letter(select_word, lifes)

