#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.display import display, Javascript

def restart_kernel():
    display(Javascript('IPython.notebook.kernel.restart(force=True)'))

restart_kernel()

# In[2]:

import time 
import pandas as pd



#import data sets
df = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/player data/player_data.xlsx')
df1 = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/Comparison/Other players data/players goal data.xlsx')
df2 = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/Comparison/Other players data/players assist data.xlsx')
df3 = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/perfomance/Forward/forward players data.xlsx')
df4 = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/last 5 games/last 5 games.xlsx')
df5 = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/player_current/seasonal_data.xlsx')
df6 = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/players.xlsx')
df7 = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/Rating/team_strength.xlsx')

#count the best players of selected squad
df6 = df6[~df6['Position'].isin(['Goalkeeper'])]
count_2 = (df6['ranking'] == 1).sum()



selected_players = df6['Player'].tolist()
#preprocesing
df['Other Positions'] = df['Other Positions'].str.replace('\n', ', ')
df['Height'] = df['Height'].str.replace('\n', '')
mask = df['Market value'].str.contains('k')
df.loc[mask, 'Market value'] = '0.' + df.loc[mask, 'Market value'].str.replace('k', '')
df['Market value']=df['Market value'].str.replace('m', '')
df['Market value'] = df['Market value'].replace('-', '0')
df['Market value'] = pd.to_numeric(df['Market value'])
df3['Shooting accuracy'] = df3['Shooting accuracy'].str.replace('%', '')



df['Goals'] = df['Goals'].replace('-', '0')
df['Assists'] = df['Assists'].replace('-', '0')
df['Goals'] = df['Goals'].astype(int)
df['Assists'] = df['Assists'].astype(int)
df['Appearance'] = df['Appearance'].astype(int)
df1 = df1.replace({"-": 0}).fillna(0)
df2 = df2.replace({"-": 0}).fillna(0)
df1 = df1.fillna(0)
df2 = df2.fillna(0)
df3 = df3.fillna(0)
df4 = df4.fillna(0)

#convert to numeric
for column in df1.columns:
    if column not in ["Player", "Position"]:
        df1[column] = pd.to_numeric(df1[column], errors='coerce')
for column in df2.columns:
    if column not in ["Player", "Position"]:
        df2[column] = pd.to_numeric(df2[column], errors='coerce')
for column in df3.columns:
    if column not in ["Player", "Position"]:
        df3[column] = pd.to_numeric(df3[column], errors='coerce')

df3['Shooting accuracy']= df3['Shooting accuracy']*0.01
df4['Pass accuracy']= df4['Pass accuracy']*0.01

#standadization
cols_to_standardize = df.columns.difference(["Player", "Position", "Other Positions", "Height", "Jersey num", "Injury update","Goal conceded","Clean sheet","Date of birth/Age","Dominant foot"])
df[cols_to_standardize] = (df[cols_to_standardize] - 0) / (df[cols_to_standardize].max() -0)
cols_to_standardize = df1.columns.difference(["Player", "Position"])
df1[cols_to_standardize] = (df1[cols_to_standardize] - 0) / (df1[cols_to_standardize].max() -0)
cols_to_standardize = df2.columns.difference(["Player", "Position"])
df2[cols_to_standardize] = (df2[cols_to_standardize] - 0) / (df2[cols_to_standardize].max() -0)
cols_to_standardize = df3.columns.difference(["Player", "Position"])
df3[cols_to_standardize] = (df3[cols_to_standardize] - 0) / (df3[cols_to_standardize].max() -0)
cols_to_standardize = df4.columns.difference(["Player"])
df4[cols_to_standardize] = (df4[cols_to_standardize] - 0) / (df4[cols_to_standardize].max() -0)
cols_to_standardize = df5.columns.difference(["Player","Position"])
df5[cols_to_standardize] = (df5[cols_to_standardize] - 0) / (df5[cols_to_standardize].max() -0)

#filter players can play left winger
filtered_df = df[((df['Position'] == 'Centre-Forward')  |df['Other Positions'].str.contains('Left Winger')|(df['Position'] == 'Left Winger')  |df['Other Positions'].str.contains('Centre-Forward'))  ]
filtered_df = filtered_df[filtered_df['Player'] != 'Diego Moreira']

