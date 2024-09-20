import requests
import json


def test_api_connection():
    # Define the API endpoint    
    url = "http://api.open-notify.org/astros"

    try:
        # Make a GET request to the API
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            print("API connection successful")
            print("Response Status Code:", response.status_code)
            # Print the response JSON
            response_json = response.json()
            print("Response JSON:", json.dumps(response_json, indent=4))
        else:
            print("API connection unsuccessful")
            print("Response Status Code:", response.status_code)
            print("Response Content:", response.content)

    except requests.exceptions.RequestException as e:
        print("Error: Cannot connect to the API")
        print("Exception:", e)

# Call the function
test_api_connection()
