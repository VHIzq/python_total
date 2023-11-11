from random import *

lifes = 6
play = True
words = ['microsoft', 'apple', 'netflix', 'facebook', 'alphabet']
alphabet = list(map(chr, range(97, 123)))
guesses = []


def get_random_word(list_words):
    word = choice(list_words)
    return word


def get_word_underscores(word_):
    underscores = '_' * len(word_)
    return underscores


def get_letter():
    letter_ = input('Guess a letter: ').lower()
    return letter_


def is_valid_letter(letter_):
    is_string = str == type(letter_)
    is_letter = letter_ in alphabet
    return is_string and is_letter


def has_letter_in_word(letter_, word_):
    has_letter = letter_ in word_
    return has_letter


def replace_underscores(underscores_, letter_: str, right_letter: bool):




word = get_random_word(words)
print(word)
word_underscores = get_word_underscores(word)
print(word_underscores)
letter = get_letter()
valid_letter = is_valid_letter(letter)
is_right_letter = has_letter_in_word(letter, word)


def game(lifes_):
    if is_right_letter:
        print('Good job')
    else:
        lifes_ -= 1
        guesses.append(letter)
        res = f' Lifes: {lifes_} / Wrong letters: {guesses}'
        print(res)


game(lifes)



