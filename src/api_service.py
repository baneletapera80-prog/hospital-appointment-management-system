import requests
import json
import os

# Your MockAPI base URL
BASE_URL = "https://6ada27117512f497b3ffadb5.mockapi.io"
APPOINTMENTS_FILE = "appointments.json"

class ApiService:
    @staticmethod
    def get_data(endpoint):
        # Handle appointments locally using JSON file
        if endpoint == "appointments":
            if not os.path.exists(APPOINTMENTS_FILE):
                return []
            try:
                with open(APPOINTMENTS_FILE, "r") as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error reading local appointments: {e}")
                return []
        
        # Handle patients and doctors via MockAPI
        try:
            response = requests.get(f"{BASE_URL}/{endpoint}")
            if response.status_code == 200:
                return response.json()
            return []
        except Exception as e:
            print(f"Error fetching {endpoint}: {e}")
            return []

    @staticmethod
    def post_data(endpoint, data):
        # Handle saving appointments locally
        if endpoint == "appointments":
            try:
                appointments = []
                if os.path.exists(APPOINTMENTS_FILE):
                    with open(APPOINTMENTS_FILE, "r") as f:
                        appointments = json.load(f)
                
                # Assign a simple ID and append
                data["id"] = str(len(appointments) + 1)
                appointments.append(data)
                
                with open(APPOINTMENTS_FILE, "w") as f:
                    json.dump(appointments, f, indent=4)
                return True
            except Exception as e:
                print(f"Error saving local appointment: {e}")
                return False

        # Handle posting patients or doctors to MockAPI
        try:
            response = requests.post(f"{BASE_URL}/{endpoint}", json=data)
            return response.status_code in [200, 201]
        except Exception as e:
            print(f"Error posting to {endpoint}: {e}")
            return False

    @staticmethod
    def delete_data(endpoint, item_id):
        if endpoint == "appointments":
            try:
                if os.path.exists(APPOINTMENTS_FILE):
                    with open(APPOINTMENTS_FILE, "r") as f:
                        appointments = json.load(f)
                    appointments = [a for a in appointments if str(a.get("id")) != str(item_id)]
                    with open(APPOINTMENTS_FILE, "w") as f:
                        json.dump(appointments, f, indent=4)
                    return True
            except Exception as e:
                print(f"Error deleting local appointment: {e}")
                return False

        try:
            response = requests.delete(f"{BASE_URL}/{endpoint}/{item_id}")
            return response.status_code == 200
        except Exception as e:
            print(f"Error deleting from {endpoint}: {e}")
            return False