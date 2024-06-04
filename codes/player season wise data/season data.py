#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df1= pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/player_current/playerseasondata2-22.xlsx')
df2= pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/player_current/playerseasondata2-23.xlsx')
df3= pd.read_excel('C:/Users/Admin/Documents/research final - chelsea/Research/player_current/playerseasondata2-21.xlsx')


# In[4]:


import pandas as pd

# Calculate mean 'Season_appernce' across df1, df2, and df3
season_apperence = pd.DataFrame({
    'Season appearance': pd.concat([df1['Season appearance'], df2['Season appearance'], df3['Season appearance']], axis=1).replace('-', '0').astype(int).mean(axis=1).round().astype(int)
})

# Calculate mean 'Goals' across df1, df2, and df3
Goals = pd.DataFrame({
    'Goals': pd.concat([df1['Goals'], df2['Goals'], df3['Goals']], axis=1).replace('-', '0').astype(int).mean(axis=1).round().astype(int)
})
Assist = pd.DataFrame({
    'Assists': pd.concat([df1['Assists'], df2['Assists']], axis=1).replace('-', '0').astype(int).mean(axis=1).round().astype(int)    
})
Goal_conceeded = pd.DataFrame({
    'Goal conceded': pd.concat([df1['Goal conceded'], df2['Goal conceded'], df3['Goal conceded']], axis=1).replace('-', '0').astype(int).mean(axis=1).round().astype(int)
})
Clean_Sheet = pd.DataFrame({
    'Clean sheet': pd.concat([df1['Clean sheet'], df2['Clean sheet'],df3['Clean sheet']], axis=1).replace('-', '0').astype(int).mean(axis=1).round().astype(int)
})
Yellow = pd.DataFrame({
    'Yellow cards': pd.concat([df1['Yellow cards'], df2['Yellow cards'],df3['Yellow cards']], axis=1).replace('-', '0').astype(int).mean(axis=1).round().astype(int)
})
Red = pd.DataFrame({
    'Red cards': pd.concat([df1['Red cards'], df2['Red cards'],df3['Red cards']], axis=1).replace('-', '0').astype(int).mean(axis=1).round().astype(int)
})
Second_Yellow = pd.DataFrame({
    'Second yellow cards': pd.concat([df1['Second yellow cards'], df2['Second yellow cards'],df3['Second yellow cards']], axis=1).replace('-', '0').astype(int).mean(axis=1).round().astype(int)
})
Played_minutes = pd.DataFrame({
    'Played_minutes': pd.concat([df1['Played minutes'], df2['Played minutes'],df3['Played minutes']], axis=1).replace('-', '0').astype(int).mean(axis=1).round().astype(int)
})



average_data= pd.DataFrame({
    'Player': df1['Player'],
    'Position': df1['Position'],
    'Season appearance': season_apperence['Season appearance'],
    'Goals': Goals['Goals'],
    'Assists': Assist['Assists'],
    'Goal conceded': Goal_conceeded['Goal conceded'],
    'Clean sheet': Clean_Sheet['Clean sheet'],
    'Yellow cards': Yellow['Yellow cards'],
    'Red cards': Red['Red cards'],
    'Second yellow cards': Second_Yellow['Second yellow cards'],
    'Played_minutes': Played_minutes['Played_minutes']
    
})

file_path = 'C:/Users/Admin/Documents/research final - chelsea/Research/player_current/seasonal_data.xlsx'

# Save the DataFrame to an Excel file
average_data.to_excel(file_path, index=False)


# In[ ]:




