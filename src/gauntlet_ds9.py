cluster_nodes = [
    {"node_id": "cluster-01a", "region": "eu-west", "latency_ms": 14.2, "ram_pct": 62.5, "status": "online"},
    {"node_id": "cluster-02b", "region": "us-east", "latency_ms": 115.8, "ram_pct": 89.1, "status": "online"}, # High stress!
    {"node_id": "cluster-03c", "region": "af-south", "latency_ms": 0.0, "ram_pct": 0.0, "status": "offline"}, # Offline node!
    {"node_id": "cluster-04d", "region": "eu-west", "latency_ms": 95.4, "ram_pct": 87.4, "status": "online"},  # High stress!
    {"node_id": "cluster-05e", "region": "us-east", "latency_ms": 18.1, "ram_pct": 41.2, "status": "online"}
]

active_node = list(filter(lambda x : x["status"] == "online", cluster_nodes))
def assessment(node):
    node_id = node["node_id"]
    latency = node["latency_ms"]
    ram = node["ram_pct"]
    
    if latency > 90.0 or ram > 80.0:
        return (node_id, STRESSED, latency)
    else:
        return ({node_id, HEALTHY, latency) 

node_profiles = list(map(assessment, active_node))
latencies = list(map(lambda profile : profile[2], node_profiles))
from functools import reduce
total_latency = reduce(lambda a, b : a + b, latencies)
average_latency = total_latency / len(node_profiles)

print("="*45)
print(f"{'ENTERPRISE DASHBOARD':^45}")
print("="*45)
for node_id, status, latency in node_profiles:
    label = f"{node_id} [{status}]"
    print(f"{label:<33}{f'{latency:.2f} ms':>12}")
print(f"{'Average Latency':<25}{f'{average_latency:.2f}':>20}")

