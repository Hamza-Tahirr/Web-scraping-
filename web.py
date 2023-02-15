import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_most_visited_websites'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the website names
table = soup.find('table', class_='wikitable')

# Find all the rows in the table
rows = table.find_all('tr')

# Extract the website names from each row
website_names = []
for row in rows[1:]:
    cols = row.find_all('td')
    website_names.append(cols[1].text.strip())

# Create a Pandas dataframe with the website names
df = pd.DataFrame({'Website Name': website_names})

# Print the dataframe
print(df)