#filter all data set
filtered_df = filtered_df[~filtered_df['Player'].isin(selected_players)]
filtered_df1 = df1[df1['Player'].isin(filtered_df['Player'].tolist())]
filtered_df2 = df2[df2['Player'].isin(filtered_df['Player'].tolist())]
filtered_df3 = df3[df3['Player'].isin(filtered_df['Player'].tolist())]
filtered_df4 = df4[df4['Player'].isin(filtered_df['Player'].tolist())]
filtered_df5 = df5[df5['Player'].isin(filtered_df['Player'].tolist())]

import pandas as pd


file_path = 'C:/Users/Admin/Documents/research final - chelsea/Research/Strength and weakness/Strength and weakness.xlsx'
sheet_name = "FC Fulham"

#opposint team strengths
df8= pd.read_excel(file_path, sheet_name=sheet_name)

tasks_strengths = df8[(df8['Strength/Weakness'] == 'Very Strong') | (df8['Strength/Weakness'] == 'Strong')]

kpi_list = ['Defending counter attacks', 'Defending against long shots','Protecting the lead', 'Defending set pieces', 'Defending against attacks down the wings']


tasks_strengths['Matched KPIs'] = tasks_strengths['KPIs'].apply(lambda x: sum(kpi in x for kpi in kpi_list))
additional_weigth=[]
defensive_weigth=[]


for index, row in tasks_strengths.iterrows():
    if row['Matched KPIs'] == 5:
        additional_weigth.append(5)
    elif row['Matched KPIs'] == 4:
        additional_weigth.append(4)
    elif row['Matched KPIs'] == 3:
        additional_weigth.append(3)
    elif row['Matched KPIs'] == 2:
        additional_weigth.append(2)
    elif row['Matched KPIs'] == 1:
        additional_weigth.append(1)
    else:
        additional_weigth.append(0)

tasks_strengths['Matched KPIs'] = tasks_strengths['KPIs'].apply(lambda x: 'Attacking down the wings' in x)


for index, row in tasks_strengths.iterrows():
    if row['Matched KPIs']:
        defensive_weigth.append(2)
    else:
        defensive_weigth.append(0)
        

from ortools.linear_solver import pywraplp
#function select left winger
def select_best_left_winger(Market_value,apperence, position_list, seasonal_apperence, goals, assists, againts_team_goals, againts_team_assists, Shots, ShotsOnTarget, Penalty, Free_kick, Big_chances_missed, Shooting_accuracy, Big_chances_created, Crosees, Passes, Off_side, Tackles_per_game, Block_shots_per_game, interceptions_per_game, Total_clearance_per_game, seasonal_goals, seasonal_assists, seasonal_Yellow, seasonal_Red, seasonal_Second_Yellow, recent_Goals, recent_Assists, recent_Shots, recent_ShotOnTarget, recent_Fouls, recent_Yellow_card, recent_Red_card, recent_Offside,recent_Pass_accuracy,recent_Keypasses,Right_foot_goals, weights):
    # Create a solver
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        return None, None
    
    # Define variables
    num_left_winger = len(goals)
    x = [solver.IntVar(0, 1, f'x{i}') for i in range(num_left_winger)]

    # Define objective function
    objective = solver.Objective()
    for i in range(num_left_winger):
        objective.SetCoefficient(x[i],weights['Market_value'] * Market_value[i]+ weights['position_list'] * position_list[i] + weights['goals'] * (goals[i] / apperence[i]) + weights['assists'] * (assists[i] / apperence[i]) + weights['againts_team_goals'] * againts_team_goals[i] + weights['againts_team_assists'] * againts_team_assists[i] + weights['Shots'] * Shots[i] + weights['ShotsOnTarget'] * ShotsOnTarget[i] + weights['Penalty'] * Penalty[i] + weights['Free_kick'] * Free_kick[i] - weights['Big_chances_missed'] * Big_chances_missed[i] + weights['Shooting_accuracy'] * Shooting_accuracy[i] + weights['Big_chances_created'] * Big_chances_created[i] + weights['Crosees'] * Crosees[i] + weights['Passes'] * Passes[i] - weights['Off_side'] * Off_side[i]+weights['Tackles_per_game'] * Tackles_per_game[i] +weights['Block_shots_per_game'] * Block_shots_per_game[i]+weights['interceptions_per_game'] * interceptions_per_game[i]+weights['Total_clearance_per_game'] * Total_clearance_per_game[i]+ weights['seasonal_goals'] * (seasonal_goals[i] / seasonal_apperence[i]) + weights['seasonal_assists'] * (seasonal_assists[i] / seasonal_apperence[i]) - weights['seasonal_Yellow'] * seasonal_Yellow[i] - weights['seasonal_Red'] * seasonal_Red[i] - weights['seasonal_Second_Yellow'] * seasonal_Second_Yellow[i] + weights['recent_Goals'] * recent_Goals[i] + weights['recent_Assists'] * recent_Assists[i] + weights['recent_Shots'] * recent_Shots[i] + weights['recent_ShotOnTarget'] * recent_ShotOnTarget[i] - weights['recent_Fouls'] * recent_Fouls[i] - weights['recent_Yellow_card'] * recent_Yellow_card[i] - weights['recent_Red_card'] * recent_Red_card[i] - weights['recent_Offside'] * recent_Offside[i]+weights['recent_Pass_accuracy']*recent_Pass_accuracy[i]+weights['recent_Keypasses']*recent_Keypasses[i]+weights['Right_foot_goals']*Right_foot_goals[i])
    objective.SetMaximization()
    
    # Add constraint
    solver.Add(sum(x[i] for i in range(num_left_winger)) == 2)  # Select 2 forwards
    
    # Solve the problem
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL:
        selected_left_winger = [i for i in range(num_left_winger) if x[i].solution_value() == 1]
        return selected_left_winger
    else:
        return None, None





