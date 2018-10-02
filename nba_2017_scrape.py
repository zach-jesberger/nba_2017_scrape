# import packages
import pandas as pd
import csv

# define url
url = "https://www.basketball-reference.com/leagues/NBA_2018.html"

# column names
cols = ['team', 'wins', 'losses', 'win_perc', 'games_back', 'psg', 'pag', 'srs']

# import and define east
east = pd.read_html(url)[0].dropna()
east.columns = cols
east['conference'] = 'Eastern Conference'

# import and define west 
west = pd.read_html(url)[1].dropna()
west.columns = cols
west['conference'] = 'Western Conference'

# appeand west to east
nba = east.append(west)

# clean dataframe
nba['team'] = nba['team'].str.replace('[^a-zA-Z0-9 \n\.]', '').str.replace("[0-9()]+$", "")
nba = nba.set_index('team')
nba = nba.sort_values('wins', ascending = False)
#print(nba)

# write to csv
nba.to_csv('nba_2017.csv')