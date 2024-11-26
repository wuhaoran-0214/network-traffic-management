import lightgbm as lgb
import pandas as pd

# Load dataset
data = pd.read_csv("flow_stats.csv")
X = data.drop(columns=["label"])  # Features
y = data["label"]  # Labels

# Prepare data for LightGBM
train_data = lgb.Dataset(X, label=y)

# Define parameters and train model
params = {
    "objective": "multiclass",
    "num_class": 5,
    "learning_rate": 0.1,
    "boosting_type": "gbdt",
    "max_depth": 10
}
model = lgb.train(params, train_data, num_boost_round=100)

# Save trained model
model.save_model("lightgbm_model.txt")
from sklearn.metrics import classification_report
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
model.save_model("lightgbm_model.txt")
# 加载模型
model = lgb.Booster(model_file="lightgbm_model.txt")
