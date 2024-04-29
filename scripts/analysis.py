import statistics
import re
import sys

def extract_time(line):
    words = line.split(" ")
    if len(words) != 3 or words[1] != "took":
        return None

    match = re.search(r'\d+\.\d+', line)
    if match:
        return float(match.group())
    else:
        return None

def extract_clients_and_reqs(line):
    num_clients_pattern = r'Num_clients:(\d+)'
    num_requests_pattern = r'num_requests:(\d+)'

    num_clients_match = re.search(num_clients_pattern, line)
    num_requests_match = re.search(num_requests_pattern, line)

    if num_clients_match:
        num_clients = int(num_clients_match.group(1))
    else:
        num_clients = None

    if num_requests_match:
        num_requests = int(num_requests_match.group(1))
    else:
        num_requests = None
    return num_clients, num_requests

def analyze_latency(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    latencies = []
    for line in lines:
        words = line.split(" ")
        if len(words) != 3 or words[0] != "Round":
            continue

        match = re.search(r'\d+\.\d+', line)
        if match:
            seconds = float(match.group())
            milliseconds = seconds * 1000
            latencies.append(milliseconds)

    if latencies:
        median_latency = statistics.median(latencies)
        percentile_latency = statistics.quantiles(latencies, n=100, method='inclusive')[-1]

        print(f"Median latency: {median_latency}ms")
        print(f"99th percentile latency: {percentile_latency}ms")
    else:
        print("No latency data found in the file.")

def analyze_throughput(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    start_time = 0
    end_time = 0
    flag = False
    first_line = True
    for line in lines:
        if first_line:
            num_clients, num_req = extract_clients_and_reqs(line)
            first_line = False

        time = extract_time(line)
        
        if time is not None:
            if flag:
                end_time = time
            else:
                start_time = time
                flag = True

    if flag:
        time_in_s = end_time - start_time
        throughput = (num_clients * num_req) / time_in_s

        print("Throughput (client requests per second):", throughput)
    else:
        print("No throughput data found in the file.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 analysis.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]

    analyze_latency(filename)
    analyze_throughput(filename)