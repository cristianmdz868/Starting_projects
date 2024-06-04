import requests
from bs4 import BeautifulSoup
import csv

# Fetch the webpage content
url = "https://www.statsamerica.org/sip/rank_list.aspx?rank_label=pop1"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find the specific table by class
    table = soup.find("table", attrs={"class": "table table-bordered table-condensed data"})
    
    if table:
        # Extract the headers
        headers = [th.text.strip() for th in table.find_all('th')]
        
        # Extract the rows of the table
        rows = []
        for tr in table.find_all('tr')[1:]:  # Skip the header row
            cells = [td.text.strip() for td in tr.find_all('td')]
            if cells:  # Ensure it's not an empty row
                rows.append(cells)
        
        # Write data to a CSV file
        with open('population_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)  # Write the header row
            writer.writerows(rows)  # Write the data rows
        
        print("Data has been successfully written to population_data.csv")
    else:
        print("No table found with the specified class.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
