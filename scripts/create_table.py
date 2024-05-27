import pandas as pd

systems = ["EPaxos (NP)", "Multi-Paxos (NP)", "EPaxos", "Multi-Paxos"]
metrics = ["Throughput", "Median Latency (ms)", "99th Percentile Latency (ms)"]

df = pd.DataFrame(index=metrics, columns=systems)

values = {
    "EPaxos (NP)": [766.01, 1.18, 3.23],
    "Multi-Paxos (NP)": [855.46, 1.14, 1.92],
    "EPaxos": [1829.13, 0.95, 3.0],
    "Multi-Paxos": [2289.13, 0.8, 2.49]
}

for system in systems:
    df[system] = values[system]

print("Table 1: Performance comparison of EPaxos and Multi-Paxos for 3 replicas")
print(df.to_string(index=True, justify='left', float_format='{:.2f}'.format))
