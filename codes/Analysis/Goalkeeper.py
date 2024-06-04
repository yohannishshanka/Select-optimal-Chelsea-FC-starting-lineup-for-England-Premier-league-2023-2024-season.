#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.core.display import HTML
#display(HTML("<script>Jupyter.notebook.kernel.restart()</script>"))
from IPython.display import display, Javascript

def restart_kernel():
    display(Javascript('IPython.notebook.kernel.restart(force=True)'))

restart_kernel()


# In[ ]:


import time 
import pandas as pd
#time.sleep(5)

#import datasets
df = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/player data/player_data.xlsx')
df1 = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/Comparison/Goalkeeper player data/Goalkeeper cleansheet data.xlsx')
df2 = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/Comparison/Goalkeeper player data/Goalkeeper conceeded goal data.xlsx')
df3 = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/perfomance/Goal keeper/Goalkeeper_data.xlsx')
df4 = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/last 5 games/last 5 games.xlsx')
df5 = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/player_current/seasonal_data.xlsx')
df6 = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/players.xlsx')
df7 = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/Rating/team_strength.xlsx')

selected_players = df6['Player'].tolist()

#preprocesing
df['Other Positions'] = df['Other Positions'].str.replace('\n', ', ')
df['Height'] = df['Height'].str.replace('\n', '')
mask = df['Market value'].str.contains('k')
df.loc[mask, 'Market value'] = '0.' + df.loc[mask, 'Market value'].str.replace('k', '')
df['Market value']=df['Market value'].str.replace('m', '')
df['Market value'] = df['Market value'].replace('-', '0')
df['Market value'] = pd.to_numeric(df['Market value'])


df['Goal conceded'] = df['Goal conceded'].replace('-', '0')
df['Clean sheet'] = df['Clean sheet'].replace('-', '0')
df['Goal conceded'] = df['Goal conceded'].astype(int)
df['Clean sheet'] = df['Clean sheet'].astype(int)
df['Appearance'] = df['Appearance'].astype(int)
df1 = df1.replace({"-": 0}).fillna(0)
df2 = df2.replace({"-": 0}).fillna(0)
df1 = df1.fillna(0)
df2 = df2.fillna(0)
df3 = df3.fillna(0)
df4 = df4.fillna(0)
df5 = df5.fillna(0)

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

#standization
cols_to_standardize = df.columns.difference(["Player", "Position", "Other Positions", "Height", "Jersey num", "Injury update","Goals","Assists","Date of birth/Age","Dominant foot"])
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

#filter players can play Goalkeeper
filtered_df = df[(df['Position'] == 'Goalkeeper') ] 
filtered_df = filtered_df[~filtered_df['Player'].isin(selected_players)]
#filter all data set
filtered_df1 = df1[df1['Player'].isin(filtered_df['Player'].tolist())]
filtered_df2 = df2[df2['Player'].isin(filtered_df['Player'].tolist())]
filtered_df3 = df3[df3['Player'].isin(filtered_df['Player'].tolist())]
filtered_df4 = df4[df4['Player'].isin(filtered_df['Player'].tolist())]
filtered_df5 = df5[df5['Player'].isin(filtered_df['Player'].tolist())]

import pandas as pd


file_path = 'C:/Users/Admin/Documents/research final - chelsea/Research/Strength and weakness/Strength and weakness.xlsx'
sheet_name = "Arsenal"

#opposint team strengths
df6= pd.read_excel(file_path, sheet_name=sheet_name)

tasks_strengths = df6[(df6['Strength/Weakness'] == 'Very Strong') | (df6['Strength/Weakness'] == 'Strong')]

additional_weigth=[]


kpi_list = ['Counter attacks', 'Attacking set pieces','Finishing scoring chances', 'Shooting from direct free kicks']


tasks_strengths['Matched KPIs'] = tasks_strengths['KPIs'].apply(lambda x: sum(kpi in x for kpi in kpi_list))


