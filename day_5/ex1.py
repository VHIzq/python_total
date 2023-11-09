def devolver_distintos(lista):
    greater = max(lista)
    medium = 0
    smaller = min(lista)

    for num in lista:
        if num != greater and num != smaller:
            medium = num
    response = f'Biggest value: {greater}, mediun value: {medium}, smaller one: {smaller}'
    print(response)


devolver_distintos([100, 6, 20])
