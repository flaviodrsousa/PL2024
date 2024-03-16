import json
import datetime
import ply.lex as lex

def adicionar_subtrair_moeda(nova_moeda, char):
    global conta
    moeda_atual_centimos = converter_para_centimos(conta)
    nova_moeda_centimos = converter_para_centimos(nova_moeda)
    if char == '+':
        total_centimos = moeda_atual_centimos + nova_moeda_centimos
    else : total_centimos = moeda_atual_centimos - nova_moeda_centimos
    
    if total_centimos >= 0:
        total_moeda = formatar_para_moeda(total_centimos)
        conta = total_moeda

def converter_para_centimos(moeda):
    if moeda.endswith('e'):
        return int(float(moeda[:-1]) * 100) 
    elif moeda.endswith('c'):
        moeda = moeda[:-1]
        if 'e' in  moeda:
            partes = moeda.split('e')
            return int(partes[0]) * 100 + int(partes[1])
        else: return int(moeda)
    else:
        raise ValueError("Formato de moeda inválido")

def formatar_para_moeda(centimos):
    euros = centimos // 100
    centimos_restantes = centimos % 100
    return f"{euros}e{centimos_restantes:02d}c"


data_atual = datetime.datetime.now()
data_formatada = data_atual.strftime("%d/%m/%Y") 


tokens = ('MOEDA', 'LISTAR', 'SELECIONAR', 'SAIR')
def t_MOEDA(t):
    r'MOEDA (.*)'
    global conta
    t.value = t.value[6:]
    adicionar_subtrair_moeda(t.value, '+')
    print("Saldo = " + conta)

    return t

def t_SAIR(t):
    r'SAIR'
    t.value = 0
    print("Até à próxima")
    return t

def t_LISTAR(t):
    r'LISTAR'
    print("| {:<6} | {:<10} | {:<12} | {:<6} |".format("cod", "nome", "quantidade", "preço"))
    print("-" * 47)
    for chave, lista in stock.items():
        for valor in lista:
            print("| {:<6} | {:<10} | {:<12} | {:<6} |".format(valor["id"], valor["nome"], valor["quantidade"], valor["preco"]))
            print("-" * 47)
    return t

def t_SELECIONAR(t):
    r'SELECIONAR (.*)'
    global conta
    check = conta
    t.value = t.value[11:]
    for chave, lista in stock.items():
        for value in lista:
            if value["id"] == t.value:
                if(value["quantidade"] > 0):
                    adicionar_subtrair_moeda(value["preco"], '-')
                    if(check != conta):
                        value["quantidade"] -= 1
                        print("Pode retirar o produto dispensado \"" + value["nome"] + "\"")
                        print("Saldo = " + conta)
                    else:
                        print("Saldo insufuciente para satisfazer o seu pedido")
                        print("Saldo = " + conta + "; Pedido = " + value["preco"])
                else: 
                    print("Lamento, mas já não temos stock de \"" + value["nome"] + "\"")
                    
    
    return t

t_ignore = ' \t'

def  main():
    global stock 
    global conta
    conta = "0e"
    with open('TP5/stock.json', 'r') as arquivo:
        stock = json.load(arquivo)
    print(stock)
    print(data_formatada + ", Stock carregado, Estado atualizado.\n")

    lexer =  lex.lex()
    status = 1
    while(status):
        frase = input("maq:")
        lexer.input(frase)
        tok = lexer.token()
        if tok and tok.value == 0: 
            status = 0

    print("Pode retirar o troco: " + conta)

    with open('TP5/stock.json', 'w') as arquivo:
        json.dump(stock, arquivo, indent=4)




if __name__=='__main__':
    main()