#  data
names = filtered_df["Player"].to_list()
position_list = [1 if position == "Left Winger" else 0 for position in filtered_df["Position"]]
goals = filtered_df["Goals"].to_list()
assists = filtered_df["Assists"].to_list()
apperence = filtered_df["Appearance"].to_list()
Market_value = filtered_df["Market value"].to_list()
againts_team_goals= filtered_df1[sheet_name].to_list()
againts_team_assists= filtered_df2[sheet_name].to_list()
Shots= filtered_df3["Shots per game"].to_list()
ShotsOnTarget= filtered_df3["Shots on target per game"].to_list()
Penalty= filtered_df3["Penalty goals"].to_list()
Free_kick= filtered_df3["Free kick goals"].to_list()
Big_chances_missed= filtered_df3["Big chances missed per game"].to_list()
Shooting_accuracy= filtered_df3["Shooting accuracy"].to_list()
Big_chances_created= filtered_df3["Big chances created per game"].to_list()
Crosees= filtered_df3["Crosses per game"].to_list()
Passes= filtered_df3["Passes per game"].to_list()
Off_side= filtered_df3["Offside per game"].to_list()
Goals_per_game= filtered_df3["Goals per game"].to_list()
Tackles_per_game= filtered_df3["Tackles per game"].to_list()
Block_shots_per_game= filtered_df3["Block shots per game"].to_list()
interceptions_per_game= filtered_df3["Interceptions per game"].to_list()
Total_clearance_per_game= filtered_df3["Total clearance per game"].to_list()
seasonal_apperence= filtered_df5["Season appearance"].to_list()
seasonal_goals= filtered_df5["Goals"].to_list()
seasonal_assists= filtered_df5["Assists"].to_list()
seasonal_Yellow= filtered_df5["Yellow cards"].to_list()
seasonal_Red= filtered_df5["Red cards"].to_list()
seasonal_Second_Yellow= filtered_df5["Second yellow cards"].to_list()
recent_Goals= filtered_df4["Goals"].to_list()
recent_Assists= filtered_df4["Assists"].to_list()
recent_Shots= filtered_df4["Shots"].to_list()
recent_ShotOnTarget= filtered_df4["Shot on targets"].to_list()
recent_Fouls= filtered_df4["Fouls"].to_list()
recent_Yellow_card= filtered_df4["Yellow card"].to_list()
recent_Red_card= filtered_df4["Red card"].to_list()
recent_Offside= filtered_df4["Offside"].to_list()
recent_Pass_accuracy= filtered_df4["Pass accuracy"].to_list()
recent_Keypasses= filtered_df4["Key passes"].to_list()
Right_foot_goals= filtered_df3["Right foot goals"].to_list()
Jersey_num= filtered_df["Jersey num"].to_list()

