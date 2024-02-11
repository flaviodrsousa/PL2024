def results(aptos, inaptos, dicionario_idades, modalidades):
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
    modalidades_ordenado = sorted(modalidades)
    print(f'\nModalidades: \n{modalidades_ordenado}')