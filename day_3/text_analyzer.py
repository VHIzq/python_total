text = input('Introduce a text, joke or some poem: ').lower()
letters = input('Enter three letters: ').lower()

print(text)

letters_list = list(letters)
print(letters_list)

is_there = letters_list[0] in text
print(is_there)