weights = {'Market_value':1,'position_list':1,'goals': 6, 'assists': 5,'againts_team_goals' : 6  ,'againts_team_assists' : 5,'Shots': 4+additional_weigth[0],'ShotsOnTarget': 4+additional_weigth[0], 'Penalty': 2+additional_weigth[0],'Free_kick' : 2+additional_weigth[0] ,'Big_chances_missed' : 2,'Shooting_accuracy': 4,'Big_chances_created' : 4 ,'Crosees' : 6,'Passes': 2,'Off_side' : 2,'Tackles_per_game': defensive_weigth[0] ,'Block_shots_per_game':defensive_weigth[0],'interceptions_per_game':defensive_weigth[0],'Total_clearance_per_game':defensive_weigth[0],'seasonal_goals':8,'seasonal_assists':7,'seasonal_Yellow':2,'seasonal_Red':2,'seasonal_Second_Yellow':2,'recent_Goals':10,'recent_Assists':9,'recent_Shots':6,'recent_ShotOnTarget':6,'recent_Fouls':4,'recent_Yellow_card':4,'recent_Red_card':4,'recent_Offside':4,'recent_Pass_accuracy':4,'recent_Keypasses':6,'Right_foot_goals':2}

# Select the best and second-best left winger
selected_left_winger = select_best_left_winger(Market_value,apperence, position_list, seasonal_apperence, goals, assists, againts_team_goals, againts_team_assists, Shots, ShotsOnTarget, Penalty, Free_kick, Big_chances_missed, Shooting_accuracy, Big_chances_created, Crosees, Passes, Off_side, Tackles_per_game, Block_shots_per_game, interceptions_per_game, Total_clearance_per_game, seasonal_goals, seasonal_assists, seasonal_Yellow, seasonal_Red, seasonal_Second_Yellow, recent_Goals, recent_Assists, recent_Shots, recent_ShotOnTarget, recent_Fouls, recent_Yellow_card, recent_Red_card, recent_Offside,recent_Pass_accuracy,recent_Keypasses,Right_foot_goals, weights)

# Sort the selected left winger by their objective function values
selected_left_winger.sort(key=lambda x:weights['Market_value'] * Market_value[x]+ weights['position_list'] * position_list[x] + weights['goals'] * (goals[x] / apperence[x]) + weights['assists'] * (assists[x] / apperence[x]) + weights['againts_team_goals'] * againts_team_goals[x] + weights['againts_team_assists'] * againts_team_assists[x] + weights['Shots'] * Shots[x] + weights['ShotsOnTarget'] * ShotsOnTarget[x] + weights['Penalty'] * Penalty[x] + weights['Free_kick'] * Free_kick[x] - weights['Big_chances_missed'] * Big_chances_missed[x] + weights['Shooting_accuracy'] * Shooting_accuracy[x] + weights['Big_chances_created'] * Big_chances_created[x] + weights['Crosees'] * Crosees[x] + weights['Passes'] * Passes[x] - weights['Off_side'] * Off_side[x] +weights['Tackles_per_game'] * Tackles_per_game[x] +weights['Block_shots_per_game'] * Block_shots_per_game[x]+weights['interceptions_per_game'] * interceptions_per_game[x]+weights['Total_clearance_per_game'] * Total_clearance_per_game[x] + weights['seasonal_goals'] * (seasonal_goals[x] / seasonal_apperence[x]) + weights['seasonal_assists'] * (seasonal_assists[x] / seasonal_apperence[x]) - weights['seasonal_Yellow'] * seasonal_Yellow[x] - weights['seasonal_Red'] * seasonal_Red[x] - weights['seasonal_Second_Yellow'] * seasonal_Second_Yellow[x] + weights['recent_Goals'] * recent_Goals[x] + weights['recent_Assists'] * recent_Assists[x] + weights['recent_Shots'] * recent_Shots[x] + weights['recent_ShotOnTarget'] * recent_ShotOnTarget[x] - weights['recent_Fouls'] * recent_Fouls[x] - weights['recent_Yellow_card'] * recent_Yellow_card[x] - weights['recent_Red_card'] * recent_Red_card[x] - weights['recent_Offside'] * recent_Offside[x]+weights['recent_Pass_accuracy']*recent_Pass_accuracy[x]+weights['recent_Keypasses']*recent_Keypasses[x]+weights['Right_foot_goals']*Right_foot_goals[x], reverse=True)

# Get the names of the two best left winger
best_left_winger_idx = selected_left_winger[0]
second_best_left_winger_idx = selected_left_winger[1]
best_left_winger_name = names[best_left_winger_idx]
second_best_left_winger_name = names[second_best_left_winger_idx]



