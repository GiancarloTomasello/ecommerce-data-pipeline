import json

def extract_Categories(api_client):
    #Call API Client to get all categories
    categories = api_client.call_request("GET", "https://dummyjson.com/products/category-list")
    
    #Save the retuned data to a JSON file
    with open("../data/raw/categories.json", "w", encoding="utf-8") as file:
        json.dump(categories, file, indent=4)

    return categories
