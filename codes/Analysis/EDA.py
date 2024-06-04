#!/usr/bin/env python
# coding: utf-8

# In[132]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/player data/player_data.xlsx')
df1 = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/player_current/playerseasondata2-21.xlsx')
df2 = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/player_current/playerseasondata2-22.xlsx')
df3 = pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/player_current/playerseasondata2-23.xlsx')
df4 =pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/perfomance/Forward/forward players data.xlsx')
df6 =pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/perfomance/Goal keeper/Goalkeeper_data.xlsx')
df7 =pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/perfomance/Defenders/defender players data.xlsx')
df8 =pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/perfomance/Mid fielder/midfield players data.xlsx')


# In[121]:


def categorize_position(position):
    if position == 'Goalkeeper':
        return 'Goalkeeper'
    elif position in ['Left-Back', 'Centre-Back', 'Right-Back']:
        return 'Defender'
    elif position in ['Central Midfield', 'Attacking Midfield', 'Defensive Midfield', 'Left Midfield', 'Right Midfield']:
        return 'Midfielder'
    elif position in ['Centre-Forward', 'Left Winger', 'Right Winger', 'Second Striker']:
        return 'Forward'
    else:
        return 'Other'

# Assuming df is your DataFrame containing the football player data
df['Main Position'] = df['Position'].apply(categorize_position)

position_counts = df["Main Position"].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(position_counts, labels=[f'{index} ({value}, {100*value/position_counts.sum():.1f}%)' for index, value in position_counts.items()], startangle=140)

plt.axis('equal')
plt.title('Player Position Distribution')
plt.show()


# In[122]:


mask = df['Market value'].str.contains('k')
df.loc[mask, 'Market value'] = '0.' + df.loc[mask, 'Market value'].str.replace('k', '')
df['Market value']=df['Market value'].str.replace('m', '')
df['Market value'] = df['Market value'].replace('-', '0')
df['Market value'] = pd.to_numeric(df['Market value'])

Goalkeepers_avg_market_value = df[df["Main Position"] == 'Goalkeeper']["Market value"].mean()
midfielders_avg_market_value = df[df["Main Position"] == 'Midfielder']["Market value"].mean()
Forwards_avg_market_value = df[df["Main Position"] == 'Forward']["Market value"].mean()
midfielders_avg_market_value = df[df["Main Position"] == 'Goalkeeper']["Market value"].mean()


# Data
positions = ['Goalkeeper', 'Defender', 'Midfielder', 'Forward']
avg_market_values = [df[df["Main Position"] == pos]["Market value"].mean() for pos in positions]

# Creating the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(positions, avg_market_values, color='skyblue')
plt.xlabel('Position')
plt.ylabel('Average Market Value')
plt.title('Average Market Value by Position')

# Adding value labels at the end of each bar with "m"
for bar, value in zip(bars, avg_market_values):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{round(value, 2)}m', 
             ha='center', va='bottom')
plt.savefig('Average_Market_Value_by_Position.png', facecolor='white')
plt.show()



# In[123]:


import matplotlib.pyplot as plt
df["Goals"] = pd.to_numeric(df["Goals"], errors='coerce')
df["Appearance"] = pd.to_numeric(df["Appearance"], errors='coerce')
df["Assists"] = pd.to_numeric(df["Assists"], errors='coerce')

# Create a figure and a grid of subplots
fig, axs = plt.subplots(3, 1, figsize=(12, 18))

# Plot for Goals
axs[0].bar(df["Player"], df["Goals"], color='skyblue')
axs[0].set_ylabel('Number of Goals')
axs[0].set_title('Number of Goals for Each Player')

# Plot for Appearances
axs[1].bar(df["Player"], df["Appearance"], color='green')
axs[1].set_ylabel('Number of Appearances')
axs[1].set_title('Number of Appearances for Each Player')

# Plot for Assists
axs[2].bar(df["Player"], df["Assists"], color='red')
axs[2].set_ylabel('Number of Assists')
axs[2].set_title('Number of Assists for Each Player')

# Rotate x-axis labels for better visibility
for ax in axs:
    ax.set_xticklabels(df["Player"], rotation=45, ha='right')

# Adjust layout
plt.tight_layout()
plt.savefig('Number_of_Assists_for_Each_Player.png', facecolor='white')
# Display the plots
plt.show()


# In[124]:


import matplotlib.pyplot as plt

df1["Played minutes"] = pd.to_numeric(df1["Played minutes"], errors='coerce')
df2["Played minutes"] = pd.to_numeric(df2["Played minutes"], errors='coerce')
df3["Played minutes"] = pd.to_numeric(df3["Played minutes"], errors='coerce')

