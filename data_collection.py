import json
import numpy as np
from datetime import datetime
import random

# 模拟采集流量数据
def fetch_flow_stats(source="127.0.0.1", duration=60):
    """
    模拟从网络设备采集流量数据。
    Parameters:
        source (str): 数据来源 IP 地址
        duration (int): 数据采集持续时间（秒）
    Returns:
        list: 包含流量记录的字典列表
    """
    flow_stats = []
    for i in range(duration):
        flow_record = {
            "timestamp": str(datetime.now()),
            "source_ip": source,
            "destination_ip": f"192.168.1.{random.randint(1, 255)}",
            "protocol": random.choice(["TCP", "UDP"]),
            "packet_size": np.random.normal(512, 50),
            "duration": random.uniform(0.1, 5),
            "tcp_flags": random.choice(["SYN", "ACK", "FIN"]),
        }
        flow_stats.append(flow_record)
    return flow_stats

# 保存为JSON文件
def save_flow_stats(data, file_path="./datasets/flow_stats.json"):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Flow statistics saved to {file_path}.")

if __name__ == "__main__":
    # 采集模拟流量
    flow_data = fetch_flow_stats()
    save_flow_stats(flow_data)

