import json

def extract_Users(api_client):
    #Call API Client to get all users
    users = api_client.call_request("GET", "https://dummyjson.com/users", {"limit":0})
    
    #Save the retuned data to a JSON file
    with open("../data/raw/users.json", "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)

    return users