for index, row in tasks_strengths.iterrows():
    if row['Matched KPIs'] == 4:
        additional_weigth.append(4)
    elif row['Matched KPIs'] == 3:
        additional_weigth.append(3)
    elif row['Matched KPIs'] == 1:
        additional_weigth.append(1)
    else:
        additional_weigth.append(0)
     

from ortools.linear_solver import pywraplp

def select_best_goalkeeper(apperence,seasonal_apperence, Goal_conceeded, Clean_Sheet, againts_team_cleansheet, againts_team_conceeded_goal, Market_value, Penalty_Saved,Total_punches_per_game, high_claims_per_game, catches_per_game, Sweeper_clearence_per_game, accurate_long_balls_per_game,error_lead_to_goal, Own_goals, Passses_per_game,Total_saves_per_game,seasonal_Goal_conceeded,seasonal_Clean_Sheet,seasonal_Yellow,seasonal_Red,seasonal_Second_Yellow,recent_Goal_conceeded,recent_Saves,recent_Clean_sheet,recent_Fouls,recent_Yellow_card,recent_Red_card,recent_Long_passes, weights):
    # Create a solver
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        return None, None
    
    # Define variables
    num_goalkeeper = len(Goal_conceeded)
    x = [solver.IntVar(0, 1, f'x{i}') for i in range(num_goalkeeper)]

    # Define objective function
    objective = solver.Objective()
    for i in range(num_goalkeeper):
        objective.SetCoefficient(x[i],-weights['Goal_conceeded'] * (Goal_conceeded[i] / apperence[i]) + weights['Clean_Sheet'] * (Clean_Sheet[i] / apperence[i]) + weights['againts_team_cleansheet'] *  againts_team_cleansheet[i] + weights['againts_team_conceeded_goal'] * againts_team_conceeded_goal[i] + weights['Market_value'] * Market_value[i] + weights['Penalty_Saved'] *  Penalty_Saved[i] + weights['Total_punches_per_game'] * Total_punches_per_game[i] + weights['high_claims_per_game'] * high_claims_per_game[i] + weights['catches_per_game'] * catches_per_game[i] + weights['Sweeper_clearence_per_game'] * Sweeper_clearence_per_game[i] + weights['accurate_long_balls_per_game'] * accurate_long_balls_per_game[i] - weights['error_lead_to_goal'] * error_lead_to_goal[i] - weights['Own_goals'] * Own_goals[i] + weights['Total_saves_per_game'] * Total_saves_per_game[i] +weights['Passses_per_game'] * Passses_per_game[i]-weights['seasonal_Goal_conceeded'] * (seasonal_Goal_conceeded[i] / seasonal_apperence[i])+weights['seasonal_Clean_Sheet'] * (seasonal_Clean_Sheet[i] / seasonal_apperence[i])-weights['seasonal_Yellow'] * seasonal_Yellow[i]-weights['seasonal_Red'] * seasonal_Red[i]- weights['seasonal_Second_Yellow'] * seasonal_Second_Yellow[i]-weights['recent_Goal_conceeded'] * recent_Goal_conceeded[i]+weights['recent_Clean_sheet'] * recent_Clean_sheet[i]+weights['recent_Saves'] * recent_Saves[i]-weights['recent_Fouls'] * recent_Fouls[i]-weights['recent_Yellow_card'] * recent_Yellow_card[i]-weights['recent_Red_card'] * recent_Red_card[i]+weights['recent_Long_passes'] * recent_Long_passes[i])
    objective.SetMaximization()
    
    # Add constraint
    solver.Add(sum(x[i] for i in range(num_goalkeeper)) == 2)  # Select 2 forwards
    
    # Solve the problem
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL:
        selected_goalkeeper = [i for i in range(num_goalkeeper) if x[i].solution_value() == 1]
        return selected_goalkeeper
    else:
        return None, None

