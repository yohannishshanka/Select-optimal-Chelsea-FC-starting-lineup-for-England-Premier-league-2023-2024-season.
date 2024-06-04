
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
df1 = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/Comparison/Other players data/players goal data.xlsx')
df2 = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/Comparison/Other players data/players assist data.xlsx')
df3 = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/perfomance/Mid fielder/midfield players data.xlsx')
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
df3['Tackles accuracy'] = df3['Tackles accuracy'].str.replace('%', '')
df3['Crosses accuracy'] = df3['Crosses accuracy'].str.replace('%', '')




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

df3['Shooting accuracy']= df3['Shooting accuracy']*0.01
df3['Tackles accuracy']= df3['Tackles accuracy']*0.01
df3['Crosses accuracy']= df3['Crosses accuracy']*0.01
df4['Pass accuracy']= df4['Pass accuracy']*0.01
#standization
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

#filter players can play attacking  midfielder
filtered_df = df[((df['Position'] == 'Central Midfield') |df['Other Positions'].str.contains('Central Midfield') |(df['Position'] == 'Attacking Midfield') |df['Other Positions'].str.contains('Attacking Midfield'))  ]
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
df8= pd.read_excel(file_path, sheet_name=sheet_name)

tasks_strengths = df8[(df8['Strength/Weakness'] == 'Very Strong') | (df8['Strength/Weakness'] == 'Strong')]

additional_weigth=[]
Creating_long_weigth=[]
Stealing_the_ball_weigth=[]


kpi_list = ['Defending counter attacks', 'Defending against long shots','Protecting the lead', 'Defending set pieces', 'Defending against attacks down the wings']


tasks_strengths['Matched KPIs'] = tasks_strengths['KPIs'].apply(lambda x: sum(kpi in x for kpi in kpi_list))
additional_weigth=[]


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

        
tasks_strengths['Matched KPIs'] = tasks_strengths['KPIs'].apply(lambda x: 'Creating long shot opportunities' in x)

for index, row in tasks_strengths.iterrows():
    if row['Matched KPIs']:
        Creating_long_weigth.append(2)
    else:
        Creating_long_weigth.append(0)

tasks_strengths['Matched KPIs'] = tasks_strengths['KPIs'].apply(lambda x: 'Stealing the ball from the opposition' in x)
        
for index, row in tasks_strengths.iterrows():
    if row['Matched KPIs']:
        Stealing_the_ball_weigth.append(2)
    else:
        Stealing_the_ball_weigth.append(0)
        





        

from ortools.linear_solver import pywraplp

