import random

def rolar_dado(lados):
    """Função para rolar um dado com um número especificado de lados."""
    return random.randint(1, lados)

def main():
    print("Bem-vindo ao simulador de rolagem de dados!")
    
    while True:
        # Solicitar ao usuário o número de dados e o número de lados
        num_dados = int(input("Quantos dados você quer rolar? "))
        num_lados = int(input("Quantos lados tem o dado? "))
        
        resultados = []
        for _ in range(num_dados):
            resultados.append(rolar_dado(num_lados))
        
        # Exibir os resultados
        print(f"Resultados da rolagem dos {num_dados} dados de {num_lados} lados: {resultados}")
        
        # Perguntar se o usuário deseja rolar novamente
        jogar_novamente = input("Você quer rolar os dados novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar!")
            break

if __name__ == "__main__":
    main()
