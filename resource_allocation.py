import numpy as np

# 动态资源分配策略
def allocate_resources(flow_stats, predictions):
    allocation = {}
    for i, flow in enumerate(flow_stats):
        priority = "high" if predictions[i] == 2 else "normal"
        allocation[flow["source_ip"]] = {
            "bandwidth": np.random.uniform(1, 10) if priority == "high" else 5,
            "priority": priority,
        }
    return allocation

if __name__ == "__main__":
    # 测试动态资源分配
    flow_stats = [
        {"source_ip": "192.168.1.1", "destination_ip": "10.0.0.1", "packet_size": 512},
    ]
    predictions = [2]  # 模拟预测结果
    allocation_map = allocate_resources(flow_stats, predictions)
    print("Allocation Map:", allocation_map)