def select_best_attacking_midfielder(Market_value,apperence,position_list,seasonal_apperence, goals, assists, againts_team_goals, againts_team_assists, accurate_long_balls_per_game, Big_chances_created_per_game, Block_shots_per_game, Passes_per_game, tackles_accuracy, Crosses_accuracy, Clearence_per_game, Interception_per_game, Fouls_per_game, Duels_won_per_game, Aerial_won_per_game,seasonal_goals,seasonal_assists,seasonal_Yellow,seasonal_Red,seasonal_Second_Yellow,recent_Goals,recent_Assists,recent_Shots,recent_ShotOnTarget,recent_Fouls,recent_Yellow_card,recent_Red_card,recent_Offside,recent_Clearances,recent_Pass_accuracy,recent_Key_passes, weights):
    # Create a solver
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        return None, None
    
    # Define variables
    num_attacking_midfielder = len(goals)
    x = [solver.IntVar(0, 1, f'x{i}') for i in range(num_attacking_midfielder)]

    # Define objective function
    objective = solver.Objective()
    for i in range(num_attacking_midfielder):
        objective.SetCoefficient(x[i],weights['Market_value'] * Market_value[i]+weights['position_list'] * position_list[i]+ weights['goals'] * (goals[i] / apperence[i]) + weights['assists'] * (assists[i] / apperence[i]) + weights['againts_team_goals'] * againts_team_goals[i] + weights['againts_team_assists'] * againts_team_assists[i] + weights['accurate_long_balls_per_game'] * accurate_long_balls_per_game[i] + weights['Big_chances_created_per_game'] * Big_chances_created_per_game[i] + weights['Block_shots_per_game'] * Block_shots_per_game[i] + weights['Passes_per_game'] * Passes_per_game[i] + weights['tackles_accuracy'] * tackles_accuracy[i] + weights['Crosses_accuracy'] * Crosses_accuracy[i] + weights['Clearence_per_game'] * Clearence_per_game[i] + weights['Interception_per_game'] * Interception_per_game[i] - weights['Fouls_per_game'] * Fouls_per_game[i] + weights['Duels_won_per_game'] * Duels_won_per_game[i] + weights['Aerial_won_per_game'] * Aerial_won_per_game[i] +weights['seasonal_goals'] * (seasonal_goals[i] / seasonal_apperence[i])+weights['seasonal_assists'] * (seasonal_assists[i] / seasonal_apperence[i])-weights['seasonal_Yellow'] * seasonal_Yellow[i]-weights['seasonal_Red'] * seasonal_Red[i]- weights['seasonal_Second_Yellow'] * seasonal_Second_Yellow[i]+weights['recent_Goals'] * recent_Goals[i]+weights['recent_Assists'] * recent_Assists[i]+weights['recent_Shots'] * recent_Shots[i]+weights['recent_ShotOnTarget'] * recent_ShotOnTarget[i]-weights['recent_Fouls'] * recent_Fouls[i]-weights['recent_Yellow_card'] * recent_Yellow_card[i]-weights['recent_Red_card'] * recent_Red_card[i]-weights['recent_Offside'] * recent_Offside[i]+ weights['recent_Clearances'] * recent_Clearances[i]+ weights['recent_Pass_accuracy'] * recent_Pass_accuracy[i]+ weights['recent_Key_passes'] * recent_Key_passes[i])
    objective.SetMaximization()
    
    # Add constraint
    solver.Add(sum(x[i] for i in range(num_attacking_midfielder)) == 2)  # Select 2 forwards
    
    # Solve the problem
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL:
        selected_attacking_midfielder = [i for i in range(num_attacking_midfielder) if x[i].solution_value() == 1]
        return selected_attacking_midfielder
    else:
        return None, None

#  data
names = filtered_df["Player"].to_list()
goals = filtered_df["Goals"].to_list()
position_list = [1 if position == "Attacking Midfield" else 0 for position in filtered_df["Position"]]
assists = filtered_df["Assists"].to_list()
apperence = filtered_df["Appearance"].to_list()
Market_value = filtered_df["Market value"].to_list()
againts_team_goals= filtered_df1[sheet_name].to_list()
againts_team_assists= filtered_df2[sheet_name].to_list()
accurate_long_balls_per_game= filtered_df3["Accurate long balls per game"].to_list()
Big_chances_created_per_game= filtered_df3["Big chances created per game"].to_list()
Block_shots_per_game= filtered_df3["Block shots per game"].to_list()
Passes_per_game= filtered_df3["Passes per game"].to_list()
tackles_accuracy= filtered_df3["Tackles accuracy"].to_list()
Crosses_accuracy= filtered_df3["Crosses accuracy"].to_list()
Clearence_per_game= filtered_df3["Total clearance per game"].to_list()
Interception_per_game= filtered_df3["Interceptions per game"].to_list()
Fouls_per_game= filtered_df3["Fouls per game"].to_list()
Duels_won_per_game= filtered_df3["Duels won per game"].to_list()
Aerial_won_per_game= filtered_df3["Aerial won per game"].to_list()
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
recent_Takels= filtered_df4["Tackles"].to_list()
recent_Clearances= filtered_df4["Clearances"].to_list()
recent_Pass_accuracy= filtered_df4["Pass accuracy"].to_list()
recent_Key_passes= filtered_df4["Key passes"].to_list()
Jersey_num= filtered_df["Jersey num"].to_list()



