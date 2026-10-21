import os
import requests
from dotenv import load_dotenv

# Load keys from .env file
load_dotenv()
API_KEY = os.getenv("AVIATIONSTACK_KEY")

def get_flight_data(dep_iata, arr_iata):
    url = "http://api.aviationstack.com/v1/flights"
    
    params = {
        'access_key': API_KEY,
        'dep_iata': dep_iata,
        'arr_iata': arr_iata,
        'limit': 5 
    }
    
    print(f"Searching for flights from {dep_iata} to {arr_iata}...")
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status() # Throws an error if status is 4xx or 5xx
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": True, "message": str(e)}

if __name__ == "__main__":
    # Test connection
    data = get_flight_data("RIX", "HEL")
    print(data)