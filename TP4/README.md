# TPC3: Interpretador Léxico
**Autor:** Flávio David Rodrigues Sousa
**Número de Aluno:** 100715

## Descrição do trabalho realizado

### Objetivos
Para a realização deste trabalho prático foi defenido o objetivo de criar um interpretador léxico com base na informação e matéria lecionada durante as aulas.

## Métodos Implementados
**1. Definição dos tokens:**
- Tokens -É uma tupla que contém os tipos de tokens que o lexer pode reconhecer.
- Tokens específicos são definidos utilizando expressões regulares (regex). Por exemplo, t_SELECT corresponde ao token "SELECT" (case-insensitive), e t_NUMBER corresponde a um número.

**2. Expressões Regulares para Tokens:**
- t_SELECT, t_FROM, t_WHERE: Palavras-chave SQL como "SELECT", "FROM" e "WHERE", respectivamente. O modificador (?i) torna a correspondência case-insensitive.
- t_OPERATOR: Operadores de comparação como ">=", "<=", ">", "<", ou "=".
- t_COMMA: Vírgula para separar elementos em uma lista.

**3. Função para Tratar Números:**
- def t_NUMBER(t): Uma função que é chamada quando um número é identificado. Converte o valor do token para um inteiro.

**4. Ignorar Espaços em Branco:**
- t_ignore = ' \t': Define espaços em branco e tabulações como caracteres a serem ignorados.

**5. Função de Tratamento de Erros:**
- def t_error(t): Uma função chamada quando um caractere ilegal é encontrado. No exemplo, ela imprime uma mensagem indicando o caractere ilegal e pula para o próximo caractere.

**6. Função Principal (main):**
- Cria uma instância do lexer e solicita ao usuário que insira uma frase SQL.
- A função lexer.input(frase) alimenta a frase para o lexer.
- Um loop é usado para iterar sobre os tokens gerados pelo lexer, e cada token é impresso.

## Conclusão
Em resumo, o código desenvolvido demonstra eficazmente a implementação de um analisador léxico para comandos SQL simples. Os objetivos estabelecidos foram alcançados com sucesso, proporcionando uma estrutura organizada e funcional para reconhecer e classificar tokens relevantes, tais como palavras-chave, identificadores, números e operadores. A utilização da biblioteca ply.lex facilita a definição de regras léxicas através de expressões regulares, contribuindo para a precisão na análise sintática de frases SQL. A capacidade do código em identificar e processar tokens é evidenciada pelo loop de impressão que exibe os tokens correspondentes ao analisar uma frase de entrada. Assim, o analisador léxico desenvolvido cumpre de forma satisfatória os requisitos estabelecidos para a análise básica de comandos SQL.