weights = {'Market_value':1,'position_list':1,'goals': 4, 'assists': 6,'againts_team_goals' : 4 ,'againts_team_assists' : 6,'accurate_long_balls_per_game': 2+Stealing_the_ball_weigth[0],'Big_chances_created_per_game': 4+additional_weigth[0], 'Block_shots_per_game': 2+Creating_long_weigth[0],'Passes_per_game' : 2 ,'tackles_accuracy' : 2,'Crosses_accuracy': 2+Stealing_the_ball_weigth[0],'Clearence_per_game' : 2 ,'Interception_per_game' : 2,'Fouls_per_game': 2,'Duels_won_per_game' : 2,'Aerial_won_per_game': 2,'seasonal_goals':6,'seasonal_assists':8,'seasonal_Yellow':2,'seasonal_Red':2,'seasonal_Second_Yellow':2,'recent_Goals':8,'recent_Assists':10,'recent_Shots':6,'recent_ShotOnTarget':6,'recent_Fouls':4,'recent_Yellow_card':4,'recent_Red_card':4,'recent_Offside':2,'recent_Clearances':4,'recent_Pass_accuracy':6,'recent_Key_passes':6}

# Select the best and second-best Attacking Midfield
selected_attacking_midfielder = select_best_attacking_midfielder(Market_value,apperence,position_list,seasonal_apperence, goals, assists, againts_team_goals, againts_team_assists, accurate_long_balls_per_game, Big_chances_created_per_game, Block_shots_per_game, Passes_per_game, tackles_accuracy, Crosses_accuracy, Clearence_per_game, Interception_per_game, Fouls_per_game, Duels_won_per_game, Aerial_won_per_game,seasonal_goals,seasonal_assists,seasonal_Yellow,seasonal_Red,seasonal_Second_Yellow,recent_Goals,recent_Assists,recent_Shots,recent_ShotOnTarget,recent_Fouls,recent_Yellow_card,recent_Red_card,recent_Offside,recent_Clearances,recent_Pass_accuracy,recent_Key_passes, weights)

selected_attacking_midfielder.sort(key=lambda x:weights['Market_value'] * Market_value[x]+ weights['position_list'] * position_list[x] + weights['goals'] * (goals[x] / apperence[x]) + weights['assists'] * (assists[x] / apperence[x]) + weights['againts_team_goals'] * againts_team_goals[x] + weights['againts_team_assists'] * againts_team_assists[x] + weights['accurate_long_balls_per_game'] * accurate_long_balls_per_game[x] + weights['Big_chances_created_per_game'] * Big_chances_created_per_game[x] + weights['Block_shots_per_game'] * Block_shots_per_game[x] + weights['Passes_per_game'] * Passes_per_game[x] + weights['tackles_accuracy'] * tackles_accuracy[x] + weights['Crosses_accuracy'] * Crosses_accuracy[x] + weights['Clearence_per_game'] * Clearence_per_game[x] + weights['Interception_per_game'] * Interception_per_game[x] - weights['Fouls_per_game'] * Fouls_per_game[x] + weights['Duels_won_per_game'] * Duels_won_per_game[x] + weights['Aerial_won_per_game'] * Aerial_won_per_game[x] + weights['seasonal_goals'] * (seasonal_goals[x] / seasonal_apperence[x]) + weights['seasonal_assists'] * (seasonal_assists[x] / seasonal_apperence[x]) - weights['seasonal_Yellow'] * seasonal_Yellow[x] - weights['seasonal_Red'] * seasonal_Red[x] - weights['seasonal_Second_Yellow'] * seasonal_Second_Yellow[x] + weights['recent_Goals'] * recent_Goals[x] + weights['recent_Assists'] * recent_Assists[x] + weights['recent_Shots'] * recent_Shots[x] + weights['recent_ShotOnTarget'] * recent_ShotOnTarget[x] - weights['recent_Fouls'] * recent_Fouls[x] - weights['recent_Yellow_card'] * recent_Yellow_card[x] - weights['recent_Red_card'] * recent_Red_card[x] - weights['recent_Offside'] * recent_Offside[x]  +  weights['recent_Clearances'] * recent_Clearances[x]+ weights['recent_Pass_accuracy'] * recent_Pass_accuracy[x]+ weights['recent_Key_passes'] * recent_Key_passes[x], reverse=True)



# Get the names of the two best Attacking Midfield
best_attacking_midfielder_idx = selected_attacking_midfielder[0]
second_best_attacking_midfielder_idx = selected_attacking_midfielder[1]
best_attacking_midfielder_name = names[best_attacking_midfielder_idx]
second_best_attacking_midfielder_name = names[second_best_attacking_midfielder_idx]



team_strength = df7.loc[df7['Team'] == sheet_name, 'Team Strength'].values[0] if sheet_name in df7['Team'].values else None


