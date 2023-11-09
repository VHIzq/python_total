def contar_primos(*args):
    counter = 0
    for item in args:
        for i in range(2, item):
            is_divisible = item % i == 0
            if is_divisible:
                break
            else:
                counter += 1
    return counter
print(contar_primos(5, 3, 15))
