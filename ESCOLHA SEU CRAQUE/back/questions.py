from random import randint

questionsDict = [
    {
        "index" : 0,
        "pergunta" : 'As normas de segurança de alimentos começam em nossos fornecedores homologados e finalizam no consumo do produto pelo cliente final.',
        "resposta" :'Verdadeiro'
    },

    {
        "index" : 1,
        "pergunta" : 'Situação hipotética: um colaborador adentrou na área de envase sem o uso de touca e não higienizou as mãos. Sabendo do ocorrido, seu gestor imediato o orientou que, quando fosse possível, realizasse a higienização das mãos e que o uso de touca seria opcional, tendo em vista que o serviço prestado seria inferior a 30 minutos. Com base no contexto descrito, podemos classificar a conduta do gestor como positiva.',
        "resposta" :'Falso'
    },

    {
        "index" : 2,
        "pergunta" : 'O conceito principal de segurança de alimentos é entregar o produto para o cliente final livre de potenciais contaminações.',
        "resposta" :'Verdadeiro'
    },

    {
        "index" : 3,
        "pergunta" : 'A disseminação da cultura de segurança de alimentos é de responsabilidade apenas do manipulador dos alimentos, não sendo necessário a expansão para o restante da cadeia produtiva.',
        "resposta" :'Falso'
    },

    {
        "index" : 4,
        "pergunta" : 'O consumo de alimentos em área de processo e nos corredores da fábrica é totalmente aceito; a probabilidade de o alimento cair dentro de uma garrafa na linha de envase ou de haver contaminação é mínima.',
        "resposta" :'Falso'
    },

    {
        "index" : 5,
        "pergunta" : 'A correta armazenagem dos produtos finais também está ligada a estocagem, onde a elevação da temperatura acima de 40°C é aceitável para embalagens do portfólio Coca-Cola.',
        "resposta" :'Falso'
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
        "pergunta" : '"Não consumir alimento fora das áreas designadas e não os guardar em locais impróprios" é uma das regra de ouro referente a segurança de alimentos',
        "resposta" : 'Verdadeiro'
    },

    {
        "index" : 14,
        "pergunta" : 'Um dos objetivos da Segurança de Alimentos é zelar pela da saúde das pessoas/consumidores.',
        "resposta" : 'Verdadeiro'
    },

    {
        "index" : 15,
        "pergunta" : 'Deitar ou sentar na grama e depois acessar as áreas de manipulação de alimentos ou armazenagem de ingredientes é uma conduta vista como correta.',
        "resposta" : 'Falso'
    },

    {
        "index" : 16,
        "pergunta" : 'Os pacotes de refrigerantes devem ser armazenados diretamente no chão, não sendo necessário o uso de pallets.',
        "resposta" : 'Falso'
    },

    {
        "index" : 17,
        "pergunta" : 'É permitido lanchar e dormir no espaço ZEN.',
        "resposta" : 'Falso'
    },

    {
        "index" : 18,
        "pergunta" : 'Devo lavar as mãos somente uma vez ao dia; fazê-lo mais de uma vez implica no ressecamento da pele e não é saudável.',
        "resposta" : 'Falso'
    },

    {
        "index" : 19,
        "pergunta" : 'Restos de comida atraem pragas (baratas, ratos e moscas), que podem contaminar os produtos.',
        "resposta" : 'Verdadeiro'
    },

    {
        "index" : 20,
        "pergunta" : 'Sol e chuva podem danificar as embalagens, alterando características do produto - como gosto, odor e aparência -, afetando a segurança do alimento.',
        "resposta" : 'Verdadeiro'
    },

    {
        "index" : 21,
        "pergunta" : 'A política de segurança de alimentos não garante totalmente um alimento seguro no mercado.',
        "resposta" : 'Falso'
    },

    {
        "index" : 22,
        "pergunta" : 'Sempre que falamos de segurança de alimentos, estamos nos referindo a produtos livres de contaminações.',
        "resposta" : 'Falso'
    },

    {
        "index" : 23,
        "pergunta" : 'São exemplos de boas práticas de armazenagem: armazenar as embalagens diretamente no chão, armazenar produtos próximos a produtos químicos.',
        "resposta" : 'Verdadeiro'
    },

    {
        "index" : 24,
        "pergunta" : 'As DTAs (Doença Transmitidas por Alimentos) são ocasionadas por falta de higiene das mãos.',
        "resposta" : 'Falso'
    },

    {
        "index" : 25,
        "pergunta" : 'Devemos higienizar as mãos sempre que acessarmos as áreas de processo (fabricação e produção).',
        "resposta" : 'Verdadeiro'
    },

    {
        "index" : 26,
        "pergunta" : 'Nas áreas administrativas onde é permitida a alimentação, pode-se deixar o copo de café em qualquer local, já que não há risco de atrair pragas.',
        "resposta" : 'Falso'
    },

    {
        "index" : 27,
        "pergunta" : 'Ao higienizar as mãos posso secá-las na minha roupa.',
        "resposta" : 'Falso'
    },     

    {
        "index" : 28,
        "pergunta" : 'Todos os colaboradores são responsáveis pela limpeza do ambiente.',
        "resposta" : 'Verdadeiro'
    },

    {
        "index" : 29,
        "pergunta" : 'Os produtos químicos devem ser mantidos com acesso restrito e devem estar dentro do prazo de validade.',
        "resposta" : 'Verdadeiro'
    }

]

'''
aleatoryIndex = randint(0,17)

for i in range(len(questionsDict)):
    if questionsDict[i]["index"] == aleatoryIndex:
        print(questionsDict[i]['pergunta'])
'''