from openpyxl import load_workbook 
wb= load_workbook('C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/players.xlsx')


sheet = wb.active
#opposint team strengths
if team_strength=='Big six':
    i=best_attacking_midfielder_idx
    per=weights['Market_value'] * Market_value[i]+weights['position_list'] * position_list[i]+ weights['goals'] * (goals[i] / apperence[i]) + weights['assists'] * (assists[i] / apperence[i]) + weights['againts_team_goals'] * againts_team_goals[i] + weights['againts_team_assists'] * againts_team_assists[i] + weights['accurate_long_balls_per_game'] * accurate_long_balls_per_game[i] + weights['Big_chances_created_per_game'] * Big_chances_created_per_game[i] + weights['Block_shots_per_game'] * Block_shots_per_game[i] + weights['Passes_per_game'] * Passes_per_game[i] + weights['tackles_accuracy'] * tackles_accuracy[i] + weights['Crosses_accuracy'] * Crosses_accuracy[i] + weights['Clearence_per_game'] * Clearence_per_game[i] + weights['Interception_per_game'] * Interception_per_game[i] - weights['Fouls_per_game'] * Fouls_per_game[i] + weights['Duels_won_per_game'] * Duels_won_per_game[i] + weights['Aerial_won_per_game'] * Aerial_won_per_game[i] +weights['seasonal_goals'] * (seasonal_goals[i] / seasonal_apperence[i])+weights['seasonal_assists'] * (seasonal_assists[i] / seasonal_apperence[i])-weights['seasonal_Yellow'] * seasonal_Yellow[i]-weights['seasonal_Red'] * seasonal_Red[i]- weights['seasonal_Second_Yellow'] * seasonal_Second_Yellow[i]+weights['recent_Goals'] * recent_Goals[i]+weights['recent_Assists'] * recent_Assists[i]+weights['recent_Shots'] * recent_Shots[i]+weights['recent_ShotOnTarget'] * recent_ShotOnTarget[i]-weights['recent_Fouls'] * recent_Fouls[i]-weights['recent_Yellow_card'] * recent_Yellow_card[i]-weights['recent_Red_card'] * recent_Red_card[i]-weights['recent_Offside'] * recent_Offside[i]+ weights['recent_Clearances'] * recent_Clearances[i]+ weights['recent_Pass_accuracy'] * recent_Pass_accuracy[i]+ weights['recent_Key_passes'] * recent_Key_passes[i]
    sheet.append(('Attacking Midfield', best_attacking_midfielder_name,1,per,Jersey_num[i]))
    
