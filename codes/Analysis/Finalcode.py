import os
#command = 'spyder-kernels --restart'
#os.system(command)


import random
import pandas as pd
import os



# Provide the path to your Excel file and specify the sheet name
file_path = 'C:/Users/Admin/Documents/research final - chelsea/Research/Strength and weakness/Strength and weakness.xlsx'
sheet_name = "Arsenal"

# Read the Excel file with the specified sheet name
df= pd.read_excel(file_path, sheet_name=sheet_name)

tasks_strengths = df[(df['Strength/Weakness'] == 'Very Strong') | (df['Strength/Weakness'] == 'Strong')]

opposing_team_strengths = {task: 1 for task in tasks_strengths['KPIs']}

tasks_weaknesses = df[(df['Strength/Weakness'] == 'Very Weak') | (df['Strength/Weakness'] == 'Weak')]

opposing_team_weaknesses = {task: 1 for task in tasks_weaknesses['KPIs']}


formation_scores = {
    '4-4-2': {
        'strengths': ['Stopping opponents from creating chances','Creating chances using through balls','Attacking down the wings','Aerial duels','Counter attacks','Defending counter attacks','Defending against attacks down the wings'],
        'weaknesses': ['creating chances through individual skill','Attacking down the wings','Aerial duels','Counter attacks'],
        'score': 0
    },
    '4-4-1-1': {
        'strengths': ['Counter attacks', 'Finishing scoring chances','Attacking down the wings','Attacking set pieces'],
        'weaknesses': ['Creating scoring chances','Coming back from losing positions'],
        'score': 0
    },
    '4-3-3': {
        'strengths': ['Avoiding individual errors', 'Protecting the lead','Avoiding fouling in dangerous areas','Stealing the ball from the opposition'],
        'weaknesses': ['Shooting from direct free kicks','Avoiding offside','Coming back from losing positions','Defending against long shots'],
        'score': 0
    },
    '4-5-1': {
        'strengths': ['Attacking set pieces', 'Creating scoring chances','Creating chances through individual skill','Finishing scoring chances','Aerial duels','Shooting from direct free kicks'],
        'weaknesses': ['Finishing scoring chances','Creating long shot opportunities'],
        'score': 0
    },
    '3-5-2': {
        'strengths': ['Creating chances through individual skill', 'Attacking down the wings','Avoiding offside','Defending against skillful players','Defending counter attacks','Defending against long shots'],
        'weaknesses': ['Protecting the lead','Defending set pieces','Avoiding fouling in dangerous areas'],
        'score': 0
    },
    '4-2-3-1': {
        'strengths': ['Stopping opponents from creating chances', 'Avoiding individual errors','Protecting the lead','Creating chances using through balls','Defending against through ball attacks','Stealing the ball from the opposition','Defending set pieces'],
        'weaknesses': ['Defending against through ball attacks','Stealing the ball from the opposition','Defending against skillful players','Defending counter attacks','Defending against attacks down the wings','Keeping possession of the ball'],
        'score': 0
    },
    '3-4-3': {
        'strengths': ['Creating chances through individual skill', 'Coming back from losing positions','Keeping possession of the ball'],
        'weaknesses': ['Defending against attacks down the wings'],
        'score': 0
    },
    '4-1-4-1': {
        'strengths': ['Attacking set pieces', 'Creating scoring chances','Finishing scoring chances','Avoiding fouling in dangerous areas','Shooting from direct free kicks','Defending against through ball attacks','Creating long shot opportunities'],
        'weaknesses': ['Creating scoring chances','Creating chances using through balls'],
        'score': 0
    },
    # Add more formations and their corresponding strengths and weaknesses
}

# Calculate formation scores based on opposing team's weaknesses and strengths
for formation, details in formation_scores.items():
    for weakness in details['weaknesses']:
        if weakness in opposing_team_weaknesses:
            formation_scores[formation]['score'] += opposing_team_weaknesses[weakness]
    for strength in details['strengths']:
        if strength in opposing_team_strengths:
            formation_scores[formation]['score'] += opposing_team_strengths[strength]