# data
names = filtered_df["Player"].to_list()
Goal_conceeded = filtered_df["Goal conceded"].to_list()
Clean_Sheet = filtered_df["Clean sheet"].to_list()
apperence = filtered_df["Appearance"].to_list()
Market_value = filtered_df["Market value"].to_list()
againts_team_cleansheet= filtered_df1[sheet_name].to_list()
againts_team_conceeded_goal= filtered_df2[sheet_name].to_list()
Penalty_Saved= filtered_df3["Penalty saved"].to_list()
Total_punches_per_game= filtered_df3["Total punches per game"].to_list()
high_claims_per_game= filtered_df3["High claims per game"].to_list()
catches_per_game= filtered_df3["Catches per game"].to_list()
Sweeper_clearence_per_game= filtered_df3["Sweeper clearence per game"].to_list()
accurate_long_balls_per_game= filtered_df3["Accurate long balls per game"].to_list()
error_lead_to_goal= filtered_df3["Error leading to a goals"].to_list()
Own_goals= filtered_df3["Own goals"].to_list()
Passses_per_game= filtered_df3["Passes per game"].to_list()
Total_saves_per_game= filtered_df3["Total saves per game"].to_list()
seasonal_apperence= filtered_df5["Season appearance"].to_list()
seasonal_Goal_conceeded= filtered_df5["Goal conceded"].to_list()
seasonal_Clean_Sheet= filtered_df5["Clean sheet"].to_list()
seasonal_Yellow= filtered_df5["Yellow cards"].to_list()
seasonal_Red= filtered_df5["Red cards"].to_list()
seasonal_Second_Yellow= filtered_df5["Second yellow cards"].to_list()
recent_Goal_conceeded= filtered_df4["Goal conceded"].to_list()
recent_Saves= filtered_df4["Saves"].to_list()
recent_Clean_sheet= filtered_df4["Clean sheet"].to_list()
recent_Fouls= filtered_df4["Fouls"].to_list()
recent_Yellow_card= filtered_df4["Yellow card"].to_list()
recent_Red_card= filtered_df4["Red card"].to_list()
recent_Long_passes= filtered_df4["Long passes"].to_list()
Jersey_num= filtered_df["Jersey num"].to_list()




weights = {'Goal_conceeded': 4, 'Clean_Sheet': 4,'againts_team_cleansheet' : 4 ,'againts_team_conceeded_goal': 4,'Market_value': 1, 'Penalty_Saved': 2+additional_weigth[0],'Total_punches_per_game' : 2+additional_weigth[0] ,'high_claims_per_game' : 2+additional_weigth[0],'catches_per_game': 2+additional_weigth[0],'Sweeper_clearence_per_game' : 2+additional_weigth[0] ,'accurate_long_balls_per_game' : 2,'error_lead_to_goal': 2,'Own_goals' : 2,'Passses_per_game': 1,'Total_saves_per_game':2+additional_weigth[0],'seasonal_Goal_conceeded':6,'seasonal_Clean_Sheet':6,'seasonal_Yellow':3,'seasonal_Red':3,'seasonal_Second_Yellow':3,'recent_Goal_conceeded':8,'recent_Saves':4,'recent_Clean_sheet':8,'recent_Fouls':4,'recent_Yellow_card':4,'recent_Red_card':4,'recent_Long_passes':4}

