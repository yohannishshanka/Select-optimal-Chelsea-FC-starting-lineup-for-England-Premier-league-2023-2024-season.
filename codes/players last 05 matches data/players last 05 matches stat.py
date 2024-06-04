import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup


chrome_driver_path = 'C:/Users/Admin/Documents/research final - chelsea/Research/chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "https://www.statmuse.com/fc/club/chelsea-34/stats/2024"
driver.get(url)


import time
time.sleep(5)

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find the second table and extract all href links
table = soup.find_all('table')[1]  # Assuming the second table is the one we want
links = table.find_all('a', href=True)

# Use a set to store unique URLs
unique_links = set()

# Add unique URLs to the set
for link in links:
    if "/matches?seasonYear" not in link['href']:
        unique_links.add("https://www.statmuse.com" + link['href'])

urls  = list(unique_links)

urls  = list(unique_links)
urls = [link for link in urls if link != 'https://www.statmuse.com/fc/player/ian-maatsen-2468']



    
# Close the browser
driver.quit()

def scrape_url(url):
    driver = webdriver.Chrome(executable_path=chrome_driver_path)

    # Load the webpage
    driver.get(url)
    
    time.sleep(5)

    # Get the HTML content of the page
    html = driver.page_source

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the element with the specified class
    element = soup.find(class_='whitespace-nowrap text-center md:text-left')

    if element:
        text = element.get_text(strip=True)
        if len(text) >= 2:
            first_two_letters = text[:2]
            if first_two_letters == "GK":
                # Find all tables on the page
                tables = soup.find_all('table')
                #print(len(tables))

                # Assuming the third table is the one we want, extract the specified columns
                if len(tables) >= 8:
                    desired_table = tables[2]  # Index 2 corresponds to the third table
                    data = []
                    for index, row in enumerate(desired_table.find_all('tr')):
                        if index == len(desired_table.find_all('tr')) - 1:
                            break
                        cells = row.find_all('td')
                        if cells:
                            # Extract data from specified columns
                            columns_to_extract = [0, 3, 6, 7, 8, 11, 12, 15,16, 17]  # 1, 4, 7, 8, 9, 10, 11, 12 columns
                            row_data = [cells[i].text.strip() for i in columns_to_extract if i < len(cells)]
                            data.append(row_data)

                    # Define column names
                    column_names = ['Date', 'Opposing team', 'played minutes', 'Goal conceded', 'Saves', 'Clean sheet', 'Fouls','Long passes', 'Yellow card', 'Red card']

                    # Create a DataFrame from the scraped data
                    df = pd.DataFrame(data, columns=column_names)

                    # Extract player's name from URL and capitalize each word
                    player_name_parts = url.split("/")[-1].split("-")[:-1]
                    player_name = " ".join([part.capitalize() for part in player_name_parts])

                    # Save the DataFrame to an Excel file
                    df.to_excel(f'{player_name}.xlsx', index=False)

                else:
                    desired_table = tables[1]  # Index 2 corresponds to the third table
                    data = []
                    for index, row in enumerate(desired_table.find_all('tr')):
                        if index == len(desired_table.find_all('tr')) - 1:
                            break
                        cells = row.find_all('td')
                        if cells:
                            # Extract data from specified columns
                            columns_to_extract = [0, 3, 6, 7, 8, 11, 12, 15,16, 17]  # 1, 4, 7, 8, 9, 10, 11, 12 columns
                            row_data = [cells[i].text.strip() for i in columns_to_extract if i < len(cells)]
                            data.append(row_data)

                    # Define column names
                    column_names = ['Date', 'Opposing team', 'played minutes', 'Goal conceded', 'Saves', 'Clean sheet', 'Fouls','Long passes', 'Yellow card', 'Red card']

                    # Create a DataFrame from the scraped data
                    df = pd.DataFrame(data, columns=column_names)

                    # Extract player's name from URL and capitalize each word
                    player_name_parts = url.split("/")[-1].split("-")[:-1]
                    player_name = " ".join([part.capitalize() for part in player_name_parts])

                    # Save the DataFrame to an Excel file
                    df.to_excel(f'{player_name}.xlsx', index=False)

            elif first_two_letters == "DF":
                tables = soup.find_all('table')

                # Assuming the third table is the one we want, extract the specified columns
                if len(tables) >= 8:
                    desired_table = tables[2]  # Index 2 corresponds to the third table
                    data = []
                    for index, row in enumerate(desired_table.find_all('tr')):
                        if index == len(desired_table.find_all('tr')) - 1:
                            break
                        cells = row.find_all('td')
                        if cells:
                            # Extract data from specified columns
                            columns_to_extract = [0, 3, 6, 7, 8,  11, 12,15,17, 26,25,28,30,31]  # 1, 4, 7, 8, 9, 10, 11, 12 columns
                            row_data = [cells[i].text.strip() for i in columns_to_extract if i < len(cells)]
                            data.append(row_data)

                    # Define column names
                    column_names = ['Date', 'Opposing team', 'played minutes', 'Goals', 'Assists', 'Shots', 'Shot on targets', 'Pass accuracy','Key passes','Takels', 'Clearances','Fouls','Yellow card', 'Red card']

                    # Create a DataFrame from the scraped data
                    df = pd.DataFrame(data, columns=column_names)

                    # Extract player's name from URL and capitalize each word
                    player_name_parts = url.split("/")[-1].split("-")[:-1]
                    player_name = " ".join([part.capitalize() for part in player_name_parts])

                    # Save the DataFrame to an Excel file
                    df.to_excel(f'{player_name}.xlsx', index=False)
                else:
                    desired_table = tables[1]  # Index 2 corresponds to the third table
                    data = []
                    for index, row in enumerate(desired_table.find_all('tr')):
                        if index == len(desired_table.find_all('tr')) - 1:
                            break
                        cells = row.find_all('td')
                        if cells:
                            # Extract data from specified columns
                            columns_to_extract = [0, 3, 6, 7, 8,  11, 12,15,17, 26,25,28,30,31]  # 1, 4, 7, 8, 9, 10, 11, 12 columns
                            row_data = [cells[i].text.strip() for i in columns_to_extract if i < len(cells)]
                            data.append(row_data)

                    # Define column names
                    column_names = ['Date', 'Opposing team', 'played minutes', 'Goals', 'Assists', 'Shots', 'Shot on targets', 'Pass accuracy','Key passes','Takels', 'Clearances','Fouls','Yellow card', 'Red card']

                    # Create a DataFrame from the scraped data
                    df = pd.DataFrame(data, columns=column_names)

                    # Extract player's name from URL and capitalize each word
                    player_name_parts = url.split("/")[-1].split("-")[:-1]
                    player_name = " ".join([part.capitalize() for part in player_name_parts])

                    # Save the DataFrame to an Excel file
                    df.to_excel(f'{player_name}.xlsx', index=False)

            else:
                tables = soup.find_all('table')

                # Assuming the third table is the one we want, extract the specified columns
                if len(tables) >= 8:
                    desired_table = tables[2]  # Index 2 corresponds to the third table
                    data = []
                    for index, row in enumerate(desired_table.find_all('tr')):
                        if index == len(desired_table.find_all('tr')) - 1:
                            break
                        cells = row.find_all('td')
                        if cells:
                            # Extract data from specified columns
                            columns_to_extract = [0, 3, 6, 7, 8,  11, 12, 15,17,18,28,30,31]  # 1, 4, 7, 8, 9, 10, 11, 12 columns
                            row_data = [cells[i].text.strip() for i in columns_to_extract if i < len(cells)]
                            data.append(row_data)

                    # Define column names
                    column_names = ['Date', 'Opposing team', 'played minutes', 'Goals', 'Assists', 'Shots', 'Shot on targets', 'Pass accuracy','Key passes', 'Offside','Fouls','Yellow card', 'Red card']

                    # Create a DataFrame from the scraped data
                    df = pd.DataFrame(data, columns=column_names)

                    # Extract player's name from URL and capitalize each word
                    player_name_parts = url.split("/")[-1].split("-")[:-1]
                    player_name = " ".join([part.capitalize() for part in player_name_parts])

                    # Save the DataFrame to an Excel file
                    df.to_excel(f'{player_name}.xlsx', index=False)
                    
                else:
                    desired_table = tables[1]  # Index 2 corresponds to the third table
                    data = []
                    for index, row in enumerate(desired_table.find_all('tr')):
                        if index == len(desired_table.find_all('tr')) - 1:
                            break
                        cells = row.find_all('td')
                        if cells:
                            # Extract data from specified columns
                            columns_to_extract = [0, 3, 6, 7, 8,  11, 12, 15,17,18,28,30,31]  # 1, 4, 7, 8, 9, 10, 11, 12 columns
                            row_data = [cells[i].text.strip() for i in columns_to_extract if i < len(cells)]
                            data.append(row_data)

                    # Define column names
                    column_names =  ['Date', 'Opposing team', 'played minutes', 'Goals', 'Assists', 'Shots', 'Shot on targets', 'Pass accuracy','Key passes', 'Offside','Fouls','Yellow card', 'Red card']

                    # Create a DataFrame from the scraped data
                    df = pd.DataFrame(data, columns=column_names)

                    # Extract player's name from URL and capitalize each word
                    player_name_parts = url.split("/")[-1].split("-")[:-1]
                    player_name = " ".join([part.capitalize() for part in player_name_parts])

                    # Save the DataFrame to an Excel file
                    df.to_excel(f'{player_name}.xlsx', index=False)

        else:
            print('Text is too short to extract first and second letters.')
    else:
        print(f'Element with class "whitespace-nowrap text-center md:text-left" not found on')
        
    driver.quit()