team_strength = df7.loc[df7['Team'] == sheet_name, 'Team Strength'].values[0] if sheet_name in df7['Team'].values else None


from openpyxl import load_workbook 
wb= load_workbook('C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/players.xlsx')


sheet = wb.active
#select player based on opponent
if team_strength=='Big six':
    i=best_left_winger_idx
    per=weights['Market_value'] * Market_value[i]+ weights['position_list'] * position_list[i] + weights['goals'] * (goals[i] / apperence[i]) + weights['assists'] * (assists[i] / apperence[i]) + weights['againts_team_goals'] * againts_team_goals[i] + weights['againts_team_assists'] * againts_team_assists[i] + weights['Shots'] * Shots[i] + weights['ShotsOnTarget'] * ShotsOnTarget[i] + weights['Penalty'] * Penalty[i] + weights['Free_kick'] * Free_kick[i] - weights['Big_chances_missed'] * Big_chances_missed[i] + weights['Shooting_accuracy'] * Shooting_accuracy[i] + weights['Big_chances_created'] * Big_chances_created[i] + weights['Crosees'] * Crosees[i] + weights['Passes'] * Passes[i] - weights['Off_side'] * Off_side[i] +weights['Tackles_per_game'] * Tackles_per_game[i] +weights['Block_shots_per_game'] * Block_shots_per_game[i]+weights['interceptions_per_game'] * interceptions_per_game[i]+weights['Total_clearance_per_game'] * Total_clearance_per_game[i] + weights['seasonal_goals'] * (seasonal_goals[i] / seasonal_apperence[i]) + weights['seasonal_assists'] * (seasonal_assists[i] / seasonal_apperence[i]) - weights['seasonal_Yellow'] * seasonal_Yellow[i] - weights['seasonal_Red'] * seasonal_Red[i] - weights['seasonal_Second_Yellow'] * seasonal_Second_Yellow[i] + weights['recent_Goals'] * recent_Goals[i] + weights['recent_Assists'] * recent_Assists[i] + weights['recent_Shots'] * recent_Shots[i] + weights['recent_ShotOnTarget'] * recent_ShotOnTarget[i] - weights['recent_Fouls'] * recent_Fouls[i] - weights['recent_Yellow_card'] * recent_Yellow_card[i] - weights['recent_Red_card'] * recent_Red_card[i] - weights['recent_Offside'] * recent_Offside[i]+weights['recent_Pass_accuracy']*recent_Pass_accuracy[i]+weights['recent_Keypasses']*recent_Keypasses[i]+weights['Right_foot_goals']*Right_foot_goals[i]
    sheet.append(('Left Winger', best_left_winger_name,1,per,Jersey_num[i]))
    
