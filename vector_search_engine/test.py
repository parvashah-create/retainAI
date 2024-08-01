# from pymilvus import connections


# connections.connect(
#   alias="default", 
#   host='http://54.160.87.79', 
#   port='9091'
# )

# import requests

# url = "http://54.160.87.79:9091/api/v1/health"
# response = requests.get(url)

# if response.status_code == 200:
#     print(response.content)
# else:
#     print("Error:", response.status_code)


import requests
import json

# Set the API endpoint URL
url = 'http://54.160.87.79:9091/api/v1/collection'

# Set the headers
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

# Set the request data
data = {
    "collection_name": "book",
    "schema": {
        "autoID": False,
        "description": "Test book search",
        "fields": [
            {
                "name": "book_id",
                "description": "book id",
                "is_primary_key": True,
                "autoID": False,
                "data_type": 5
            },
            {
                "name": "word_count",
                "description": "count of words",
                "is_primary_key": False,
                "data_type": 5
            },
            {
                "name": "book_intro",
                "description": "embedded vector of book introduction",
                "data_type": 101,
                "is_primary_key": False,
                "type_params": [
                    {
                        "key": "dim",
                        "value": "2"
                    }
                ]
            }
        ],
        "name": "book"
    }
}

# Send the HTTP request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Print the response status code and body
print('Status code:', response.status_code)
print('Response body:', response.json())

# # Set the API endpoint URL
url = 'http://54.160.87.79:9091/api/v1/collection/existence'

# Set the headers
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

# Set the request data
data = {
    "collection_name": "book",
}

# Send the HTTP request
response = requests.get(url, headers=headers, data=json.dumps(data))

# # Print the response status code and body
# print('Status code:', response.status_code)
# print('Response body:', response.json())

url = 'http://54.160.87.79:9091/api/v1/collection'

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
    'collection_name': 'book'
}

response = requests.get(url, headers=headers, data=json.dumps(data))

print('Status code:', response.status_code)
print('Response body:', response.json())