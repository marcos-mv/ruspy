'''
# [comp-vs-interp]

Compreender as principais diferenças entre um compilador e um interpretador. 

* Situar um interpretador no contexto da arquitetura tradicional de compiladores.
* Compreender a distinção entre um interpretador de árvores sintáticas e uma máquina virtual.
* Identificar, entre as linguagens de programção mais conhecidas, quais são tradicionalmente interpretadas e quais são compiladas. 

-----

Responda às questões:

Q1) Descreva sucintamente as semelhanças e diferenças entre compiladores e 
interpretadores, em especial no que ambos diferem (ou se assemelham) com relação 
às etapas mencionadas na questão anterior em COMP_ORG.

Q2) É um erro comum acreditar que "compilada" vs "interpretada" é uma 
característica da linguagem de programação. Estas são características de 
**implementações** específicas de cada linguagem. Ainda que a implementação de 
Python criada por Guido seja interpretada (e de longe a mais popular) ou que a 
versão do C que presente no GCC seja compilada, nada impede se crie versões 
compiladas de Python ou interpretadas de C. Na realidade, elas existem. 

Encontre pelo menos um exemplo de implementação de um compilador para uma 
linguagem normalmente tida como interpretada ou de um interpretador para uma 
linguagem normalmente tida como compilada. Forneça uma referência como link, 
artigo, etc que aponte para os projetos escolhidos como exemplos.


Salve a sua resposta em duas variáveis do tipo string como abaixo:

    COMP_VS_INTERP_Q1 = """
    
    Em suma, a grande diferença está na forma de execução. Enquanto um compilador analisa todo
    o código a fim de traduzi-lo de uma vez (muitas vezes, o resultado é um arquivo executável
    ou uma biblioteca), o interpretador faz esse trabalho de conversão aos poucos, sempre que 
    uma declaração ou função é executada, por exemplo.
    
    Uma das grandes vantagens dos compiladores é sua velocidade de execução, muito em função
    de traduzir todo o código de uma vez. Não precisar fazer a conversão toda vez que o sistema
    é executado dá uma eficiência muito maior do que um interpretador.
    
    Uma compilação costuma dar resultados mais confiáveis graças às suas diversas etapas de validação e otimização.
    Uma checagem de tipos estáticos, por exemplo, é comum em compiladores, e identifica diversos erros de programação
    antes do executável ser gerado.
    Por sua vez, enquanto uma linguagem compilada precisa fazer essa tradução para cada plataforma destinada (Windows, linux, etc...)
    a interpretação, por poder rodar em tempo de execução, é independente.
    
    """

    COMP_VS_INTERP_Q2 = """
    
    Nuitka é um compilador de fonte para fonte que compila
    o código Python para o código C, aplicando algumas otimizações
    em tempo de compilação no processo, como dobramento e propagação constantes,
    previsão de chamada integrada, inferência de tipo e execução de instrução condicional.

    https://pypi.org/project/Nuitka/0.4.1/ 

    """
'''
import pytest

def test_verificações_básicas(var):
    print(var('COMP_VS_INTERP_Q1'))
    print(var('COMP_VS_INTERP_Q2'))
    pytest.skip('a resposta será avaliada manualmente')