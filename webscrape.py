import requests
from bs4 import BeautifulSoup

url = requests.get("https://elderscrolls.fandom.com/wiki/Books_(Skyrim)")

html_content = url.text

soup = BeautifulSoup(html_content, "html.parser")

# Assuming the table has a specific class or ID you want to target
table = soup.find("table")  # You can specify an ID/class, e.g., soup.find("table", {"id": "my-table"})
rows = table.find_all("tr")  # Get all table rows

# Extract table data
table_data = []
for row in rows:
    cells = row.find_all(["th", "td"])  # Get both header and cell data
    row_data = [cell.text.strip() for cell in cells]
    table_data.append(row_data)

# Write the data to csv
with open('tables.csv', 'w') as f:    
    #Write table
    for row in table_data:
        f.write(f'"{row[0]}",Unobtained,Not Read\n')