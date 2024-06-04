#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd

# Path to your Excel file
file_path = 'C:/Users/Admin/Documents/research final - chelsea/Research/Rating/football_data.xlsx'

# Read all sheets into a dictionary of dataframes
xls = pd.ExcelFile(file_path)
data_frames = {}

for sheet_name in xls.sheet_names:
    # Read each sheet into a DataFrame
    df = xls.parse(sheet_name)
    
    # Convert the "league position" column to integer
    if 'league position' in df.columns:
        df['league position'] = df['league position'].astype(int)
        
    data_frames[sheet_name] = df  

# Initialize dictionary to store total sums
total_sums = {}

# Calculate total sum for each sheet
for sheet_name, df in data_frames.items():
    premier_league_df = df.loc[df['Tier'] == 'Premier League']
    championship_df = df.loc[df['Tier'] == 'Championship']
    League_One_df = df.loc[df['Tier'] == 'League One']
    lower_df = df[df['Tier'].isin(['League Two', 'Conference Premier'])]

    premier_league_df['marks'] = 21 - premier_league_df['league position']
    championship_df['marks'] = ((25 - championship_df['league position']) * 0.416666667)
    League_One_df['marks'] = ((25 - League_One_df['league position']) * 0.2083333)
    lower_df['marks'] = ((25 - lower_df['league position']) *0.104)

    premier_league_df['marks'] = premier_league_df['marks'].astype(float)
    championship_df['marks'] = championship_df['marks'].astype(float)
    League_One_df['marks'] = League_One_df['marks'].astype(float)
    lower_df['marks'] = lower_df['marks'].astype(float)

    total_sum_premier = premier_league_df['marks'].sum() + championship_df['marks'].sum() + League_One_df['marks'].sum() + lower_df['marks'].sum()
    total_sums[sheet_name] = total_sum_premier

# Convert dictionary to DataFrame
totals_df = pd.DataFrame(list(total_sums.items()), columns=['Sheet Name', 'Total Sum'])

# Sort DataFrame by 'Total Sum' in descending order
totals_df = totals_df.sort_values(by='Total Sum', ascending=False)

big_six = totals_df.head(6)['Sheet Name'].tolist()
good_teams = totals_df.iloc[6:12]['Sheet Name'].tolist()
middle_teams = totals_df.iloc[12:17]['Sheet Name'].tolist()
poor_teams = totals_df.tail(3)['Sheet Name'].tolist()

import pandas as pd

# Create an empty DataFrame with columns "Position" and "Player"
df = pd.DataFrame(columns=['Team', 'Team Strength'])

df['Team'] = big_six + good_teams+middle_teams+poor_teams

# Populate the 'Team Strength' column based on the team category
df['Team Strength'] = ['Big six']*len(big_six) + ['Good teams']*len(good_teams)+ ['Middle teams']*len(middle_teams)+ ['Poor teams']*len(poor_teams)

output_file_path = 'C:/Users/Admin/Documents/research final - chelsea/Research/Rating/team_strength.xlsx'

# Save the DataFrame to an Excel file
df.to_excel(output_file_path, index=False)


# In[6]:





# In[ ]:




