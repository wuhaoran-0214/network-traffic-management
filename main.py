from data_collection import fetch_flow_stats
from traffic_classification import classify_traffic
from traffic_prediction import predict_traffic
from resource_allocation import allocate_resources

def main():
    # Step 1: Fetch data
    print("Fetching network flow statistics...")
    flow_stats = fetch_flow_stats("127.0.0.1")  # Replace with actual SDN controller IP

    # Step 2: Classify traffic
    print("Classifying traffic...")
    classification_results = classify_traffic(flow_stats)
    print("Classification Results:", classification_results)

    # Step 3: Predict traffic
    print("Predicting future traffic trends...")
    predictions = predict_traffic(flow_stats)
    print("Predictions:", predictions)

    # Step 4: Allocate resources
    print("Allocating resources based on predictions...")
    allocation = allocate_resources(flow_stats, predictions)
    print("Resource Allocation Map:", allocation)

if __name__ == "__main__":
    main()

