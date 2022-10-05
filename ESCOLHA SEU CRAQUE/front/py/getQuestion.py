import sys 
from random import randint

sys.path.insert(1, '/home/storch/Documentos/BRASAL/JOGOS SEMANA SGB/ESCOLHA SEU CRAQUE/back')

from questions import questionsDict

def getQuestions() :

    aleatoryIndex = randint(0,17)

    question = ''
    
    for i in range(len(questionsDict)):
        
        if questionsDict[i]["index"] == aleatoryIndex:
            question = questionsDict[i]['pergunta']
    
    return question

teste = getQuestions()

print(teste)