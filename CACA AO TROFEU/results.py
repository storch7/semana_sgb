import pandas as pd
from functions import *

#formularys
form1 = pd.read_csv("./forms/F1 (respostas).csv")
form2 = pd.read_csv("./forms/F2 (respostas).csv")
form3 = pd.read_csv("./forms/F3 (respostas).csv")
form4 = pd.read_csv("./forms/F4 (respostas).csv")
form5 = pd.read_csv("./forms/F5 (respostas).csv")
form6 = pd.read_csv("./forms/F6 (respostas).csv")
form7 = pd.read_csv("./forms/F7 (respostas).csv")
form8 = pd.read_csv("./forms/F8 (respostas).csv")
form9 = pd.read_csv("./forms/F9 (respostas).csv")
form10 = pd.read_csv("./forms/F10 (respostas).csv")

formularys = [form1, 
              form2, 
              form3,
              form4,
              form5,
              form6,
              form7,
              form8,
              form9,
              form10]

#answears 
answears = ["Verdadeiro", 
            "Falso", 
            "Verdadeiro",
            "Verdadeiro", 
            "Falso", 
            "Falso",
            "Verdadeiro", 
            "Falso", 
            "Verdadeiro",
            "Verdadeiro"]

#selecting registers
correct_answars = []

for i in range(len(formularys)):
    forms = formularys[i]
    forms = renamingColumns(forms)
    forms = selectCorrectAnswears(forms, answears[i])
    matriculas = list(forms['Matricula'])

    for j in range(len(matriculas)):
        correct_answars.append(matriculas[j])

unique_registers = get_unique_numbers(correct_answars)

#counting
winnersRegister = []
winnersCount = []

for i in range(len(unique_registers)):
    register = unique_registers[i]
    counting = correct_answars.count(register)
    winnersRegister.append(register)
    winnersCount.append(counting)

#creating a table with the count 
data = {
    'Matrícula' : winnersRegister,
    'Acertos' : winnersCount
}

dataBase = pd.DataFrame(data)
dataBase.to_csv("Contagem de acertos.csv")