def fibonacci(num):
    a, b = 0, 1

    if num == 0 or  num == 1:
        return True
    
    while b < num:
        a, b = b, a + b

    return b == num

numero = int(input('Infome um número para verificar se pertence a sequencia de fibonacci'))

if fibonacci(numero):
    print(f"{numero} pertence à sequencia.")
else:
    print(f"{numero} não pertence à sequencia")

