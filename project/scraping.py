import requests
import csv

# Make a GET request to the API
response = requests.get("http://servicodados.ibge.gov.br/api/v2/censos/nomes/")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()

    # Specify the CSV file path
    csv_file_path = "data.csv"

    # Extract relevant data from the API response
    extracted_data = []
    for entry in data:
        name = entry.get("nome", "")
        region = entry.get("localidades", [{}])[0].get("nome", "")
        extracted_data.append([name, region])

    # Write the data to a CSV file
    with open(csv_file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Region"])
        writer.writerows(extracted_data)

    print("Data successfully stored in", csv_file_path)
else:
    print("Failed to retrieve data from the API.")
