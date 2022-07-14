'''
    Montagem da tabela que adiciona as colunas de score, melhor posição no chart e tempo no chart (song_chart.csv) aos dados de 
    características acústicas (acoustic_features.csv).
    Feita para que se possa ler um só arquivo .csv com todos os dados, minimizando o uso de força computacional. 
'''

import pandas as pd

max = 1000 # Número máximo de entradas
# Um número maior de entradas estava insustentável no meu PC, mas 1k é suficiente para as demandads do projeto.

# Leitura do DataFrame das características acústicas das músicas
useless_cols_acoustic = ["duration_ms", "time_signature", "key", "mode"] # Dados inúteis pra nossa análise das características acústicaas.
cols_acoustic = list(pd.read_csv("data/acoustic_features.csv", nrows =1, sep='\t'))
df_acoustic_features = pd.read_csv("data/acoustic_features.csv", sep='\t', nrows=max, usecols=[i for i in cols_acoustic if i not in useless_cols_acoustic])

# Leitura do DataFrame das características de popularidade das músicas
useless_cols_chart = ["week", "weeks_on_chart", "rank_score"] # Um vetor com um só valor pode parecer idiota, mas é útil caso eu decida dropar mais colunas
chart_cols = list(pd.read_csv("data/song_chart.csv", nrows =1, sep='\t'))
df_song_chart = pd.read_csv("data/song_chart.csv", sep='\t', usecols=[i for i in chart_cols if i not in useless_cols_chart])

# Lista de todos os ids de música
ids = df_acoustic_features.song_id

df_charts_nodups = pd.DataFrame(columns=["song_id", "peak_position"]) # Variável que guarda os charts, sem duplicatas

'''
    Eduardo, por quê você não simplesmente meteu um "df_acoustic_features.remove_duplicates()"?
    A resposta é que o número de duplicatas no dataset é variável e não tem como eu remover todas as duplicatas, exceto a primeira,
    diretamente pelo pandas.. (não que eu saiba)
    Esse comentário já foi feito pro meu eu do futuro que vai ler isso e pensar "mano, pra quê?"
'''

# Remoção de duplicatas
for id in ids:
    id_charts = df_song_chart[df_song_chart.song_id == id] # Separando os charts de cada música por ID
    entry = id_charts[id_charts.peak_position == id_charts.peak_position.max()].drop_duplicates()
    df_charts_nodups = df_charts_nodups.append(entry)

# União dos dois dataframes e exportação pra CSV
df_charts_nodups.set_index("song_id", inplace=True)
df_acoustic_features.set_index("song_id", inplace=True)

df_charts_nodups.join(df_acoustic_features).to_csv('data/join.csv')