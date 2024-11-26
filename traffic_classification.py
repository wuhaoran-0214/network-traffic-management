import lightgbm as lgb
import pandas as pd
import numpy as np

# 载入数据集
def load_data(file_path="./datasets/sample_data.csv"):
    return pd.read_csv(file_path)

# 训练分类模型
def train_classifier(data, labels):
    train_data = lgb.Dataset(data, label=labels)
    params = {
        "objective": "multiclass",
        "num_class": 3,
        "learning_rate": 0.05,
        "max_depth": 7,
        "feature_fraction": 0.8,
    }
    model = lgb.train(params, train_data, num_boost_round=100)
    model.save_model("./datasets/lightgbm_model.txt")
    return model

# 分类流量
def classify_traffic(flow_stats):
    model = lgb.Booster(model_file="./datasets/lightgbm_model.txt")
    data = pd.DataFrame(flow_stats)
    features = data[["packet_size", "duration", "tcp_flags"]]
    predictions = model.predict(features)
    return np.argmax(predictions, axis=1)

if __name__ == "__main__":
    # 加载数据并训练模型
    dataset = load_data()
    X = dataset.drop("label", axis=1)
    y = dataset["label"]
    train_classifier(X, y)

