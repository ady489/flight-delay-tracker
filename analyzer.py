from notifier import send_alert_email

def analyze_flights(data):
    if "error" in data:
        print(f"API Error: {data['message']}")
        return

    flights = data.get('data', [])
    
    if not flights:
        print("No flights found for this route today.")
        return

    print(f"\n--- Found {len(flights)} flights ---")
    
    for flight in flights:
        airline = flight['airline']['name']
        flight_num = flight['flight']['iata']
        dep_delay = flight['departure']['delay']
        arr_time = flight['arrival']['scheduled']
        
        # If delay is None, set to 0
        delay_minutes = dep_delay if dep_delay else 0
        delay_status = f"{delay_minutes} mins late" if delay_minutes > 0 else "On time"
        
        print(f"{airline} ({flight_num}) | Arrives: {arr_time} | Status: {delay_status}")
        
        # Trigger alert for delays over 10 minutes
        if delay_minutes >= 10:
            alert_message = f"Flight {airline} ({flight_num}) is delayed by {delay_minutes} mins. ETA: {arr_time}"
            print(f"--> Sending alert for {flight_num}...")
            send_alert_email(alert_message)

if __name__ == "__main__":
    # Dummy data for quick testing
    test_data = {'data': []} 
    analyze_flights(test_data)