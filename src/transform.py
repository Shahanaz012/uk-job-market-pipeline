import json

try:
    with open('/home/shannu/Personal-Projects/uk-job-market-pipeline/data/raw_Data_analyst_20260520_193038.json', 'r') as file:
        data = json.load(file)
        for job in data["results"]:
            print(job["title"], job["company"]["display_name"], job["location"]["display_name"], job["salary_min"], job["contract_type"])
   
except FileNotFoundError:
    print("The file 'data.json' was not found.")
