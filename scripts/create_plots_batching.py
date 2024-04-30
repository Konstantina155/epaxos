import subprocess
import pandas as pd
import re
import matplotlib.pyplot as plt

def run_analysis(filename, clients, replicas): # change number of requests to 20000
    if filename == "batching_epaxos100":
        command = ["python3", f"analysis.py", f"logs/{filename}-S{replicas}-C{clients}-r200-b10-c100--client0.out"]
    else:
        command = ["python3", f"analysis.py", f"logs/{filename}-S{replicas}-C{clients}-r200-b10-c0--client0.out"]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def parse_output(output):
    throughput_match = re.search(r"Throughput \(ops/sec\): (\d+\.\d+)", output)
    median_match = re.search(r"Median latency: (\d+\.\d+)ms", output)
    percentile_match = re.search(r"99th percentile latency: (\d+\.\d+)ms", output)
    if median_match and percentile_match and throughput_match:
        return float(throughput_match.group(1)), float(median_match.group(1)), float(percentile_match.group(1))
    else:
        raise ValueError("Failed to parse latency output")

def create_plots(system, output, client):
    throughput, median_latency, percentile_latency = parse_output(output)
    df = pd.DataFrame({
        'Throughput': [throughput],
        'Median Latency (ms)': [median_latency],
        '99th Percentile Latency (ms)': [percentile_latency],
        'System': [system],
        'Clients': [client]
    })
    return df

systems = ["EPaxos 0%", "EPaxos 100%", "Multi-Paxos"]
file_names = ["batching_epaxos0", "batching_epaxos100", "batching_paxos"]
clients = [20, 40, 60, 80, 100, 200, 300, 400, 500]
metrics = ["Throughput", "Median Latency (ms)", "99th Percentile Latency (ms)"]
replicas = [3, 5]

markers=['o', 's', 'd', 'x', '+', '*', '^', 'v', '>', '<']
i = 0
for replica in replicas:
    dfs = []
    for system, file_name in zip(systems, file_names):
        for client in clients:
            output = run_analysis(file_name, client, replica)
            df = create_plots(system, output, client)
            dfs.append(df)

    result_df = pd.concat(dfs, ignore_index=True)

    plt.figure(figsize=(10, 6))

    for system in systems:
        system_data = result_df[result_df['System'] == system]
        plt.plot(system_data['Throughput'], system_data['Median Latency (ms)'],
                marker=markers[i], linestyle='-', markersize=8, label=system)

    plt.xlabel('Throughput (ops/sec)')
    plt.ylabel('Median Latency (ms)')
    plt.title('Median Latency vs Throughput for 3 replicas')
    plt.legend(title='System')
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    for system in systems:
        system_data = result_df[result_df['System'] == system]
        plt.plot(system_data['Throughput'], system_data['99th Percentile Latency (ms)'],
                marker=markers[i], linestyle='-', markersize=8, label=system)
    i += 1

    plt.xlabel('Throughput (ops/sec)')
    plt.ylabel(f'99%ile Latency (ms)')
    plt.title(f'99%ile Latency (ms) vs Throughput for 3 replicas')
    plt.legend(title='System')
    plt.grid(True)
    plt.show()