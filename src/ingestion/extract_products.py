import json

def extract_Products(api_client):
    #Call API Client to get all products
    products = api_client.call_request("GET", "https://dummyjson.com/products", {"limit":0})
    
    #Save the retuned data to a JSON file
    with open("../data/raw/products.json", "w", encoding="utf-8") as file:
        json.dump(products, file, indent=4)

    return products
