for numero in range(0, 101):
    Impar = {}
    Par = []
    if numero % 2 == 0:
        Impar.append(numero) and print('= Impar')

    elif numero % 2 == 1:
        Par.append(numero) and print('= Par')
    print(f' {Impar,Par}',end=" ")