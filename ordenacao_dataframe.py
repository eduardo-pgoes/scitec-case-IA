'''
    Ordenação do DataFrame pela melhor posição (peak position) das músicas no chart
'''
import pandas as pd

df = pd.read_csv('data/join.csv')

df.set_index('song_id', inplace=True)

(df.sort_values(by=['peak_position'])).to_csv('data/sorted.csv')