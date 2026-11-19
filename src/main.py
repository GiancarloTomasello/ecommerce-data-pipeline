from ingestion.api_client import ApiClient
from ingestion import extract_categories, extract_users, extract_products, extract_carts

import json


client = ApiClient()

products = extract_products.extract_Products(client)
users = extract_users.extract_Users(client)
categories = extract_categories.extract_Categories(client)
carts = extract_carts.extract_Carts(client)
