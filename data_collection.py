import json
import random
from datetime import datetime

def fetch_flow_stats(duration=100):
    """
    模拟流量数据采集，生成 JSON 格式的流量统计。
    """
    flow_stats = []
    for _ in range(duration):
        flow_record = {
            "timestamp": str(datetime.now()),
            "source_ip": f"192.168.1.{random.randint(1, 255)}",
            "destination_ip": f"10.0.0.{random.randint(1, 255)}",
            "protocol": random.choice(["TCP", "UDP"]),
            "packet_size": random.randint(64, 1500),
            "duration": round(random.uniform(0.1, 5.0), 2),
            "tcp_flags": random.choice(["SYN", "ACK", "FIN"]),
        }
        flow_stats.append(flow_record)
    return flow_stats

def save_flow_stats(data, file_path="./datasets/flow_stats.json"):
    """
    保存流量统计数据到 JSON 文件。
    """
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Flow statistics saved to {file_path}.")

if __name__ == "__main__":
    data = fetch_flow_stats(duration=100)
    save_flow_stats(data)


