import requests
import pandas as pd

def fetch_flow_stats(controller_ip):
    """
    Fetch flow statistics from ONOS REST API
    """
    url = f"http://{controller_ip}:8181/onos/v1/flows"
    headers = {"Accept": "application/json"}
    response = requests.get(url, auth=("onos", "rocks"), headers=headers)
    data = response.json()
    
    flows = []
    for flow in data["flows"]:
        flows.append({
            "flow_id": flow["id"],
            "src": flow["selector"]["criteria"][0]["ipv4Src"],
            "dst": flow["selector"]["criteria"][1]["ipv4Dst"],
            "bytes": flow["bytes"],
            "packets": flow["packets"]
        })
    return pd.DataFrame(flows)

# Save collected data
df = fetch_flow_stats("127.0.0.1")
df.to_csv("flow_stats.csv", index=False)
if response.status_code != 200:
    raise Exception(f"Failed to fetch flow stats: {response.status_code}")
