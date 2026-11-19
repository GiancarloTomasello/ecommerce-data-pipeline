
def extract_Products(api_client):
    products = api_client.call_request("GET", "https://dummyjson.com/products", 10, 0)
    return products
