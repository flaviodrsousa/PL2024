# TPC3: Somador on/off
**Autor:** Flávio David Rodrigues Sousa
**Número de Aluno:** 100715

## Descrição do trabalho realizado

### Objetivos
Para a realização deste trabalho prático foi essencial estudar e dar continuidade à utilização de expressões regulares com o objetivo de "retirar" do ficheiro as partes essenciais ao programa. Sendo assim, foram delimitados 2 objetivos:

1. ****Aplicação de Expressões Regulares****
Com o objetivo de melhor entender e aplicar os conteúdos lecionados nas aulas, foi dado prioridade à implementação de expressões regulares na realização deste trabalho.

2. **Garantir o correto funcionamento do programa**
Por fim, é essencial o programa ser capaz de lidar com os diferntes ficheiros e dados, filtrar e processar corretamente a informação extraída devolvendo, sempre que solicitado, o valor da respetiva soma;

## Métodos Implementados
1.**Função somador**
Este é o único método do programa. Ele recebe as linhas de um determinado ficheiro e interpretada cada uma;
- Em primeiro lugar, temos uma expressão regular responsável por extrair todas as sequências de números, "ON", "OFF" e "=", sendo usada a flag *re.IGNORECASE* para ignorar maiúsculas e minúsculas.
`r'(\d+|on|off|=)'` É usada a função `re.findall()` para agrupar em lista todas as sequências compatíveis;
- Em seguida, temos a interpretação de cada elemento da lista obtiva anteriomente; Se for um "=" imprime a soma atual; se for "ON" ativa a soma/impressão; se for "OFF" suspende a soma/impressão; se não for nenhuma destas é porque é uma sequência de números que é, de seguida, somada à respetiva variável, caso o programa esteja ativo, isto é, tenho recebido um "ON" anteriormente.

**Nota** A variável *sum* nunca é resetada, isto significa que, quando encontro um "ON" ou um "OFF" não resetamos a variável *sum*, apenas ativamos ou bloqueamos respetivamente, a capacidade de somar e imprimir resultados.

## Conclusão
O presente trabalho foi conduzido com sucesso, alcançando os objetivos estabelecidos de maneira eficaz e eficiente. Durante o processo, foram definidos dois principais objetivos delimitados anteriormente na secção *Objetivos*.
Foi denotada uma dificuldade na implementação das expressões regulares.
Em suma, o programa cumpre os requisitos para a sua execução! É servido de exemplo o ficheiro `exemplo.txt`que contem uma série de linhas e que é corretamente interpetado e analisado pelo programa.

`Para a execução do programa é necessário passar, como argumento, o path para o ficheiro pretendido`