elif team_strength=='Good teams':
    if count_2 >6:
        i=second_best_attacking_midfielder_idx
        per=weights['Market_value'] * Market_value[i]+weights['position_list'] * position_list[i]+ weights['goals'] * (goals[i] / apperence[i]) + weights['assists'] * (assists[i] / apperence[i]) + weights['againts_team_goals'] * againts_team_goals[i] + weights['againts_team_assists'] * againts_team_assists[i] + weights['accurate_long_balls_per_game'] * accurate_long_balls_per_game[i] + weights['Big_chances_created_per_game'] * Big_chances_created_per_game[i] + weights['Block_shots_per_game'] * Block_shots_per_game[i] + weights['Passes_per_game'] * Passes_per_game[i] + weights['tackles_accuracy'] * tackles_accuracy[i] + weights['Crosses_accuracy'] * Crosses_accuracy[i] + weights['Clearence_per_game'] * Clearence_per_game[i] + weights['Interception_per_game'] * Interception_per_game[i] - weights['Fouls_per_game'] * Fouls_per_game[i] + weights['Duels_won_per_game'] * Duels_won_per_game[i] + weights['Aerial_won_per_game'] * Aerial_won_per_game[i] +weights['seasonal_goals'] * (seasonal_goals[i] / seasonal_apperence[i])+weights['seasonal_assists'] * (seasonal_assists[i] / seasonal_apperence[i])-weights['seasonal_Yellow'] * seasonal_Yellow[i]-weights['seasonal_Red'] * seasonal_Red[i]- weights['seasonal_Second_Yellow'] * seasonal_Second_Yellow[i]+weights['recent_Goals'] * recent_Goals[i]+weights['recent_Assists'] * recent_Assists[i]+weights['recent_Shots'] * recent_Shots[i]+weights['recent_ShotOnTarget'] * recent_ShotOnTarget[i]-weights['recent_Fouls'] * recent_Fouls[i]-weights['recent_Yellow_card'] * recent_Yellow_card[i]-weights['recent_Red_card'] * recent_Red_card[i]-weights['recent_Offside'] * recent_Offside[i]+ weights['recent_Clearances'] * recent_Clearances[i]+ weights['recent_Pass_accuracy'] * recent_Pass_accuracy[i]+ weights['recent_Key_passes'] * recent_Key_passes[i]
        sheet.append(('Attacking Midfield', second_best_attacking_midfielder_name,2,per,Jersey_num[i]))
       
        
    else:
        i=best_attacking_midfielder_idx
        per=weights['Market_value'] * Market_value[i]+weights['position_list'] * position_list[i]+ weights['goals'] * (goals[i] / apperence[i]) + weights['assists'] * (assists[i] / apperence[i]) + weights['againts_team_goals'] * againts_team_goals[i] + weights['againts_team_assists'] * againts_team_assists[i] + weights['accurate_long_balls_per_game'] * accurate_long_balls_per_game[i] + weights['Big_chances_created_per_game'] * Big_chances_created_per_game[i] + weights['Block_shots_per_game'] * Block_shots_per_game[i] + weights['Passes_per_game'] * Passes_per_game[i] + weights['tackles_accuracy'] * tackles_accuracy[i] + weights['Crosses_accuracy'] * Crosses_accuracy[i] + weights['Clearence_per_game'] * Clearence_per_game[i] + weights['Interception_per_game'] * Interception_per_game[i] - weights['Fouls_per_game'] * Fouls_per_game[i] + weights['Duels_won_per_game'] * Duels_won_per_game[i] + weights['Aerial_won_per_game'] * Aerial_won_per_game[i] +weights['seasonal_goals'] * (seasonal_goals[i] / seasonal_apperence[i])+weights['seasonal_assists'] * (seasonal_assists[i] / seasonal_apperence[i])-weights['seasonal_Yellow'] * seasonal_Yellow[i]-weights['seasonal_Red'] * seasonal_Red[i]- weights['seasonal_Second_Yellow'] * seasonal_Second_Yellow[i]+weights['recent_Goals'] * recent_Goals[i]+weights['recent_Assists'] * recent_Assists[i]+weights['recent_Shots'] * recent_Shots[i]+weights['recent_ShotOnTarget'] * recent_ShotOnTarget[i]-weights['recent_Fouls'] * recent_Fouls[i]-weights['recent_Yellow_card'] * recent_Yellow_card[i]-weights['recent_Red_card'] * recent_Red_card[i]-weights['recent_Offside'] * recent_Offside[i]+ weights['recent_Clearances'] * recent_Clearances[i]+ weights['recent_Pass_accuracy'] * recent_Pass_accuracy[i]+ weights['recent_Key_passes'] * recent_Key_passes[i] 
        sheet.append(('Attacking Midfield', best_attacking_midfielder_name,1,per,Jersey_num[i]))
    
