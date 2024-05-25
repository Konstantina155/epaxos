import subprocess
import pandas as pd
import re

def run_analysis(filename):
    path = f"logs-{replicas}-replicas-{filename}"

    if "np_" in filename:
        command = ["python3", f"analysis.py", f"{path}/{filename}-S3-C2-r20000-b1-c-1--client0.out"]
    else:
        command = ["python3", f"analysis.py", f"{path}/{filename}-S3-C2-r20000-b1-c0--client0.out"]
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

def fill_table(df, system, output):
    df.loc['Throughput', system], df.loc['Median Latency (ms)', system], df.loc['99th Percentile Latency (ms)', system] = parse_output(output)

systems = ["EPaxos (NP)", "Multi-Paxos (NP)", "Mencius (NP)", "EPaxos", "Multi-Paxos", "Mencius"]
file_names = ["np_epaxos", "np_paxos", "np_mencius", "p_epaxos", "p_paxos", "p_mencius"]

metrics = ["Throughput", "Median Latency (ms)", "99th Percentile Latency (ms)"]
df = pd.DataFrame(index=metrics, columns=systems)

for system, file_name in zip(systems, file_names):
    output = run_analysis(file_name)
    fill_table(df, system, output)

print("Table 1: Performance comparison of EPaxos, Multi-Paxos, and Mencius for 3 replicas")
print(df.to_string(index=True, justify='left', float_format='{:.2f}'.format))
