import subprocess
import pandas as pd
import re
import matplotlib.pyplot as plt

def run_analysis(filename, clients):
    path = f"../../../logs/no-batching/logs-3-replicas-{filename}"

    if filename == "epaxos100" or filename == "mencius100":
        command = ["python3", f"analysis.py", f"{path}/{filename}-S3-C{clients}-r20000-b1-c100--client0.out"]
    elif filename == "epaxos25":
        command = ["python3", f"analysis.py", f"{path}/{filename}-S3-C{clients}-r20000-b1-c25--client0.out"]
    else:
        command = ["python3", f"analysis.py", f"{path}/{filename}-S3-C{clients}-r20000-b1-c0--client0.out"]
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

systems = ["EPaxos 0%", "EPaxos 25%", "EPaxos 100%", "Mencius 0%", "Mencius 100%", "Multi-Paxos"]
file_names = ["epaxos0", "epaxos25", "epaxos100", "mencius0", "mencius100", "paxos"]
clients = [20, 40, 60, 80, 100]
metrics = ["Throughput", "Median Latency (ms)", "99th Percentile Latency (ms)"]

dfs = []
for system, file_name in zip(systems, file_names):
    for client in clients:
        output = run_analysis(file_name, client)
        df = create_plots(system, output, client)
        dfs.append(df)

result_df = pd.concat(dfs, ignore_index=True)

plt.figure(figsize=(10, 6))
markers=['o', 's', 'd', 'x', '+', '*']
i = 0
for system in systems:
    system_data = result_df[result_df['System'] == system]
    plt.plot(system_data['Throughput'], system_data['Median Latency (ms)'],
             marker=markers[i], linestyle='-', markersize=8, label=system)
    i += 1

plt.xlabel('Throughput (ops/sec)')
plt.ylabel('Median Latency (ms)')
plt.title('Median Latency vs Throughput for 3 replicas')
plt.legend(title='System')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
i = 0
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
