import pandas as pd

systems = ["EPaxos (NP)", "Multi-Paxos (NP)", "EPaxos", "Multi-Paxos"]
metrics = ["Throughput", "Median Latency (ms)", "99th Percentile Latency (ms)"]

df = pd.DataFrame(index=metrics, columns=systems)

values = {
    "EPaxos (NP)": [...],
    "Multi-Paxos (NP)": [...],
    "EPaxos": [...],
    "Multi-Paxos": [...]
}

for system in systems:
    df[system] = values[system]

print("Table 1: Performance comparison of EPaxos and Multi-Paxos for 3 replicas")
print(df.to_string(index=True, justify='left', float_format='{:.2f}'.format))
