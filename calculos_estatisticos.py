'''
    Mostra a média e a moda de cada atributo numérico do dataset
'''

import pandas as pd

df = pd.read_csv('data/sorted.csv')
df.set_index('song_id', inplace=True)
print("Médias:")
print(df.mean())
print("\nModas:")
print(df.mean())