# Select the best and second-best goalkeeper
selected_goalkeeper = select_best_goalkeeper(apperence,seasonal_apperence, Goal_conceeded, Clean_Sheet, againts_team_cleansheet, againts_team_conceeded_goal, Market_value, Penalty_Saved,Total_punches_per_game, high_claims_per_game, catches_per_game, Sweeper_clearence_per_game, accurate_long_balls_per_game,error_lead_to_goal, Own_goals, Passses_per_game,Total_saves_per_game,seasonal_Goal_conceeded,seasonal_Clean_Sheet,seasonal_Yellow,seasonal_Red,seasonal_Second_Yellow,recent_Goal_conceeded,recent_Saves,recent_Clean_sheet,recent_Fouls,recent_Yellow_card,recent_Red_card,recent_Long_passes, weights)
selected_goalkeeper.sort(key=lambda x: -weights['Goal_conceeded'] * (Goal_conceeded[x] / apperence[x]) + weights['Clean_Sheet'] * (Clean_Sheet[x] / apperence[x]) + weights['againts_team_cleansheet'] * againts_team_cleansheet[x] + weights['againts_team_conceeded_goal'] * againts_team_conceeded_goal[x] + weights['Market_value'] * Market_value[x] + weights['Penalty_Saved'] * Penalty_Saved[x] + weights['Total_punches_per_game'] * Total_punches_per_game[x] + weights['high_claims_per_game'] * high_claims_per_game[x] + weights['catches_per_game'] * catches_per_game[x] + weights['Sweeper_clearence_per_game'] * Sweeper_clearence_per_game[x] + weights['accurate_long_balls_per_game'] * accurate_long_balls_per_game[x] - weights['error_lead_to_goal'] * error_lead_to_goal[x] - weights['Own_goals'] * Own_goals[x] + weights['Total_saves_per_game'] * Total_saves_per_game[x] + weights['Passses_per_game'] * Passses_per_game[x] - weights['seasonal_Goal_conceeded'] * (seasonal_Goal_conceeded[x] / seasonal_apperence[x]) + weights['seasonal_Clean_Sheet'] * (seasonal_Clean_Sheet[x] / seasonal_apperence[x]) - weights['seasonal_Yellow'] * seasonal_Yellow[x] - weights['seasonal_Red'] * seasonal_Red[x] - weights['seasonal_Second_Yellow'] * seasonal_Second_Yellow[x] - weights['recent_Goal_conceeded'] * recent_Goal_conceeded[x] + weights['recent_Clean_sheet'] * recent_Clean_sheet[x] + weights['recent_Saves'] * recent_Saves[x] - weights['recent_Fouls'] * recent_Fouls[x] - weights['recent_Yellow_card'] * recent_Yellow_card[x] - weights['recent_Red_card'] * recent_Red_card[x]+weights['recent_Long_passes'] * recent_Long_passes[x], reverse=True)

# Get the names of the two best goalkeeper
best_goalkeeper_idx = selected_goalkeeper[0]
second_best_goalkeeper_idx = selected_goalkeeper[1]
best_goalkeeper_name = names[best_goalkeeper_idx]
second_best_goalkeeper_name = names[second_best_goalkeeper_idx]

team_strength = df7.loc[df7['Team'] == sheet_name, 'Team Strength'].values[0] if sheet_name in df7['Team'].values else None


from openpyxl import load_workbook 
wb= load_workbook('C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/players.xlsx')


#opposint team strengths
sheet = wb.active

