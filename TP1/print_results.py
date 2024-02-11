def results(aptos, dicionario_idades, modalidades):
    #Imprimir Resultados
    print(f'\nResultados\n')
    print(f'Total de atletas aptos: {aptos}\n')

    #Ordena o dicionário anterior e imprime-o
    print('Intervalos de Idades')
    dicionario_ordenado = dict(sorted(dicionario_idades.items()))
    for key in dicionario_ordenado:
        print(f'[{key*5}...{key*5+4}] :: {dicionario_ordenado[key]} atletas')

    #Ordenar as modalidades e imprime-as
    modalidades_ordenado = sorted(modalidades)
    print(f'\nModalidades: \n{modalidades_ordenado}')