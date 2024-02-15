import sys

def calculate(caminho_do_arquivo):
    aptos = 0
    inaptos = 0
    dicionario_idades = {}
    modalidades = []
    
    with open(caminho_do_arquivo, 'r', encoding='utf-8') as arquivo:

        # Abre cada linha
        for linha in arquivo:
            tokens = linha.split(',')

            # Verifica se o atleta está apto ou não
            if tokens[12] == 'true\n': aptos += 1
            else: inaptos += 1

            if tokens:
                try:
                    idade = int(tokens[5])
                    intervalo = (idade) // 5  # Ajustado para corrigir o cálculo do intervalo

                    if intervalo in dicionario_idades:
                        dicionario_idades[intervalo] += 1
                    else:
                        dicionario_idades[intervalo] = 1

                    if tokens[8] not in modalidades: 
                        modalidades.append(tokens[8])

                except ValueError:
                    print('Não foi possível separar em tokens')
                    
    inaptos -= 1 #Retira a primeira linha que é a caracterização de cada parâmetro
    #Imprimir Resultados
    print(f'\nResultados\n')
    print(f'Total de atletas: {aptos+inaptos}')
    print(f'Nº de atletas aptos: {aptos} ({round(100 * (aptos/(aptos+inaptos)), 2)}%)')
    print(f'Nº de atletas inaptos: {inaptos} ({round(100 * (inaptos/(aptos+inaptos)), 2)}%)')

    #Ordena o dicionário anterior e imprime-o
    print(f'\nIntervalos de Idades')
    dicionario_ordenado = dict(sorted(dicionario_idades.items()))
    for key in dicionario_ordenado:
        print(f'[{key*5}...{key*5+4}] :: {dicionario_ordenado[key]} atletas')

    #Ordenar as modalidades e imprime-as
    modalidades_ordenado = sorted(modalidades, key=str.casefold)
    print(f'\nModalidades: \n{modalidades_ordenado}')


if __name__ == "__main__":
    caminho_do_arquivo = input('Digite o caminho para o arquivo:')
    calculate(caminho_do_arquivo)


