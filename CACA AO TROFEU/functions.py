import pandas as pd

def renamingColumns(form):

    #selecting the name of columns 
    lastNameColumn = list(form.columns)
    lastNameColumn1 = lastNameColumn[1]
    lastNameColumn2 = lastNameColumn[2]
    lastNameColumn3 = lastNameColumn[3]

    #changing the column's name 
    formulary = form.rename(columns={lastNameColumn1:'Nome', lastNameColumn2:'Matricula', lastNameColumn3:'Resposta'})

    return formulary

def selectCorrectAnswears(form, correct_answear):

    formulary = renamingColumns(form)
    formulary = form[form["Resposta"] == correct_answear]

    return formulary

def get_unique_numbers(numbers):

    list_of_unique_numbers = []

    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers