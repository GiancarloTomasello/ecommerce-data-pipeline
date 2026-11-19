from ingestion.api_client import ApiClient
from ingestion.extract_products import extract_Products
import json


client = ApiClient()

products = extract_Products(client)
#print(products)
