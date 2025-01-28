import json

def calcular_faturamento(faturamentos):
    faturamentos_validos = [dado['valor'] for dado in faturamentos if dado['valor'] > 0]
    
    if len(faturamentos_validos) == 0:
        return {
            "menor_valor": 0,
            "maior_valor": 0,
            "media_acima": 0
        }

    menor_valor = min(faturamentos_validos)
    maior_valor = max(faturamentos_validos)
    media_faturamento = sum(faturamentos_validos) / len(faturamentos_validos)

    media_acima = sum(1 for valor in faturamentos_validos if valor > media_faturamento)

    return {
        "menor_valor": menor_valor,
        "maior_valor": maior_valor,
        "media_acima": media_acima
    }

def ler_json(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        return json.load(file)

def main():
    nome_arquivo = "mock.json"
    faturamentos = ler_json(nome_arquivo)
    resultado = calcular_faturamento(faturamentos)

    print(f"Menor faturamento: R$ {resultado['menor_valor']:.2f}")
    print(f"Maior faturamento: R$ {resultado['maior_valor']:.2f}")
    print(f"Número de dias com faturamento superior à média: {resultado['media_acima']}")

if __name__ == "__main__":
    main()