elif team_strength=='Good teams':
    if count_2 >6:
        i=second_best_left_winger_idx
        per=weights['Market_value'] * Market_value[i]+ weights['position_list'] * position_list[i] + weights['goals'] * (goals[i] / apperence[i]) + weights['assists'] * (assists[i] / apperence[i]) + weights['againts_team_goals'] * againts_team_goals[i] + weights['againts_team_assists'] * againts_team_assists[i] + weights['Shots'] * Shots[i] + weights['ShotsOnTarget'] * ShotsOnTarget[i] + weights['Penalty'] * Penalty[i] + weights['Free_kick'] * Free_kick[i] - weights['Big_chances_missed'] * Big_chances_missed[i] + weights['Shooting_accuracy'] * Shooting_accuracy[i] + weights['Big_chances_created'] * Big_chances_created[i] + weights['Crosees'] * Crosees[i] + weights['Passes'] * Passes[i] - weights['Off_side'] * Off_side[i]+weights['Tackles_per_game'] * Tackles_per_game[i] +weights['Block_shots_per_game'] * Block_shots_per_game[i]+weights['interceptions_per_game'] * interceptions_per_game[i]+weights['Total_clearance_per_game'] * Total_clearance_per_game[i]  + weights['seasonal_goals'] * (seasonal_goals[i] / seasonal_apperence[i]) + weights['seasonal_assists'] * (seasonal_assists[i] / seasonal_apperence[i]) - weights['seasonal_Yellow'] * seasonal_Yellow[i] - weights['seasonal_Red'] * seasonal_Red[i] - weights['seasonal_Second_Yellow'] * seasonal_Second_Yellow[i] + weights['recent_Goals'] * recent_Goals[i] + weights['recent_Assists'] * recent_Assists[i] + weights['recent_Shots'] * recent_Shots[i] + weights['recent_ShotOnTarget'] * recent_ShotOnTarget[i] - weights['recent_Fouls'] * recent_Fouls[i] - weights['recent_Yellow_card'] * recent_Yellow_card[i] - weights['recent_Red_card'] * recent_Red_card[i] - weights['recent_Offside'] * recent_Offside[i]+weights['recent_Pass_accuracy']*recent_Pass_accuracy[i]+weights['recent_Keypasses']*recent_Keypasses[i]+weights['Right_foot_goals']*Right_foot_goals[i]
        sheet.append(('Left Winger', second_best_left_winger_name,2,per,Jersey_num[i]))
        
    else:
        i=best_left_winger_idx
        per=weights['Market_value'] * Market_value[i]+ weights['position_list'] * position_list[i] + weights['goals'] * (goals[i] / apperence[i]) + weights['assists'] * (assists[i] / apperence[i]) + weights['againts_team_goals'] * againts_team_goals[i] + weights['againts_team_assists'] * againts_team_assists[i] + weights['Shots'] * Shots[i] + weights['ShotsOnTarget'] * ShotsOnTarget[i] + weights['Penalty'] * Penalty[i] + weights['Free_kick'] * Free_kick[i] - weights['Big_chances_missed'] * Big_chances_missed[i] + weights['Shooting_accuracy'] * Shooting_accuracy[i] + weights['Big_chances_created'] * Big_chances_created[i] + weights['Crosees'] * Crosees[i] + weights['Passes'] * Passes[i] - weights['Off_side'] * Off_side[i] +weights['Tackles_per_game'] * Tackles_per_game[i] +weights['Block_shots_per_game'] * Block_shots_per_game[i]+weights['interceptions_per_game'] * interceptions_per_game[i]+weights['Total_clearance_per_game'] * Total_clearance_per_game[i] + weights['seasonal_goals'] * (seasonal_goals[i] / seasonal_apperence[i]) + weights['seasonal_assists'] * (seasonal_assists[i] / seasonal_apperence[i]) - weights['seasonal_Yellow'] * seasonal_Yellow[i] - weights['seasonal_Red'] * seasonal_Red[i] - weights['seasonal_Second_Yellow'] * seasonal_Second_Yellow[i] + weights['recent_Goals'] * recent_Goals[i] + weights['recent_Assists'] * recent_Assists[i] + weights['recent_Shots'] * recent_Shots[i] + weights['recent_ShotOnTarget'] * recent_ShotOnTarget[i] - weights['recent_Fouls'] * recent_Fouls[i] - weights['recent_Yellow_card'] * recent_Yellow_card[i] - weights['recent_Red_card'] * recent_Red_card[i] - weights['recent_Offside'] * recent_Offside[i]+weights['recent_Pass_accuracy']*recent_Pass_accuracy[i]+weights['recent_Keypasses']*recent_Keypasses[i]+weights['Right_foot_goals']*Right_foot_goals[i]
        sheet.append(('Left Winger', best_left_winger_name,1,per,Jersey_num[i]))
    
