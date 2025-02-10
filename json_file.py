import requests
import json

class APIClient:

    def fetch_and_save_data(self):
        response = requests.get("https://dummyjson.com/posts")
        data = response.json()

        with open(r"D:\apexa_webscrspping\REST_API_DAY4\ayta.json", "w") as file:
            json.dump(data, file, indent=4)
            
        return data
    fetch_and_save_data()
