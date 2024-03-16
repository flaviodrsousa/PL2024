# TPC4: Máquina de Vending
**Autor:** Flávio David Rodrigues Sousa
**Número de Aluno:** 100715

## Descrição do trabalho realizado

### Objetivos
Neste trabalho de casa foi-nos pedida a implementação de um pequeno programa capaz de lidar com vendas e tratamentos de moedas.
Para isso, foram definidos 2 objetivos principais:
- Implementar o programa de acordo com a matéria lecionada nas aulas;
- Garantir o correto funcionamento do programa

## Métodos Implementados
**1. Definição dos tokens:**
Nesta primeira fase foram definidos os principais tokens a utilizar: SELECIONAR, LISTAR, MOEDA e SAIR.
Para cada um deles foi definida a respetiva regra.

**2. Funções Auxiliares:**
Foram criadas funções para o tratamento das moedas recebidas. Para o efeito, o programa faz a conversão da moeda que entrou para cêntimos, somo à variável global e converte para o formato de leitura pedido.
Ao mesmo tempo, a biblioteca *json* é usada na medida em que, é necessária a utilização de um ficheiro *.json* para a interpretação e carregamento de todo o stock presente na máquina.

**6. Função Principal (main):**
A função main, por sua vez, é bastante similar ao da realizada no TP4. Utiliza um lexer e interpreta, através de um loop que apenas é interrompido quando o *status* fica a 0, todas as frases passadas pelo utilizador.

## Conclusão
Em resumo, acredito que os objetivos tenham sido alcançados com sucesso garantindo o correto funcionamento de todo o programa.A capacidade do código em identificar e processar tokens é evidenciada pelo loop de impressão que exibe os tokens correspondentes ao analisar uma frase de entrada. Assim, o analisador léxico desenvolvido cumpre de forma satisfatória os requisitos estabelecidos para a análise básica de comandos SQL.