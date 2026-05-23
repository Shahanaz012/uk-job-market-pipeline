import json
import pandas as pd

try:
    with open('/home/shannu/Personal-Projects/uk-job-market-pipeline/data/raw_Data_analyst_20260520_193038.json', 'r') as file:
        data = json.load(file)
        job_list = []
        for job in data["results"]:
            job_list.append({
                "title" : job["title"],
                "company" : job["company"]["display_name"],
                "location" : job["location"]["display_name"],
                "salary_min" : job["salary_min"],
                "salary_max" : job["salary_max"],
                "contract_type" : job["contract_type"]
            })
        df = pd.DataFrame(job_list)

except FileNotFoundError:
    print("The file 'data.json' was not found.")

def clean_data(title):
    if "Trainee" in title:
        return "Trainee Data Analyst"
    if "No experience" in title:
        return "Trainee Data Analyst"
    else:
        return title
df["title"] = df["title"].apply(clean_data)

print(df.head())