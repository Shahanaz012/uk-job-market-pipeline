import json
import pandas as pd
import os

try:
    job_list = []
    for filename in os.listdir("data/"):
        if filename.endswith(".json"):
            with open(f"data/{filename}", 'r') as file:
                data = json.load(file)
            for job in data["results"]:
                job_list.append({
                    "title" : job["title"],
                    "company" : job["company"]["display_name"],
                    "location" : job["location"]["display_name"],
                    "salary_min" : job.get("salary_min", 0),
                    "salary_max" : job.get("salary_max", 0),
                    "contract_type" : job.get("contract_type", "Not Specified")
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

def clean_location(location):
    if location == "UK":
        return "Not Specified"
    else:
        return location
df["location"] = df["location"].apply(clean_location)
df["salary_min"] = df["salary_min"].fillna(0)
df["salary_max"] = df["salary_max"].fillna(0)
df = df.drop_duplicates()
print(len(df))