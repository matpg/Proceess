'''
	Programa codificado por Matias Poblete Garrido
'''


import pandas as pd
df = pd.read_csv("test1.csv", sep=';')
# separado por un ";"

# print(df.head())
# imprimer un pequeño encabezado a forma de muestra.
# print(df.columns)

# print(df.index)
num_answer = df.shape[0]
alters_names = df.columns.tolist()
num_alters = len(alters_names)
answer_dict = {}
# creacion de un diccionario de respuestas, con forma de ranking parcial/alternativa
for alternative in range(num_alters):
    total_answers, ith_rank = 0, 0
    for answers in range(num_answer):
        ith_alter = df.at[answers, alters_names[alternative]]
        total_answers += ith_alter
        ith_rank += ith_alter * (num_answer - answers)
    partial_rank = ith_rank / total_answers
    answer_dict.setdefault(partial_rank, alters_names[alternative])

print('El Ranking Final es: ')
# muestra el resultado del calculo en forma de ranking.
for alternative in range(num_alters):
    max_value_key = max(answer_dict.keys())
    value = answer_dict.pop(max_value_key)
    max_value_key = round(max_value_key, 2)
    print(str(alternative + 1) + ' ' + value + ' (' + str(max_value_key) + ')')
