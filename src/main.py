from ingestion.api_client import ApiClient


client = ApiClient()
resp = client.call_request("Get", 'https://api.github.com/events', 5)
print(resp.status_code)