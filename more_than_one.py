import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()

# Fetch ActionKit creds
ak_username = os.getenv("AK_USER")
ak_password = os.getenv("AK_PWD")

# Fetch Action Network API key
an_api_key = os.getenv("AN_KEY")

# ------------------- GET from ActionKit -------------------

ak_url = "https://roboticdogs.actionkit.com/rest/v1/user/"  # Adjust with filters if needed

ak_response = requests.get(ak_url, auth=HTTPBasicAuth(ak_username, ak_password))

if ak_response.status_code != 200:
    print(f"ActionKit GET failed with status code: {ak_response.status_code}")
    print(ak_response.text)
    exit()

ak_data = ak_response.json()
print("Data from ActionKit:")
print(json.dumps(ak_data, indent=2))

# ------------------- Loop Through Records -------------------

an_url = "https://actionnetwork.org/api/v2/people/"  # Confirm this endpoint is correct

an_headers = {
    "Content-Type": "application/json",
    "OSDI-API-Token": an_api_key
}

for user in ak_data['objects']:
    # Build the person_data for Action Network
    person_data = {
        "person": {
            "given_name": user.get("first_name", ""),
            "family_name": user.get("last_name", ""),
            "email_addresses": [
                {"address": user.get("email", "")}
            ],
            "phone_numbers": []
        }
    }

    # Optional: Add phone number logic here if needed
    if user.get("phones"):
        person_data["person"]["phone_numbers"].append({"number": "2020000000"})  # Replace with real GET if needed

    print("\nSending payload to Action Network:")
    print(json.dumps(person_data, indent=2))

    # POST to Action Network
    an_response = requests.post(an_url, headers=an_headers, json=person_data)

    print("Status Code from Action Network:", an_response.status_code)
    try:
        print("Response from Action Network:")
        print(json.dumps(an_response.json(), indent=2))
    except Exception:
        print("Raw Response:")
        print(an_response.text)

print("\nAll records processed. Parade over.")
