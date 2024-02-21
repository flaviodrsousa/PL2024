# TPC2: Conversor de MD para HTML
**Autor:** Flávio David Rodrigues Sousa
**Número de Aluno:** 100715

## Descrição do trabalho realizado

### Objetivos
Para a realização deste trabalho foi importante estudar e utilizadar expressões regulares para facilitar a identificação de padrões em MD para a respetiva substituição e conversão em HTML. Sendo assim, foram delimitados 2 objetivos:

1. **Aplicação de Expressões Regulares**
Com o objetivo de melhor entender e aplicar os conteúdos lecionados nas aulas, foi dado prioridade à implementação de expressões regulares na realização deste trabalho

2. **Conversor de MD para HTML**
Por fim, e como objetivo principal, é importante que o programa faça o seu proposto, isto é, converter as principais formas de escrita em MD para código HTML.

## Métodos Implementados
1.**Função convert**
Este método é responsável por converter as linhas do arquivo Markdown para linhas correspondentes em HTML. Ele percorre cada linha do arquivo Markdown e verifica o seu formato, aplicando as conversões necessárias para HTML.
- Se a linha estiver em branco ou começar com "#" (indicando um cabeçalho), ">", "---" (indicando uma linha horizontal) etc., são aplicadas as transformações adequadas para criar as tags HTML correspondentes.
- Se a linha começar com números seguidos por ponto (indicando uma lista numerada), ou começar com " - " (indicando uma lista não numerada), são criadas as tags HTML para listas ordenadas ou não ordenadas, respectivamente.
Além disso, são aplicadas substituições para negrito, itálico, imagens, links e código usando expressões regulares.
O resultado é armazenado em uma lista chamada resultado.

2.**Função mdHTML**
Este método recebe um nome de arquivo como entrada, lê o conteúdo do arquivo Markdown e chama a função convert para converter o conteúdo para HTML. Em seguida, ele escreve o resultado no arquivo HTML correspondente.

##Conclusão
O presente trabalho foi conduzido com sucesso, alcançando os objetivos estabelecidos de maneira eficaz e eficiente. Durante o processo, foram definidos dois principais objetivos delimitados anteriormente na secção *Objetivos*.
Foi denotada uma dificuldade na implementação das expressões regulares. Essa dificuldade é justificada por ser algo novo e com algum certo cuidado e dedicação de estudo.
Em suma, o programa converte com eficácia os arquivos pedidos. Como prova, temos o arquivo *exemplo.md* que foi convertido e criado o arquivo *exemplo.html*, ambos presentes nesta diretoria. 
