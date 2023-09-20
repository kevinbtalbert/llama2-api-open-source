# Host Your Own Open Source Llama2 API
Open Source Llama2 API for organizations to internally host from their CML environments

This can be added to CML via its Github link or the custom catalog entry: https://raw.githubusercontent.com/kevinbtalbert/llama2-api-open-source/main/catalog-entry.yaml

![](/assets/catalog-entry.png)

## Forming a request to the API
Requests can be formed intra-domain or cross-domain. For cross-domain requests, you'll need to ensure unauthenticated app access is allowed for the POST endpoint to be reachable.

![](/assets/unauthenticated-access.png)

For request syntax: 
GET and POST to the ROOT of the CML application endpoint (e.g. `https://subdomain.domain.go01-dem.ylcu-atmi.cloudera.site/`)
Successful GET request should indicate the API is up and running:

![](/assets/GET-endpoint.png)

### Forming the POST request can be done through Postman or natively in CML:

#### 1. Postman

Form the payload/url to match the below, and add the header `Content-Type | application/json`
![](/assets/postman-setup.png)


#### 2. Pythonic (also available in the 3_app folder as an Jupyter notebook)

```python
import requests
import json
import os

# URL to send the POST request to (set to yours)
external_url = "https://subdomain.domain.ylcu-atmi.cloudera.site/"
internal_url = "https://127.0.0.1:" + str(os.environ['CDSW_APP_PORT']) + "/"

# Choose which URL to use
url = internal_url

# Headers for the POST request
headers = {
    "Content-Type": "application/json"
}

# JSON Body for the POST request
payload = {
    "inputs": "What is Cloudera Data Science Workbench?",
    "parameters": {
        "temperature": 0.0,
        "max_tokens": 150
    }
}

# Convert Python dictionary to JSON
payload_json = json.dumps(payload)

# Make the POST request
response = requests.post(url, headers=headers, data=payload_json)

# Check if the request was successful
if response.status_code == 200:
    print(f"Success! Received response: {response.json()}")
else:
    print(f"Failed to make request. Status code: {response.status_code}, Response: {response.text}")

```