elif team_strength=='Middle teams':
    if count_2 >5:
        i=second_best_left_winger_idx
        per=weights['Market_value'] * Market_value[i]+ weights['position_list'] * position_list[i] + weights['goals'] * (goals[i] / apperence[i]) + weights['assists'] * (assists[i] / apperence[i]) + weights['againts_team_goals'] * againts_team_goals[i] + weights['againts_team_assists'] * againts_team_assists[i] + weights['Shots'] * Shots[i] + weights['ShotsOnTarget'] * ShotsOnTarget[i] + weights['Penalty'] * Penalty[i] + weights['Free_kick'] * Free_kick[i] - weights['Big_chances_missed'] * Big_chances_missed[i] + weights['Shooting_accuracy'] * Shooting_accuracy[i] + weights['Big_chances_created'] * Big_chances_created[i] + weights['Crosees'] * Crosees[i] + weights['Passes'] * Passes[i] - weights['Off_side'] * Off_side[i] +weights['Tackles_per_game'] * Tackles_per_game[i] +weights['Block_shots_per_game'] * Block_shots_per_game[i]+weights['interceptions_per_game'] * interceptions_per_game[i]+weights['Total_clearance_per_game'] * Total_clearance_per_game[i] + weights['seasonal_goals'] * (seasonal_goals[i] / seasonal_apperence[i]) + weights['seasonal_assists'] * (seasonal_assists[i] / seasonal_apperence[i]) - weights['seasonal_Yellow'] * seasonal_Yellow[i] - weights['seasonal_Red'] * seasonal_Red[i] - weights['seasonal_Second_Yellow'] * seasonal_Second_Yellow[i] + weights['recent_Goals'] * recent_Goals[i] + weights['recent_Assists'] * recent_Assists[i] + weights['recent_Shots'] * recent_Shots[i] + weights['recent_ShotOnTarget'] * recent_ShotOnTarget[i] - weights['recent_Fouls'] * recent_Fouls[i] - weights['recent_Yellow_card'] * recent_Yellow_card[i] - weights['recent_Red_card'] * recent_Red_card[i] - weights['recent_Offside'] * recent_Offside[i]+weights['recent_Pass_accuracy']*recent_Pass_accuracy[i]+weights['recent_Keypasses']*recent_Keypasses[i]+weights['Right_foot_goals']*Right_foot_goals[i]
        sheet.append(('Left Winger', second_best_left_winger_name,2,per,Jersey_num[i]))
        
        
    else:
        i=best_left_winger_idx
        per=weights['Market_value'] * Market_value[i]+ weights['position_list'] * position_list[i] + weights['goals'] * (goals[i] / apperence[i]) + weights['assists'] * (assists[i] / apperence[i]) + weights['againts_team_goals'] * againts_team_goals[i] + weights['againts_team_assists'] * againts_team_assists[i] + weights['Shots'] * Shots[i] + weights['ShotsOnTarget'] * ShotsOnTarget[i] + weights['Penalty'] * Penalty[i] + weights['Free_kick'] * Free_kick[i] - weights['Big_chances_missed'] * Big_chances_missed[i] + weights['Shooting_accuracy'] * Shooting_accuracy[i] + weights['Big_chances_created'] * Big_chances_created[i] + weights['Crosees'] * Crosees[i] + weights['Passes'] * Passes[i] - weights['Off_side'] * Off_side[i] +weights['Tackles_per_game'] * Tackles_per_game[i] +weights['Block_shots_per_game'] * Block_shots_per_game[i]+weights['interceptions_per_game'] * interceptions_per_game[i]+weights['Total_clearance_per_game'] * Total_clearance_per_game[i] + weights['seasonal_goals'] * (seasonal_goals[i] / seasonal_apperence[i]) + weights['seasonal_assists'] * (seasonal_assists[i] / seasonal_apperence[i]) - weights['seasonal_Yellow'] * seasonal_Yellow[i] - weights['seasonal_Red'] * seasonal_Red[i] - weights['seasonal_Second_Yellow'] * seasonal_Second_Yellow[i] + weights['recent_Goals'] * recent_Goals[i] + weights['recent_Assists'] * recent_Assists[i] + weights['recent_Shots'] * recent_Shots[i] + weights['recent_ShotOnTarget'] * recent_ShotOnTarget[i] - weights['recent_Fouls'] * recent_Fouls[i] - weights['recent_Yellow_card'] * recent_Yellow_card[i] - weights['recent_Red_card'] * recent_Red_card[i] - weights['recent_Offside'] * recent_Offside[i]+weights['recent_Pass_accuracy']*recent_Pass_accuracy[i]+weights['recent_Keypasses']*recent_Keypasses[i]+weights['Right_foot_goals']*Right_foot_goals[i]
        sheet.append(('Left Winger', best_left_winger_name,1,per,Jersey_num[i]))
    
