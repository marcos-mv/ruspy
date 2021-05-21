'''
# [comp-org]

Compreender as etapas tradicionais de análise do código em um compilador. 

* Conhecer o papel e função das etapas de análise léxica, análise sintática, análise semântica, otimização e geração de código.
* Conhecer superficialmente como esse mecanismo funciona em alguma linguagem real e possuir elementos conceituais para comparar estas etapas em diferentes linguagens.

-----

Descreva a função de cada etapa no processo de compilação de um código

* Análise léxica
* Análise sintática
* Análise semântica
* Otimização
* Emissão de código

Salve a sua resposta em uma variável de string como abaixo:

    COMP_ORG = """
    * Análise léxica: A análise léxica também conhecida como scanner ou leitura é a primeira fase
    de um processo de compilação e sua função é fazer a leitura do programa fonte, 
    caractere a caractere, agrupar os caracteres em lexemas e produzir uma sequência 
    de símbolos léxicos conhecidos como tokens.
    A análise léxica pode ser dividida em duas etapas, a primeira chamada de escandimento
    que é uma simples varredura removendo comentários e espaços em branco, e a segunda etapa, 
    a analise léxica propriamente dita onde o texto é quebrado em lexemas.

    * Análise sintática: O Analisador sintático também conhecido como parser tem como tarefa 
    principal determinar se o programa de entrada representado pelo fluxo de tokens possui as 
    sentenças válidas para a linguagem de programação.
    A analise sintática e a segunda etapa do processo de compilação e na maioria dos casos utiliza
    gramáticas livres de contexto para especificar a sintaxe de uma linguagem de programação.

    * Análise semântica: A analise semântica é responsavel por verificar aspectos relacionados ao significado
    das instruções, essa é a terceira etapa do processo de compilação e nesse momento ocorre a validação de 
    uma serie regras que não podem ser verificadas nas etapas anteriores.
    As validações que não podem ser executadas pelas etapas anteriores devem ser executadas durante a análise semântica 
    a fim de garantir que o programa fonte estaja coerente e o mesmo possa ser convertido para linguagem de máquina.
    A análise semântica percorre a árvore sintática relaciona os identificadores com seus dependentes de acordo 
    com a estrutura hierarquica.
    Essa etapa também captura informações sobre o programa fonte para que as fases subsequentes gerar o código 
    objeto, um importante componente da analise semântica é a verificação de tipos, nela o compilador verifica se cada operador 
    recebe os operandos permitidos e especificados na linguagem fonte.

    * Otimização: A etapa final na geração de código pelo compilador é a fase de otimização. Como o código gerado através da tradução 
    orientada a sintaxe contempla expressões independentes, diversas situações contendo seqüências de código ineficiente podem ocorrer. 
    O objeto da etapa de otimização de código é aplicar um conjunto de heurísticas para detectar tais seqüências e substituí-las por outras 
    que removam as situações de ineficiência.
    As técnicas de otimização que são usadas em compiladores devem, além de manter o significado do programa original, ser capazes de capturar 
    a maior parte das possibilidades de melhoria do código dentro de limites razoáveis de esforço gasto para tal fim. Em geral, os compiladores 
    usualmente permitem especificar qual o grau de esforço desejado no processo de otimização. 

    * Emissão de código: A tradução do código de alto nível para o código do processador está associada
    à traduzir para a linguagem-alvo a representação da árvore gramatical obtida para
    as diversas expressões do programa. Embora tal atividade possa ser realizada para
    a árvore completa após a conclusão da análise sintática, em geral ela é efetivada
    através das ações semânticas associadas à aplicação das regras de reconhecimento
    do analisador sintático. Este procedimento é denominado tradução dirigida pela
    sintaxe. Em geral, a geração de código não se dá diretamente para a linguagem assembly
    do processador-alvo. Por conveniência, o analisador sintático gera código para uma
    máquina abstrata, com uma linguagem próxima a assembly porém independente de
    processadores específicos. Em uma segunda etapa de geração de código, esse código
    intermediário é traduzido para a linguagem assembly desejada. Dessa forma,
    grande parte do compilador é reaproveitada para trabalhar com diferentes tipos de
    processadores.

    """
'''
import pytest

def test_verificações_básicas(var):
    print(var('COMP_ORG'))
    pytest.skip('a resposta será avaliada manualmente')