text = input('Introduce a text, joke or some poem: ').lower()
letters = input('Enter three letters: ').lower()

print(text)

letters_list = list(letters)
print(letters_list)

first_letter = letters_list[0]
second_letter = letters_list[1]
third_letter = letters_list[2]

first_word = text[0]
last_word = text[-1]

is_first_char = first_letter in text
is_second_char = second_letter in text
is_third_char = third_letter in text

count_first = text.count(first_letter)
count_second = text.count(second_letter)
count_third = text.count(third_letter)

num_words = text.split()
length_text = len(num_words)


num_words.reverse()
new_text = ' '.join(num_words)
print(new_text)


is_python = 'python' in text

responses = {True: 'has', False: 'don"t have'}

has_python = responses[is_python]

answer = f"""
    The first letter repeats: {count_first}, the second one: {count_second} and the third one: {count_third}.
    The text has: {length_text} words. The first letter is {first_word} and the last one is: {last_word}.
    The reverse text is: {new_text}.
    Your text {has_python} the word Python.
"""

print(answer)