elif team_strength=='Poor teams':
    if count_2 >4:
        i=second_best_left_winger_idx
        per=weights['Market_value'] * Market_value[i]+ weights['position_list'] * position_list[i] + weights['goals'] * (goals[i] / apperence[i]) + weights['assists'] * (assists[i] / apperence[i]) + weights['againts_team_goals'] * againts_team_goals[i] + weights['againts_team_assists'] * againts_team_assists[i] + weights['Shots'] * Shots[i] + weights['ShotsOnTarget'] * ShotsOnTarget[i] + weights['Penalty'] * Penalty[i] + weights['Free_kick'] * Free_kick[i] - weights['Big_chances_missed'] * Big_chances_missed[i] + weights['Shooting_accuracy'] * Shooting_accuracy[i] + weights['Big_chances_created'] * Big_chances_created[i] + weights['Crosees'] * Crosees[i] + weights['Passes'] * Passes[i] - weights['Off_side'] * Off_side[i]+weights['Tackles_per_game'] * Tackles_per_game[i] +weights['Block_shots_per_game'] * Block_shots_per_game[i]+weights['interceptions_per_game'] * interceptions_per_game[i]+weights['Total_clearance_per_game'] * Total_clearance_per_game[i]  + weights['seasonal_goals'] * (seasonal_goals[i] / seasonal_apperence[i]) + weights['seasonal_assists'] * (seasonal_assists[i] / seasonal_apperence[i]) - weights['seasonal_Yellow'] * seasonal_Yellow[i] - weights['seasonal_Red'] * seasonal_Red[i] - weights['seasonal_Second_Yellow'] * seasonal_Second_Yellow[i] + weights['recent_Goals'] * recent_Goals[i] + weights['recent_Assists'] * recent_Assists[i] + weights['recent_Shots'] * recent_Shots[i] + weights['recent_ShotOnTarget'] * recent_ShotOnTarget[i] - weights['recent_Fouls'] * recent_Fouls[i] - weights['recent_Yellow_card'] * recent_Yellow_card[i] - weights['recent_Red_card'] * recent_Red_card[i] - weights['recent_Offside'] * recent_Offside[i]+weights['recent_Pass_accuracy']*recent_Pass_accuracy[i]+weights['recent_Keypasses']*recent_Keypasses[i]+weights['Right_foot_goals']*Right_foot_goals[i]
        sheet.append(('Left Winger', second_best_left_winger_name,2,per,Jersey_num[i]))
        
        
    else:
        i=best_left_winger_idx
        per=weights['Market_value'] * Market_value[i]+ weights['position_list'] * position_list[i] + weights['goals'] * (goals[i] / apperence[i]) + weights['assists'] * (assists[i] / apperence[i]) + weights['againts_team_goals'] * againts_team_goals[i] + weights['againts_team_assists'] * againts_team_assists[i] + weights['Shots'] * Shots[i] + weights['ShotsOnTarget'] * ShotsOnTarget[i] + weights['Penalty'] * Penalty[i] + weights['Free_kick'] * Free_kick[i] - weights['Big_chances_missed'] * Big_chances_missed[i] + weights['Shooting_accuracy'] * Shooting_accuracy[i] + weights['Big_chances_created'] * Big_chances_created[i] + weights['Crosees'] * Crosees[i] + weights['Passes'] * Passes[i] - weights['Off_side'] * Off_side[i]+weights['Tackles_per_game'] * Tackles_per_game[i] +weights['Block_shots_per_game'] * Block_shots_per_game[i]+weights['interceptions_per_game'] * interceptions_per_game[i]+weights['Total_clearance_per_game'] * Total_clearance_per_game[i]  + weights['seasonal_goals'] * (seasonal_goals[i] / seasonal_apperence[i]) + weights['seasonal_assists'] * (seasonal_assists[i] / seasonal_apperence[i]) - weights['seasonal_Yellow'] * seasonal_Yellow[i] - weights['seasonal_Red'] * seasonal_Red[i] - weights['seasonal_Second_Yellow'] * seasonal_Second_Yellow[i] + weights['recent_Goals'] * recent_Goals[i] + weights['recent_Assists'] * recent_Assists[i] + weights['recent_Shots'] * recent_Shots[i] + weights['recent_ShotOnTarget'] * recent_ShotOnTarget[i] - weights['recent_Fouls'] * recent_Fouls[i] - weights['recent_Yellow_card'] * recent_Yellow_card[i] - weights['recent_Red_card'] * recent_Red_card[i] - weights['recent_Offside'] * recent_Offside[i]+weights['recent_Pass_accuracy']*recent_Pass_accuracy[i]+weights['recent_Keypasses']*recent_Keypasses[i]+weights['Right_foot_goals']*Right_foot_goals[i]
        sheet.append(('Left Winger', best_left_winger_name,1,per,Jersey_num[i]))
    
else:
    print("please check agints team name")
    
        
wb.save('C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/players.xlsx')    
# Append the player's name and position