if team_strength=='Big six':
    i=best_goalkeeper_idx
    per= -weights['Goal_conceeded'] * (Goal_conceeded[i] / apperence[i]) + weights['Clean_Sheet'] * (Clean_Sheet[i] / apperence[i]) + weights['againts_team_cleansheet'] *  againts_team_cleansheet[i] + weights['againts_team_conceeded_goal'] * againts_team_conceeded_goal[i] + weights['Market_value'] * Market_value[i] + weights['Penalty_Saved'] *  Penalty_Saved[i] + weights['Total_punches_per_game'] * Total_punches_per_game[i] + weights['high_claims_per_game'] * high_claims_per_game[i] + weights['catches_per_game'] * catches_per_game[i] + weights['Sweeper_clearence_per_game'] * Sweeper_clearence_per_game[i] + weights['accurate_long_balls_per_game'] * accurate_long_balls_per_game[i] - weights['error_lead_to_goal'] * error_lead_to_goal[i] - weights['Own_goals'] * Own_goals[i] + weights['Total_saves_per_game'] * Total_saves_per_game[i] +weights['Passses_per_game'] * Passses_per_game[i]-weights['seasonal_Goal_conceeded'] * (seasonal_Goal_conceeded[i] / seasonal_apperence[i])+weights['seasonal_Clean_Sheet'] * (seasonal_Clean_Sheet[i] / seasonal_apperence[i])-weights['seasonal_Yellow'] * seasonal_Yellow[i]-weights['seasonal_Red'] * seasonal_Red[i]- weights['seasonal_Second_Yellow'] * seasonal_Second_Yellow[i]-weights['recent_Goal_conceeded'] * recent_Goal_conceeded[i]+weights['recent_Clean_sheet'] * recent_Clean_sheet[i]+weights['recent_Saves'] * recent_Saves[i]-weights['recent_Fouls'] * recent_Fouls[i]-weights['recent_Yellow_card'] * recent_Yellow_card[i]-weights['recent_Red_card'] * recent_Red_card[i]+weights['recent_Long_passes'] * recent_Long_passes[i]
    sheet.append(('Goalkeeper', best_goalkeeper_name,1,per,Jersey_num[i]))
    
elif team_strength=='Good teams':
    i=best_goalkeeper_idx
    per= -weights['Goal_conceeded'] * (Goal_conceeded[i] / apperence[i]) + weights['Clean_Sheet'] * (Clean_Sheet[i] / apperence[i]) + weights['againts_team_cleansheet'] *  againts_team_cleansheet[i] + weights['againts_team_conceeded_goal'] * againts_team_conceeded_goal[i] + weights['Market_value'] * Market_value[i] + weights['Penalty_Saved'] *  Penalty_Saved[i] + weights['Total_punches_per_game'] * Total_punches_per_game[i] + weights['high_claims_per_game'] * high_claims_per_game[i] + weights['catches_per_game'] * catches_per_game[i] + weights['Sweeper_clearence_per_game'] * Sweeper_clearence_per_game[i] + weights['accurate_long_balls_per_game'] * accurate_long_balls_per_game[i] - weights['error_lead_to_goal'] * error_lead_to_goal[i] - weights['Own_goals'] * Own_goals[i] + weights['Total_saves_per_game'] * Total_saves_per_game[i] +weights['Passses_per_game'] * Passses_per_game[i]-weights['seasonal_Goal_conceeded'] * (seasonal_Goal_conceeded[i] / seasonal_apperence[i])+weights['seasonal_Clean_Sheet'] * (seasonal_Clean_Sheet[i] / seasonal_apperence[i])-weights['seasonal_Yellow'] * seasonal_Yellow[i]-weights['seasonal_Red'] * seasonal_Red[i]- weights['seasonal_Second_Yellow'] * seasonal_Second_Yellow[i]-weights['recent_Goal_conceeded'] * recent_Goal_conceeded[i]+weights['recent_Clean_sheet'] * recent_Clean_sheet[i]+weights['recent_Saves'] * recent_Saves[i]-weights['recent_Fouls'] * recent_Fouls[i]-weights['recent_Yellow_card'] * recent_Yellow_card[i]-weights['recent_Red_card'] * recent_Red_card[i]+weights['recent_Long_passes'] * recent_Long_passes[i]
    sheet.append(('Goalkeeper', best_goalkeeper_name,1,per,Jersey_num[i]))
          
