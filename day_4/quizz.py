from random import randint

win = False
tries = 8
computer_number = randint(20, 41)
while not win:
    while tries > 0:
        print(f'Left {tries}')
        question = int(input('Introduce a number between 20 and 40: '))

        is_range = question in range(20, 41)
        if not is_range:
            print('Out of range. Try again')
            question = int(input('Introduce a number between 20 and 40: '))

        is_lower = question < computer_number
        is_higher = question > computer_number
        tries = tries - 1
        if is_lower:
            print('Too low')
        elif is_higher:
            print('Too high')
        else:
            win = True
            print('You win! You guess the number')
            break

    if tries == 0:
        print(f'You run out of tries. The number was {computer_number}')
        break
