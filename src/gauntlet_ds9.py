cluster_nodes = [
    {"node_id": "cluster-01a", "region": "eu-west", "latency_ms": 14.2, "ram_pct": 62.5, "status": "online"},
    {"node_id": "cluster-02b", "region": "us-east", "latency_ms": 115.8, "ram_pct": 89.1, "status": "online"}, # High stress!
    {"node_id": "cluster-03c", "region": "af-south", "latency_ms": 0.0, "ram_pct": 0.0, "status": "offline"}, # Offline node!
    {"node_id": "cluster-04d", "region": "eu-west", "latency_ms": 95.4, "ram_pct": 87.4, "status": "online"},  # High stress!
    {"node_id": "cluster-05e", "region": "us-east", "latency_ms": 18.1, "ram_pct": 41.2, "status": "online"}
]

active_node = list(filter(lambda x : x["status"] = "online", cluster_nodes))
def assessment(node):
    node_id = node["node_id"]
    latency = node["latency_ms"]
    ram = node["ram_pct"]
    
    if latency > 90.0 or ram > 80.0:
        return (f"{node_id}, STRESSED, {latency}")
    else:
        return (f"{node_id}, HEALTHY, {latency}") 

node_profiles = list(map(assessment, active_node))

from functools import reduce
aggregate = reduce(lambda a, b : a + b )

