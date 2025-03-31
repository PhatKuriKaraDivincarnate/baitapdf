import pandas as pd
import os
import matplotlib.pyplot as plt

# 1️⃣ Đọc dữ liệu từ các file CSV
folder_path = "D:/bai tap/PythonProject1/data/"

file_names = [
    "city_attributes.csv",
    "humidity.csv",
    "pressure.csv",
    "temperature.csv",
    "weather_description.csv",
    "wind_direction.csv",
    "wind_speed.csv"
]

# Dictionary lưu các DataFrame
dataframes = {}

for file in file_names:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path, parse_dates=['datetime']) if 'datetime' in pd.read_csv(file_path, nrows=1).columns else pd.read_csv(file_path)
    dataframes[file.replace(".csv", "")] = df

# Hiển thị kiểu dữ liệu datetime
for key, df in dataframes.items():
    if 'datetime' in df.columns:
        print(f"{key}: {df['datetime'].dtype}")

# 2️⃣ Gộp dữ liệu với suffix tránh trùng cột
df_merged = dataframes["temperature"]

merge_list = ["humidity", "pressure", "wind_speed"]

for dataset in merge_list:
    df_merged = df_merged.merge(dataframes[dataset], on="datetime", how="outer", suffixes=("", f"_{dataset}"))

# 3️⃣ Xử lý dữ liệu
df_merged['year'] = df_merged['datetime'].dt.year
df_merged['month'] = df_merged['datetime'].dt.month
df_merged['day'] = df_merged['datetime'].dt.day
df_merged['hour'] = df_merged['datetime'].dt.hour
df_merged['day_of_week'] = df_merged['datetime'].dt.dayofweek  # 0 = Monday, 6 = Sunday

# 4️⃣ Thống kê trung bình theo ngày
df_daily = df_merged.resample("D", on="datetime").mean()

# 5️⃣ Trực quan hóa nhiệt độ trung bình theo thời gian
plt.figure(figsize=(12, 6))
plt.plot(df_daily.index, df_daily["New York"], label="New York")
plt.plot(df_daily.index, df_daily["Los Angeles"], label="Los Angeles")
plt.plot(df_daily.index, df_daily["Chicago"], label="Chicago")
plt.xlabel("Ngày")
plt.ylabel("Nhiệt độ (K)")
plt.title("Nhiệt độ trung bình theo ngày")
plt.legend()
plt.show()
