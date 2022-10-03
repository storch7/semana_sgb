from random import randint

questionsDict = [
    {
        "index" : 0,
        "pergunta" : 'As normas de segurança de alimentos começam em nossos fornecedores homologados e finalizam no consumo do produto pelo cliente final. ',
        "resposta" :'Verdadeiro'
    },

    {
        "index" : 1,
        "pergunta" : 'Situação hipotética: um colaborador adentrou na área de envase sem fazer o uso de touca e não utilizou os recursos de higienização das mãos. Sabendo do ocorrido, seu gestor imediato o informou que, quando fosse possível, fizesse a lavagem das mãos; o uso de touca seria opcional tendo em vista que o serviço prestado seria inferior a 30 minutos. Com base no contexto descrito, podemos classificar o retorno do gestor como uma ação positiva.',
        "resposta" :'Falso'
    },

    {
        "index" : 2,
        "pergunta" : 'O conceito principal de segurança de alimentos é entregar o produto para o cliente final livre de potenciais contaminações.',
        "resposta" :'Verdadeiro'
    },

    {
        "index" : 3,
        "pergunta" : 'A disseminação da cultura de segurança de alimentos é de responsabilidade apenas do manipulador de alimentos, e não sendo necessário a expansão para o restante da cadeia produtiva.',
        "resposta" :'Falso'
    },

    {
        "index" : 4,
        "pergunta" : 'O consumo de alimentos em área de processo e nos corredores da fábrica é totalmente aceito; a probabilidade de o alimento chegar a cair dentro de uma garrafa na linha de envase é mínima.',
        "resposta" :'Falso'
    },

    {
        "index" : 5,
        "pergunta" : 'A correta armazenagem dos produtos finais está ligada a estocagem, onde a elevação de temperatura acima de 40°C é comum para embalagens do portfólio Coca Cola.',
        "resposta" :'Verdadeiro'
    },

    {
        "index" : 6,
        "pergunta" : 'A variação de temperatura para garrafas pet não altera as características físico-químicas na composição final dos produtos.',
        "resposta" : 'Falso'
    },

    {
        "index" : 7,
        "pergunta" : 'A correta armazenagem de produtos finais deve seguir as seguintes diretrizes: (i) conservar ao abrigo do sol e calor, em local limpo e seco, arejado e sem odor e (ii) não congelar.',
        "resposta" : 'Verdadeiro'
    },

    {
        "index" : 8,
        "pergunta" : 'É correto afirmar que um produto com contaminação biológica é seguro para consumo.',
        "resposta" : 'Falso'
    },

    {
        "index" : 9,
        "pergunta" : 'Fornecer ao mercado produtos seguros e buscar melhoraria continua de seus processos são itens que fazem parte da Política de Segurança de Alimentos.',
        "resposta" : 'Verdadeiro'
    },

    {
        "index" : 10,
        "pergunta" : 'A contaminação física, química e biológica do produto pode representar efeito adverso à saúde do consumidor',
        "resposta" : 'Verdadeiro'
    },

    {
        "index" : 11,
        "pergunta" : 'Um dos conceitos de Segurança de Alimentos é cuidar da saúde das pessoas.',
        "resposta" : 'Verdadeiro'
    },

    {
        "index" : 12,
        "pergunta" : 'São itens fundamentais para prevenir e reduzir os perigos a segurança de alimentos: higiene, organização e limpeza.',
        "resposta" : 'Verdadeiro'
    },

    {
        "index" : 13,
        "pergunta" : '"Não consumir alimento fora das áreas designadas e não os guardar em locais impróprios" é uma regra de ouro referente a segurança de alimento',
        "resposta" : 'Verdadeiro'
    },

    {
        "index" : 14,
        "pergunta" : 'Um dos conceitos de Segurança de Alimentos é cuidar da saúde das pessoas.',
        "resposta" : 'Verdadeiro'
    },

    {
        "index" : 15,
        "pergunta" : 'Deitar ou sentar na grama e depois acessar as áreas de manipulação de alimentos ou armazenagem de ingredientes é uma conduta vista como correta.',
        "resposta" : 'Falso'
    },

    {
        "index" : 16,
        "pergunta" : 'Os pacotes de refrigerantes devem ser armazenados diretamente no chão, não sendo necessário o uso do palite.',
        "resposta" : 'Falso'
    },

    {
        "index" : 17,
        "pergunta" : 'E permitido lanchar e dormir no espaço ZEN.',
        "resposta" : 'Falso'
    },     
]

'''
aleatoryIndex = randint(0,17)

for i in range(len(questionsDict)):
    if questionsDict[i]["index"] == aleatoryIndex:
        print(questionsDict[i]['pergunta'])
'''