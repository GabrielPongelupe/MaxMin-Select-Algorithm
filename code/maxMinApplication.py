from maxMinAlgorithm import find_min_max

def executar_teste(arr):
    min_val, max_val = find_min_max(arr, 0, len(arr) - 1)
    print(f"Array: {arr} -> Mínimo: {min_val}, Máximo: {max_val}")

def main():
    # Novos casos de teste
    casos_de_teste = {
        "Lista Pequena": [42, 17, 8],
        "Números Decrescentes": [50, 40, 30, 20, 10],
        "Elemento Único": [-99],
        "Números Misturados": [15, -3, 22, 0, 7, -8],
        "Valores Grandes": [100000, 500000, 999999, 250000, 750000]
    }

    print("Rodando novos testes...\n")
    
    for nome, array in casos_de_teste.items():
        print(f"{nome}:")
        executar_teste(array)
        print("-" * 30)

if __name__ == "__main__":
    main()