elif team_strength=='Middle teams':
    
    i=second_best_goalkeeper_idx
    per=-weights['Goal_conceeded'] * (Goal_conceeded[i] / apperence[i]) + weights['Clean_Sheet'] * (Clean_Sheet[i] / apperence[i]) + weights['againts_team_cleansheet'] *  againts_team_cleansheet[i] + weights['againts_team_conceeded_goal'] * againts_team_conceeded_goal[i] + weights['Market_value'] * Market_value[i] + weights['Penalty_Saved'] *  Penalty_Saved[i] + weights['Total_punches_per_game'] * Total_punches_per_game[i] + weights['high_claims_per_game'] * high_claims_per_game[i] + weights['catches_per_game'] * catches_per_game[i] + weights['Sweeper_clearence_per_game'] * Sweeper_clearence_per_game[i] + weights['accurate_long_balls_per_game'] * accurate_long_balls_per_game[i] - weights['error_lead_to_goal'] * error_lead_to_goal[i] - weights['Own_goals'] * Own_goals[i] + weights['Total_saves_per_game'] * Total_saves_per_game[i] +weights['Passses_per_game'] * Passses_per_game[i]-weights['seasonal_Goal_conceeded'] * (seasonal_Goal_conceeded[i] / seasonal_apperence[i])+weights['seasonal_Clean_Sheet'] * (seasonal_Clean_Sheet[i] / seasonal_apperence[i])-weights['seasonal_Yellow'] * seasonal_Yellow[i]-weights['seasonal_Red'] * seasonal_Red[i]- weights['seasonal_Second_Yellow'] * seasonal_Second_Yellow[i]-weights['recent_Goal_conceeded'] * recent_Goal_conceeded[i]+weights['recent_Clean_sheet'] * recent_Clean_sheet[i]+weights['recent_Saves'] * recent_Saves[i]-weights['recent_Fouls'] * recent_Fouls[i]-weights['recent_Yellow_card'] * recent_Yellow_card[i]-weights['recent_Red_card'] * recent_Red_card[i]+weights['recent_Long_passes'] * recent_Long_passes[i]
    sheet.append(('Goalkeeper', second_best_goalkeeper_name,2,per,Jersey_num[i]))
        
elif team_strength=='Poor teams':
    i=second_best_goalkeeper_idx
    per= -weights['Goal_conceeded'] * (Goal_conceeded[i] / apperence[i]) + weights['Clean_Sheet'] * (Clean_Sheet[i] / apperence[i]) + weights['againts_team_cleansheet'] *  againts_team_cleansheet[i] + weights['againts_team_conceeded_goal'] * againts_team_conceeded_goal[i] + weights['Market_value'] * Market_value[i] + weights['Penalty_Saved'] *  Penalty_Saved[i] + weights['Total_punches_per_game'] * Total_punches_per_game[i] + weights['high_claims_per_game'] * high_claims_per_game[i] + weights['catches_per_game'] * catches_per_game[i] + weights['Sweeper_clearence_per_game'] * Sweeper_clearence_per_game[i] + weights['accurate_long_balls_per_game'] * accurate_long_balls_per_game[i] - weights['error_lead_to_goal'] * error_lead_to_goal[i] - weights['Own_goals'] * Own_goals[i] + weights['Total_saves_per_game'] * Total_saves_per_game[i] +weights['Passses_per_game'] * Passses_per_game[i]-weights['seasonal_Goal_conceeded'] * (seasonal_Goal_conceeded[i] / seasonal_apperence[i])+weights['seasonal_Clean_Sheet'] * (seasonal_Clean_Sheet[i] / seasonal_apperence[i])-weights['seasonal_Yellow'] * seasonal_Yellow[i]-weights['seasonal_Red'] * seasonal_Red[i]- weights['seasonal_Second_Yellow'] * seasonal_Second_Yellow[i]-weights['recent_Goal_conceeded'] * recent_Goal_conceeded[i]+weights['recent_Clean_sheet'] * recent_Clean_sheet[i]+weights['recent_Saves'] * recent_Saves[i]-weights['recent_Fouls'] * recent_Fouls[i]-weights['recent_Yellow_card'] * recent_Yellow_card[i]-weights['recent_Red_card'] * recent_Red_card[i]+weights['recent_Long_passes'] * recent_Long_passes[i]
    sheet.append(('Goalkeeper', second_best_goalkeeper_name,2,per,Jersey_num[i]))
     
else:
    print("please check agints team name")
        
wb.save('C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/players.xlsx')    