elif team_strength=='Middle teams':
    if count_2 >5:
        i=second_best_attacking_midfielder_idx
        per=weights['Market_value'] * Market_value[i]+weights['position_list'] * position_list[i]+ weights['goals'] * (goals[i] / apperence[i]) + weights['assists'] * (assists[i] / apperence[i]) + weights['againts_team_goals'] * againts_team_goals[i] + weights['againts_team_assists'] * againts_team_assists[i] + weights['accurate_long_balls_per_game'] * accurate_long_balls_per_game[i] + weights['Big_chances_created_per_game'] * Big_chances_created_per_game[i] + weights['Block_shots_per_game'] * Block_shots_per_game[i] + weights['Passes_per_game'] * Passes_per_game[i] + weights['tackles_accuracy'] * tackles_accuracy[i] + weights['Crosses_accuracy'] * Crosses_accuracy[i] + weights['Clearence_per_game'] * Clearence_per_game[i] + weights['Interception_per_game'] * Interception_per_game[i] - weights['Fouls_per_game'] * Fouls_per_game[i] + weights['Duels_won_per_game'] * Duels_won_per_game[i] + weights['Aerial_won_per_game'] * Aerial_won_per_game[i] +weights['seasonal_goals'] * (seasonal_goals[i] / seasonal_apperence[i])+weights['seasonal_assists'] * (seasonal_assists[i] / seasonal_apperence[i])-weights['seasonal_Yellow'] * seasonal_Yellow[i]-weights['seasonal_Red'] * seasonal_Red[i]- weights['seasonal_Second_Yellow'] * seasonal_Second_Yellow[i]+weights['recent_Goals'] * recent_Goals[i]+weights['recent_Assists'] * recent_Assists[i]+weights['recent_Shots'] * recent_Shots[i]+weights['recent_ShotOnTarget'] * recent_ShotOnTarget[i]-weights['recent_Fouls'] * recent_Fouls[i]-weights['recent_Yellow_card'] * recent_Yellow_card[i]-weights['recent_Red_card'] * recent_Red_card[i]-weights['recent_Offside'] * recent_Offside[i]+ weights['recent_Clearances'] * recent_Clearances[i]+ weights['recent_Pass_accuracy'] * recent_Pass_accuracy[i]+ weights['recent_Key_passes'] * recent_Key_passes[i] 
        sheet.append(('Attacking Midfield', second_best_attacking_midfielder_name,2,per,Jersey_num[i]))
        
    else:
        i=best_attacking_midfielder_idx
        per=weights['Market_value'] * Market_value[i]+weights['position_list'] * position_list[i]+ weights['goals'] * (goals[i] / apperence[i]) + weights['assists'] * (assists[i] / apperence[i]) + weights['againts_team_goals'] * againts_team_goals[i] + weights['againts_team_assists'] * againts_team_assists[i] + weights['accurate_long_balls_per_game'] * accurate_long_balls_per_game[i] + weights['Big_chances_created_per_game'] * Big_chances_created_per_game[i] + weights['Block_shots_per_game'] * Block_shots_per_game[i] + weights['Passes_per_game'] * Passes_per_game[i] + weights['tackles_accuracy'] * tackles_accuracy[i] + weights['Crosses_accuracy'] * Crosses_accuracy[i] + weights['Clearence_per_game'] * Clearence_per_game[i] + weights['Interception_per_game'] * Interception_per_game[i] - weights['Fouls_per_game'] * Fouls_per_game[i] + weights['Duels_won_per_game'] * Duels_won_per_game[i] + weights['Aerial_won_per_game'] * Aerial_won_per_game[i] +weights['seasonal_goals'] * (seasonal_goals[i] / seasonal_apperence[i])+weights['seasonal_assists'] * (seasonal_assists[i] / seasonal_apperence[i])-weights['seasonal_Yellow'] * seasonal_Yellow[i]-weights['seasonal_Red'] * seasonal_Red[i]- weights['seasonal_Second_Yellow'] * seasonal_Second_Yellow[i]+weights['recent_Goals'] * recent_Goals[i]+weights['recent_Assists'] * recent_Assists[i]+weights['recent_Shots'] * recent_Shots[i]+weights['recent_ShotOnTarget'] * recent_ShotOnTarget[i]-weights['recent_Fouls'] * recent_Fouls[i]-weights['recent_Yellow_card'] * recent_Yellow_card[i]-weights['recent_Red_card'] * recent_Red_card[i]-weights['recent_Offside'] * recent_Offside[i]+ weights['recent_Clearances'] * recent_Clearances[i]+ weights['recent_Pass_accuracy'] * recent_Pass_accuracy[i]+ weights['recent_Key_passes'] * recent_Key_passes[i]
        sheet.append(('Attacking Midfield', best_attacking_midfielder_name,1,per,Jersey_num[i]))
    