# Assuming df1 is your DataFrame containing the football player data
plt.figure(figsize=(12, 6))
plt.plot(df1["Player"], df1["Played minutes"], linestyle='solid', color='red', label='20/21 season')
plt.plot(df2["Player"], df2["Played minutes"], linestyle='solid', color='blue', label='21/22 season')
plt.plot(df3["Player"], df3["Played minutes"], linestyle='solid', color='green',  label='22/23 season')

plt.xlabel('Player')
plt.ylabel('Played Minutes')
plt.title('Played Minutes for Each Player')

plt.xticks(rotation=90, ha='right')
plt.legend()
plt.tight_layout()

plt.savefig('Played_Minutes_for_Each_Player.png', facecolor='white')

plt.show()


# In[125]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Assuming df1, df2, and df3 are your DataFrames containing the football player data
# Convert non-numeric values to NaN and then convert the column to numeric
for df in [df1, df2, df3]:
    df["Goals"] = pd.to_numeric(df["Goals"], errors='coerce')

plt.figure(figsize=(12, 6))

# Number of seasons and players
num_seasons = 3
num_players = len(df1)

# Bar width for each season
bar_width = 0.3

# Create bars for each season
for i, df in enumerate([df1, df2, df3]):
    x = np.arange(num_players) + (i - (num_seasons - 1) / 2) * bar_width
    plt.bar(x, df["Goals"], width=bar_width, label=f'Season {i+20}/{i+21}')

plt.xlabel('Player')
plt.ylabel('Goals')
plt.title('Goals for Each Player')

plt.xticks(np.arange(num_players), df1["Player"],rotation=90 )
plt.legend()
plt.tight_layout()
plt.savefig('Goals_for_Each_Player.png', facecolor='white')

plt.show()


# In[139]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'C:/Users/Admin/Documents/research final - chelsea/Research/Strength and weakness/Strength and weakness.xlsx'
xls = pd.ExcelFile(file_path)

# Initialize a dictionary to hold the value counts for each sheet
value_counts_dict = {}

# Iterate through all sheet names and aggregate value counts of "Strength/Weakness" column
for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name)
    
    # Count value counts of "Strength/Weakness" column
    if "Strength/Weakness" in df.columns:
        value_counts = df["Strength/Weakness"].value_counts()
        value_counts_dict[sheet_name] = value_counts
    else:
        print(f"'Strength/Weakness' column not found in sheet '{sheet_name}'")

# Combine all value counts into a single DataFrame
all_value_counts_df = pd.DataFrame(value_counts_dict).fillna(0)

# Transpose the DataFrame for plotting
all_value_counts_df = all_value_counts_df.transpose()

# Define a color map for the categories
color_map = {
    "Very Weak": "red",
    "Weak": "lightcoral",
    "Strong": "lightgreen",
    "Very Strong": "green"
}

# Generate colors for the columns based on the color map
colors = [color_map.get(category, 'gray') for category in all_value_counts_df.columns]

# Plot a stacked bar chart
ax = all_value_counts_df.plot(kind='bar', stacked=True, figsize=(10, 6), color=colors)

# Set plot title and labels
plt.title('Strength/Weakness Distribution Across all premier league clubs')
plt.xlabel('Sheets')
plt.ylabel('Count')
plt.xticks(rotation=90)

# Display the legend
plt.legend(title='Strength/Weakness')

# Show the plot
plt.tight_layout()
plt.savefig('Distribution_Across_all_premier_league_clubs.png', facecolor='white')
plt.show()


# In[127]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'C:/Users/Admin/Documents/research final - chelsea/Research/Rating/football_data.xlsx'
teams = ['Chelsea', 'Arsenal', 'Manchester City', 'Liverpool', 'Tottenham Hotspur', 'Manchester United']
colors = ['blue', 'red', 'green', 'purple', 'orange', 'brown']

plt.figure(figsize=(12, 8))

for team, color in zip(teams, colors):
    # Load the specific team's sheet
    df = pd.read_excel(file_path, sheet_name=team)

    # Assuming 'Season' and 'League Position' are the column names
    # Replace with the actual column names if they are different
    season_column = 'season'
    position_column = 'league position'

    # Create the line chart for the team
    plt.plot(df[season_column], df[position_column], marker='o', label=team, color=color)

# Add labels and title
plt.xlabel('Season')
plt.ylabel('League Position')
plt.title('Big six Teams League Position Over Seasons')

# Invert x-axis to show the most recent season first
plt.gca().invert_xaxis()

# Invert y-axis to have the top position at the top
plt.gca().invert_yaxis()

# Set y-axis ticks to display 1, 2, 3, ...
plt.gca().set_yticks(range(1, 15))

# Add legend
plt.legend()

# Show grid
plt.grid(True)
plt.savefig('Big_six_Teams_League_Position_Over_Seasons.png', facecolor='white')
# Show the plot
plt.show()


# In[140]:


