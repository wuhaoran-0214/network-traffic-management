import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

# 加载数据
def load_prediction_data(file_path="./datasets/training_data.csv"):
    data = np.loadtxt(file_path, delimiter=",")
    return data

# 训练 LSTM 模型
def train_lstm(data):
    scaler = MinMaxScaler()
    data = scaler.fit_transform(data.reshape(-1, 1))

    # 构造时间序列数据
    X, y = [], []
    for i in range(len(data) - 10):
        X.append(data[i : i + 10])
        y.append(data[i + 10])
    X, y = np.array(X), np.array(y)

    # 构建模型
    model = Sequential()
    model.add(LSTM(64, input_shape=(X.shape[1], 1), return_sequences=False))
    model.add(Dense(1))
    model.compile(optimizer="adam", loss="mse")
    model.fit(X, y, epochs=20, batch_size=32, validation_split=0.2)

    # 保存模型
    model.save("./datasets/lstm_model.h5")
    return model

# 流量预测
def predict_traffic(data):
    from keras.models import load_model

    model = load_model("./datasets/lstm_model.h5")
    scaler = MinMaxScaler()
    data = scaler.fit_transform(data.reshape(-1, 1))
    return model.predict(data.reshape(1, -1, 1))

if __name__ == "__main__":
    # 加载数据并训练模型
    data = load_prediction_data()
    train_lstm(data)