elif team_strength=='Poor teams':
    if count_2 >4:
        i=second_best_attacking_midfielder_idx
        per=weights['Market_value'] * Market_value[i]+weights['position_list'] * position_list[i]+ weights['goals'] * (goals[i] / apperence[i]) + weights['assists'] * (assists[i] / apperence[i]) + weights['againts_team_goals'] * againts_team_goals[i] + weights['againts_team_assists'] * againts_team_assists[i] + weights['accurate_long_balls_per_game'] * accurate_long_balls_per_game[i] + weights['Big_chances_created_per_game'] * Big_chances_created_per_game[i] + weights['Block_shots_per_game'] * Block_shots_per_game[i] + weights['Passes_per_game'] * Passes_per_game[i] + weights['tackles_accuracy'] * tackles_accuracy[i] + weights['Crosses_accuracy'] * Crosses_accuracy[i] + weights['Clearence_per_game'] * Clearence_per_game[i] + weights['Interception_per_game'] * Interception_per_game[i] - weights['Fouls_per_game'] * Fouls_per_game[i] + weights['Duels_won_per_game'] * Duels_won_per_game[i] + weights['Aerial_won_per_game'] * Aerial_won_per_game[i] +weights['seasonal_goals'] * (seasonal_goals[i] / seasonal_apperence[i])+weights['seasonal_assists'] * (seasonal_assists[i] / seasonal_apperence[i])-weights['seasonal_Yellow'] * seasonal_Yellow[i]-weights['seasonal_Red'] * seasonal_Red[i]- weights['seasonal_Second_Yellow'] * seasonal_Second_Yellow[i]+weights['recent_Goals'] * recent_Goals[i]+weights['recent_Assists'] * recent_Assists[i]+weights['recent_Shots'] * recent_Shots[i]+weights['recent_ShotOnTarget'] * recent_ShotOnTarget[i]-weights['recent_Fouls'] * recent_Fouls[i]-weights['recent_Yellow_card'] * recent_Yellow_card[i]-weights['recent_Red_card'] * recent_Red_card[i]-weights['recent_Offside'] * recent_Offside[i]+ weights['recent_Clearances'] * recent_Clearances[i]+ weights['recent_Pass_accuracy'] * recent_Pass_accuracy[i]+ weights['recent_Key_passes'] * recent_Key_passes[i]
        sheet.append(('Attacking Midfield', second_best_attacking_midfielder_name,2,per,Jersey_num[i]))
    else:
        i=best_attacking_midfielder_idx
        per=weights['Market_value'] * Market_value[i]+weights['position_list'] * position_list[i]+ weights['goals'] * (goals[i] / apperence[i]) + weights['assists'] * (assists[i] / apperence[i]) + weights['againts_team_goals'] * againts_team_goals[i] + weights['againts_team_assists'] * againts_team_assists[i] + weights['accurate_long_balls_per_game'] * accurate_long_balls_per_game[i] + weights['Big_chances_created_per_game'] * Big_chances_created_per_game[i] + weights['Block_shots_per_game'] * Block_shots_per_game[i] + weights['Passes_per_game'] * Passes_per_game[i] + weights['tackles_accuracy'] * tackles_accuracy[i] + weights['Crosses_accuracy'] * Crosses_accuracy[i] + weights['Clearence_per_game'] * Clearence_per_game[i] + weights['Interception_per_game'] * Interception_per_game[i] - weights['Fouls_per_game'] * Fouls_per_game[i] + weights['Duels_won_per_game'] * Duels_won_per_game[i] + weights['Aerial_won_per_game'] * Aerial_won_per_game[i] +weights['seasonal_goals'] * (seasonal_goals[i] / seasonal_apperence[i])+weights['seasonal_assists'] * (seasonal_assists[i] / seasonal_apperence[i])-weights['seasonal_Yellow'] * seasonal_Yellow[i]-weights['seasonal_Red'] * seasonal_Red[i]- weights['seasonal_Second_Yellow'] * seasonal_Second_Yellow[i]+weights['recent_Goals'] * recent_Goals[i]+weights['recent_Assists'] * recent_Assists[i]+weights['recent_Shots'] * recent_Shots[i]+weights['recent_ShotOnTarget'] * recent_ShotOnTarget[i]-weights['recent_Fouls'] * recent_Fouls[i]-weights['recent_Yellow_card'] * recent_Yellow_card[i]-weights['recent_Red_card'] * recent_Red_card[i]-weights['recent_Offside'] * recent_Offside[i]+ weights['recent_Clearances'] * recent_Clearances[i]+ weights['recent_Pass_accuracy'] * recent_Pass_accuracy[i]+ weights['recent_Key_passes'] * recent_Key_passes[i]
        sheet.append(('Attacking Midfield', best_attacking_midfielder_name,1,per,Jersey_num[i]))
    
else:
    print("please check agints team name")
        
wb.save('C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/players.xlsx')    