for url in urls:
    scrape_url(url)


# In[5]:


import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

# Path to the chromedriver executable
chrome_driver_path = 'C:/Users/Admin/Documents/research final - chelsea/Research/chromedriver.exe'


# List of URLs to scrape
urls = [
    'https://www.statmuse.com/fc/player/wesley-fofana-6507'
    # Add more URLs here
]


def scrape_url(url):
    driver = webdriver.Chrome(executable_path=chrome_driver_path)

    # Load the webpage
    driver.get(url)

    # Get the HTML content of the page
    html = driver.page_source

    # Close the browser
    

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all tables on the page
    tables = soup.find_all('table')

    # Assuming the third table is the one we want, extract the specified columns
    if len(tables) >= 2:
        desired_table = tables[1]  # Index 2 corresponds to the third table
        data = []
        for index, row in enumerate(desired_table.find_all('tr')):
            if index == len(desired_table.find_all('tr')) - 1:
                break
            cells = row.find_all('td')
            if cells:
                # Extract data from specified columns
                columns_to_extract = [0, 3, 6, 7, 8,  11, 12,15,17, 26,25,28,30,31]  # 1, 4, 7, 8, 9, 10, 11, 12 columns
                row_data = [cells[i].text.strip() for i in columns_to_extract if i < len(cells)]
                data.append(row_data)

        # Define column names
        column_names =['Date', 'Opposing team', 'played minutes', 'Goals', 'Assists', 'Shots', 'Shot on targets', 'Pass accuracy','Key passes','Takels', 'Clearances','Fouls','Yellow card', 'Red card']

        # Create a DataFrame from the scraped data
        df = pd.DataFrame(data, columns=column_names)

        # Extract player's name from URL and capitalize each word
        player_name_parts = url.split("/")[-1].split("-")[:-1]
        player_name = " ".join([part.capitalize() for part in player_name_parts])

         # Save the DataFrame to an Excel file
        df.to_excel(f'{player_name}.xlsx', index=False)
    else:
        print(f'There are not enough tables on the page for URL: {url}')
    driver.close()
# Scrape each URL in the list
for url in urls:
    scrape_url(url)

# Close the Excel writer object to save the file
