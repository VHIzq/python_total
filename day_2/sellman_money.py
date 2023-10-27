name = input('WHats your name: ')
sales = float(input('How much did you sell this month? $'))

calc = round((sales * 0.13), 2)
answer = f'Hi, {name}, your money is {calc}'
print(answer)