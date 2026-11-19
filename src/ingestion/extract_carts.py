import json

def extract_Carts(api_client):
    #Call API Client to get all carts
    carts = api_client.call_request("GET", "https://dummyjson.com/carts", {"limit":0})
    
    #Save the retuned data to a JSON file
    with open("../data/raw/carts.json", "w", encoding="utf-8") as file:
        json.dump(carts, file, indent=4)

    return carts
