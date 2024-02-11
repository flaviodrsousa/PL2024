import sys
import print_results

def calculate(caminho_do_arquivo):
    aptos = 0
    dicionario_idades = {}
    modalidades = []
    
    with open(caminho_do_arquivo, 'r') as arquivo:

        # Abre cada linha
        for linha in arquivo:
            tokens = linha.split(',')

            # Verifica se o atleta está apto ou não
            if tokens[12] == 'true\n':
                aptos += 1

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
    
    print_results.results(aptos, dicionario_idades, modalidades)