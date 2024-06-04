import os
import pandas as pd

# Path to the folder containing the Excel files
folder_path = r'C:\Users\Admin\Documents\research final - chelsea\Research\last 5 games'

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Filter the list to include only Excel files
excel_files = [file for file in files if file.endswith('.xlsx') and file != 'last 5 games.xlsx'and file != '~$Wesley Fofana.xlsx']

# Create an empty dictionary to store the mean values for each Excel file
mean_values_dict = {}

# Iterate over each Excel file
for file in excel_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_excel(file_path)

    # Convert columns to numerical, excluding columns with names 'date' and 'time'
    for column in df.columns:
        if column.lower() != 'date' and column.lower() != 'time':
            try:
                df[column] = pd.to_numeric(df[column], errors='coerce')
            except ValueError:
                pass  # Ignore columns that cannot be converted to numeric

    # Calculate the mean of columns, excluding 'date' and 'time'
    numeric_cols = [col for col in df.columns if col.lower() != 'date' and col.lower() != 'time']
    mean_values = df[numeric_cols].mean()

    # Remove the ".xlsx" extension from the file name
    file_name = os.path.splitext(file)[0]

    # Store the mean values in the dictionary with the Excel file name as the key
    mean_values_dict[file_name] = mean_values.to_dict()

# Initialize data dictionary
data = {
    'Player': [],
    'played minutes': [],
    'Goals': [],
    'Assists': [],
    'Shots': [],
    'Shot on targets': [],
    'Tackles': [],
    'Clearances': [],
    'Fouls': [],
    'Yellow card': [],
    'Red card': [],
    'Pass accuracy': [],
    'Offside': [],
    'Goal conceded':[],
    'Saves': [],
    'Clean sheet':[],
    'Long passes':[],
    'Key passes':[]
}

# Iterate over mean_values_dict and update the data dictionary
for key in mean_values_dict.keys():
    nested_dict = mean_values_dict[key]
    data['Player'].append(key)
    data['played minutes'].append(nested_dict.get('played minutes', 0))
    data['Goals'].append(nested_dict.get('Goals', 0))
    data['Assists'].append(nested_dict.get('Assists', 0))
    data['Shots'].append(nested_dict.get('Shots', 0))
    data['Shot on targets'].append(nested_dict.get('Shot on targets', 0))
    data['Tackles'].append(nested_dict.get('Tackles', 0))
    data['Clearances'].append(nested_dict.get('Clearances', 0))
    data['Fouls'].append(nested_dict.get('Fouls', 0))
    data['Yellow card'].append(nested_dict.get('Yellow card', 0))
    data['Red card'].append(nested_dict.get('Red card', 0))
    data['Pass accuracy'].append(nested_dict.get('Pass accuracy', 0))
    data['Offside'].append(nested_dict.get('Offside', 0))
    data['Goal conceded'].append(nested_dict.get('Goal conceded', 0))
    data['Saves'].append(nested_dict.get('Saves', 0))
    data['Clean sheet'].append(nested_dict.get('Clean sheet', 0))
    data['Long passes'].append(nested_dict.get('Long passes', 0))
    data['Key passes'].append(nested_dict.get('Key passes', 0))

# Create a DataFrame from the updated data
df = pd.DataFrame(data)

df['Player'] = df['Player'].replace('Mykhailo Mudryk', 'Mykhaylo Mudryk').replace('Đorđe Petrović', 'Djordje Petrovic').replace('Romeo Lavia', 'Roméo Lavia')

if 'Malang Sarr' not in df['Player'].values:
    # Create a dictionary with 'Player' as 'Malang Sarr' and all other columns as 0
    new_player_data = {
        'Player': 'Malang Sarr',
        'played minutes': 0,
        'Goals': 0,
        'Assists': 0,
        'Shots': 0,
        'Shot on targets': 0,
        'Tackles': 0,
        'Clearances': 0,
        'Fouls': 0,
        'Yellow card': 0,
        'Red card': 0,
        'Pass accuracy': 0,
        'Offside': 0,
        'Goal conceded':0,
        'Saves':0,
        'Clean sheet':0,
        'Long passes':0,
        'Key passes':0
    }
    # Append the new player data to the DataFrame
    df = df.append(new_player_data, ignore_index=True)
    
if 'Diego Moreira' not in df['Player'].values:
    # Create a dictionary with 'Player' as 'Malang Sarr' and all other columns as 0
    new_player_data = {
        'Player': 'Diego Moreira',
        'played minutes': 0,
        'Goals': 0,
        'Assists': 0,
        'Shots': 0,
        'Shot on targets': 0,
        'Tackles': 0,
        'Clearances': 0,
        'Fouls': 0,
        'Yellow card': 0,
        'Red card': 0,
        'Pass accuracy': 0,
        'Offside': 0,
        'Goal conceded':0,
        'Saves':0,
        'Clean sheet':0,
        'Long passes':0,
        'Key passes':0
        
    }
    # Append the new player data to the DataFrame
    df = df.append(new_player_data, ignore_index=True)
# Path to save the Excel file
file_path = 'C:/Users/Admin/Documents/research final - chelsea/Research/last 5 games/last 5 games.xlsx'

# Save the DataFrame to an Excel file
df.to_excel(file_path, index=False)

print(f"Excel file '{file_path}' created successfully.")