# Select the formation with the highest score
best_formation = max(formation_scores, key=lambda x: formation_scores[x]['score'])

print(f"The best formation against the opposing team is: {best_formation}")


file_path_1 = 'best-formation.txt'


with open(file_path_1, 'w') as file:
    pass 

with open(file_path_1, 'a') as file:
    file.write(best_formation)



python_file_paths=[]

if best_formation=='4-4-2':
    urls_to_append = [
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Goalkeeper.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Left Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Right Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Center Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Center Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Centrel Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Centrel Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Left Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Rigth Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Left Winger.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Rigth Winger.py"
      ]
    
    python_file_paths.extend(urls_to_append)
    
elif best_formation=='4-4-1-1':
    urls_to_append = [
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Goalkeeper.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Left Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Right Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Center Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Center Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Centrel Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Centrel Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Left Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Rigth Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Second Striker.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Center Forward.py"
      ]
    
    python_file_paths.extend(urls_to_append)
    
elif best_formation=='4-3-3':
    urls_to_append = [
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Goalkeeper.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Left Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Right Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Center Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Center Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Centrel Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Left Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Rigth Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Center Forward.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Left Winger.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Rigth Winger.py"
      ]
    
    python_file_paths.extend(urls_to_append)
    
elif best_formation=='4-5-1':
    urls_to_append = [
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Goalkeeper.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Left Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Right Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Center Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Center Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Centrel Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Left Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Rigth Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Defensive Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Attacking Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Center Forward.py"
      ]
    
    python_file_paths.extend(urls_to_append)
    
elif best_formation=='3-5-2':
    urls_to_append = [
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Goalkeeper.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Left Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Right Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Center Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Centrel Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Left Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Rigth Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Defensive Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Attacking Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Left Winger.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Rigth Winger.py"
      ]
    
    python_file_paths.extend(urls_to_append)
    
elif best_formation=='4-2-3-1':
    urls_to_append = [
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Goalkeeper.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Left Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Right Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Center Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Center Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Defensive Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Left Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Rigth Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Defensive Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Attacking Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Center Forward.py"
      ]
    
    python_file_paths.extend(urls_to_append)
    
elif best_formation=='3-4-3':
    urls_to_append = [
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Goalkeeper.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Left Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Right Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Center Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Left Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Rigth Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Centrel Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Centrel Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Center Forward.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Left Winger.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Rigth Winger.py"
      ]
    
    python_file_paths.extend(urls_to_append)
    
elif best_formation=='4-1-4-1':
    urls_to_append = [
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Goalkeeper.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Left Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Right Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Center Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Center Back.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Defensive Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Left Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Rigth Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Centrel Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Centrel Midfielder.py",
    "C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/Center Forward.py",
      ]
    
    python_file_paths.extend(urls_to_append)
Total_Performance_list=[]
list1=[]

df6 = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/players.xlsx')
df6 = df6.head(0)
df6.to_excel('C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/players.xlsx', index=False)


for i in range(1,50):
    df = pd.DataFrame(columns=['Position', 'Player', 'ranking','per',"Jersey num"])
    # Create a new Excel file for each round
    df.to_excel('players.xlsx', index=False)
    
    random.shuffle(python_file_paths)
    
    print(python_file_paths)
    
    list1.append(python_file_paths)
            
    for python_file_path in python_file_paths:
        with open(python_file_path, 'r') as file:
            python_code = file.read()
            exec(python_code)


    
            
    df6 = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/players.xlsx')
    df6['per'] = pd.to_numeric(df6['per'], errors='coerce')
    total_sum = df6['per'].sum()
    Total_Performance_list.append(total_sum)

    # Keep only the first row
    df6 = df6.head(0)

    # Save the DataFrame to an Excel file, excluding the index
    df6.to_excel('C:/Users/Admin/Documents/research final - chelsea/Research/Implementation/final/players.xlsx', index=False)



best_path=Total_Performance_list.index(max(Total_Performance_list))
python_file_paths=list1[best_path]

df = pd.DataFrame(columns=['Position', 'Player', 'ranking','per',"Jersey num"])
    # Create a new Excel file for each round
df.to_excel('players.xlsx', index=False)
    
     
for python_file_path in python_file_paths:
    with open(python_file_path, 'r') as file:
        python_code = file.read()
        exec(python_code)


            
    
    
    
    

    
