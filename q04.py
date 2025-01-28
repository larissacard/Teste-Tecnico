def percentuais(faturamento):
    total = sum(faturamento.values())

    porcentagens = {}
    for estado, valor in faturamento.items():
        porcentagens[estado] = (valor / total) * 100

    return porcentagens

faturamento_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

r = percentuais(faturamento_estado)

for estado, porcentagem in r.items():
    print(f"{estado}: {porcentagem:.2f}%")
