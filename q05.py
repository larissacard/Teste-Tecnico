def inverter(string):
    string_intervida = ''

    i = len(string) - 1

    while i >= 0:
        string_intervida += string[i]
        i -= 1

    return string_intervida

palavra = input("Informe uma string: ")

r = inverter(palavra)

print(f"A string invertida é: {r}")
