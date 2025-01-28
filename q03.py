import json

def analise_faturamento(faturamentos):
    menor_valor = min(faturamentos)
    maior_valor = max(faturamentos)
    media_faturamento = sum(faturamentos) / len(faturamentos)

    media_acima = 0

    for valor in faturamentos:
        if valor > media_faturamento:
            media_acima += 1

    return {
        "menor_valor": menor_valor,
        "maior_valor": maior_valor,
        "media_acima": media_acima
    }


def ler_json(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        data = json.load(file)
    return data['faturamento_diario']

nome_arquivo = "mock.json"

faturamentos = ler_json(nome_arquivo)

r = analise_faturamento(faturamentos)

print(f"Menor faturamento: {r['menor_valor']}")
print(f"Maior faturamento: {r['maior_valor']}")
print(f"Número de dias com faturamento superior à média: {r['media_acima']}")