df4['Shooting accuracy'] = df4['Shooting accuracy'].str.rstrip('%').astype('int')
plt.figure(figsize=(10, 4))
plt.plot(df4['Player'], df4['Shooting accuracy'], color='blue', linestyle='dotted', marker='o')
plt.xlabel('Player')
plt.ylabel('Shooting accuracy')
plt.title('Shooting Accuracy by Player')
plt.xticks(rotation=90)
plt.grid(True)
plt.savefig('Shooting_Accuracy_by_Player.png', facecolor='white')
plt.show()


# In[129]:


df4 = df4.replace('-', '0')
df4['Shots per game'] = df4['Shots per game'].astype(float)
df4['Shots on target per game'] = df4['Shots on target per game'].astype(float)
index = np.arange(len(df4['Player']))

plt.figure(figsize=(10, 6))
bar1 = plt.bar(index, df4['Shots per game'], bar_width, label='Shots per game', color='blue')
bar2 = plt.bar(index , df4['Shots on target per game'], bar_width, label='Shots on target per game', color='orange')

plt.xlabel('Player')
plt.ylabel('Values')
plt.title('Shots per Game and Shots on Target per Game by Player')
plt.xticks(index , df4['Player'], rotation=90)
plt.legend()
plt.savefig('Shots_on_Target_per_Game_by.png', facecolor='white')
plt.show()


# In[133]:



import numpy as np
df5 = df[df['Position'] == 'Goalkeeper']
df5['Appearance'] = df5['Appearance'].astype(int)
df5['Goal conceded'] = df5['Goal conceded'].astype(int)
df5['Clean sheet'] = df5['Clean sheet'].astype(int)
# Assuming df5 contains the relevant data
plt.figure(figsize=(12, 6))

bar_width = 0.25
index = np.arange(len(df5['Player']))

plt.bar(index, df5['Clean sheet'], bar_width, label='Clean sheet')
plt.bar(index + bar_width, df5['Goal conceded'], bar_width, label='Goal conceded')
plt.bar(index + 2 * bar_width, df5['Appearance'], bar_width, label='Appearance')

plt.xlabel('Player')
plt.ylabel('Count')
plt.title('Clean sheets, Goals conceded, and Appearances per Goalkeeprs')
plt.xticks(index + bar_width, df5['Player'], rotation=90)
plt.legend()

plt.tight_layout()
plt.savefig('Appearances_per_Goalkeeprsr.png', facecolor='white')
plt.show()


# In[134]:


plt.figure(figsize=(10, 6))
plt.bar(df6['Player'], df6['Total saves per game'], color='green')
plt.xlabel('Goalkeeper')
plt.ylabel('Total saves per game')
plt.title('Total Saves per Game by Goalkeeper')
plt.xticks(rotation=90)
plt.savefig('Total_Saves_per_Game_by_Goalkeeper.png', facecolor='white')
plt.show()


# In[135]:


df7.fillna(0, inplace=True)
columns_to_convert = ['Tackles per game', 'Recoveries per game', 'Interceptions per game', 'Total clearance per game']
df7[columns_to_convert] = df7[columns_to_convert].astype(float)

plt.figure(figsize=(20, 12))


columns_to_plot = ['Tackles per game', 'Recoveries per game', 'Interceptions per game', 'Total clearance per game']
players = df7['Player'] 

# Define line styles for each plot
line_styles = ['-', '--', ':', '-.']

# Plot each column separately with specified line styles
for column, style in zip(columns_to_plot, line_styles):
    plt.plot(players, df7[column], marker='o', linestyle=style, label=column)

plt.xticks(rotation=90, ha='right')  
plt.xlabel('Player')
plt.ylabel('value')
plt.title('Defensive Stats Per Game')
plt.legend(title='Stats')
plt.savefig('Defensive_Stats_Per_Game.png', facecolor='white')
plt.show()


# In[ ]:





# In[ ]:





# In[136]:


df8= df8.replace('-', '0')
df8.fillna(0, inplace=True)

columns_to_convert = ['Accurate long balls per game', 'Big chances created per game']
df8[columns_to_convert] = df8[columns_to_convert].astype(float)

# Plot the data
plt.figure(figsize=(10, 6))
#plt.plot(df8['Player'], df8['Accurate long balls per game'], label='Accurate long balls per game', marker='o')
plt.plot(df8['Player'], df8['Big chances created per game'], label='Big chances created per game', marker='x')
plt.xlabel('midfield player')
plt.ylabel('Values')
plt.title('Big chances created per game')
plt.xticks(rotation=90)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('Big_chances_created_per_game.png', facecolor='white')
plt.show()


# In[137]:


plt.figure(figsize=(10, 6))
plt.plot(df8['Player'], df8['Accurate long balls per game'], label='Accurate long balls per game', marker='o')
plt.xlabel('midfield player')
plt.ylabel('Values')
plt.title('Accurate long balls per game')
plt.xticks(rotation=90)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('Accurate_long_balls_per_game.png', facecolor='white')
plt.show()


# In[138]:


df


# In[ ]:




