from data_collection import fetch_flow_stats
from traffic_classification import classify_traffic
from traffic_prediction import predict_traffic
from resource_allocation import allocate_resources

# Step 1: Fetch data from ONOS
flow_stats = fetch_flow_stats("127.0.0.1")

# Step 2: Classify traffic
classification_results = classify_traffic(flow_stats)

# Step 3: Predict traffic
predictions = predict_traffic(flow_stats)

# Step 4: Allocate resources
allocation_map = allocate_resources(flow_stats, predictions)

# Output allocation results
print("Resource Allocation Map:", allocation_map)
