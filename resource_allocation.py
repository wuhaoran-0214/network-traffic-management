def allocate_resources(flow_stats, predictions):
    """
    Allocate resources based on flow predictions and classifications.
    """
    allocation_map = {}
    for flow in flow_stats:
        flow_id = flow["flow_id"]
        bandwidth = predictions.get(flow_id, 0) * flow["priority"]
        allocation_map[flow_id] = min(bandwidth, MAX_BANDWIDTH)
    return allocation_map

def update_onos_flows(controller_ip, allocation_map):
    """
    Update ONOS flow rules based on allocation map
    """
    for flow_id, bandwidth in allocation_map.items():
        url = f"http://{controller_ip}:8181/onos/v1/flows/{flow_id}"
        data = {"bandwidth": bandwidth}
        requests.post(url, json=data, auth=("onos", "rocks"))
