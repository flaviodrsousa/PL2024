import sys
import re


def somador(linhas):
    sum = 0
    on_off = 0 #Começa desligado (0)

    for linha in linhas:
        correspondencia = re.findall(r'(\d+|on|off|=)', linha, re.IGNORECASE)

        if correspondencia:
            for dado in correspondencia:
                if(dado.lower() == "on"): on_off = 1;
                else:
                    if(dado.lower() == "off"): on_off = 0;
                    else:
                        if(dado.lower() == "="):
                            if(on_off == 1): print("Soma = " + str(sum))
                        else:
                            if(on_off == 1):
                                sum += int(dado)
                            

def main(inp):
    with open(inp[1], 'r') as arquivo:
        linhas = arquivo.readlines()
    somador(linhas)

if __name__ == "__main__":
    main(sys.argv)