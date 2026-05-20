#import all necessary libraries
import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import json

#load api key from the .env file
load_dotenv()
APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

#After connecting to the API I want to collect the data according my job search.

key_word = ["Data engineer", "ETL developer", "Data analyst", "SQL developer"]

def extract_data(keyword):

    url = f"https://api.adzuna.com/v1/api/jobs/gb/search/1"
    
    params = {
        "app_id" : APP_ID,
        "app_key" : APP_KEY,
        "what" : keyword,
        "content-type" : "application/json" 
    }
    
    try:
        result = requests.get(url, params=params, timeout=10)
    #after passing through the url using the id and key we will get the requested data
    # in a raw text format then using the json() converting into dictionary format
        if result.status_code == 200:
            return result.json()
        else:
            return None
    except requests.exceptions.Timeout:
        print(f"request time out for '{keyword}'")
        return None
    
    except requests.exceptions.ConnectionError:
        print(f"connection error occored for '{keyword}'")
        return None
    #Saving the extracted data.

def save_data(data, keyword):
    clean_data = keyword.replace(" ", "_")
    time_stamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"data/raw_{clean_data}_{time_stamp}.json"
         
    with open(filename, "w", encoding="utf-8") as f:
          json.dump(data, f, indent=2)


# main run function
def extract_start():
    print("Starting Extract Stage")
    for word in key_word:
        data = extract_data(word)
        if data:
            save_data(data, word) 
 
if __name__ == "__main__":
    extract_start()