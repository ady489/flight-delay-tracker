import time
from api_client import get_flight_data
from analyzer import analyze_flights

def run_tracker():
    print("Starting Flight Tracker...")
    
    departure = "RIX"
    arrival = "HEL"
    
    while True:
        try:
            raw_data = get_flight_data(departure, arrival)
            analyze_flights(raw_data)
            
            print("\nWaiting 30 minutes before next check...")
            time.sleep(1800) 
            
        except KeyboardInterrupt:
            print("\nTracker stopped.")
            break
        except RuntimeError as e:
            print(f"Error: {e}")
            time.sleep(300)

if __name__ == "__main__":
    run_tracker()