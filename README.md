# Bài tập 4: Phân tích dữ liệu thời tiết

## 📌 Thông tin sinh viên
- **Họ tên:** Nguyễn Chí Phát  
- **MSSV:** K215480106116  
- **Lớp:** K57KMT  

## 📥 Dữ liệu: Hourly Weather Data
Dữ liệu được lấy từ Kaggle, bạn có thể tải về tại [đây](https://www.kaggle.com/datasets/selfishgene/historical-hourly-weather-data).
Dữ liệu bao gồm các file CSV với thông tin về nhiệt độ, độ ẩm, áp suất khí quyển, tốc độ gió, hướng gió v.v.

---

## ✅ Yêu cầu bài tập

1. **Đọc dữ liệu** và kiểm tra thông tin cột thời gian.
2. **Lọc dữ liệu**: Chỉ giữ lại dữ liệu từ năm 2015 trở đi.
3. **Trích xuất thông tin thời gian**: Thêm cột `year`, `month`, `day_of_week`, `hour`.
4. **Lấy mẫu lại dữ liệu**: Chuyển từ dữ liệu theo giờ thành trung bình nhiệt độ theo ngày.
5. **Nội suy dữ liệu bị thiếu** để điền nhiệt độ bị khuyết.
6. **Tính toán xu hướng thời gian**: Tính nhiệt độ trung bình theo tháng và vẽ biểu đồ.

---

## 📊 Hướng dẫn thực hiện

### 1. Đọc dữ liệu và kiểm tra cột thời gian
```python
import pandas as pd

df_temperature = pd.read_csv("temperature.csv", parse_dates=['datetime'])
print(df_temperature['datetime'].dtype)  # Kiểm tra kiểu dữ liệu cột datetime
```
**Nguyên lý hoạt động:**
- Dữ liệu được đọc từ tệp CSV.
- Cột `datetime` được chuyển thành kiểu dữ liệu datetime để dễ xử lý.

### 2. Lọc dữ liệu từ năm 2015
```python
df_filtered = df_temperature[df_temperature['datetime'].dt.year >= 2015]
print(df_filtered.head())
```
**Nguyên lý hoạt động:**
- Lọc dữ liệu chỉ giữ lại các hàng có năm từ 2015 trở đi.
- Dữ liệu được trích xuất từ cột `datetime`.

### 3. Trích xuất thông tin thời gian
```python
df_filtered['year'] = df_filtered['datetime'].dt.year
df_filtered['month'] = df_filtered['datetime'].dt.month
df_filtered['day_of_week'] = df_filtered['datetime'].dt.day_name()
df_filtered['hour'] = df_filtered['datetime'].dt.hour
```
**Nguyên lý hoạt động:**
- Tạo các cột mới để trích xuất thông tin năm, tháng, ngày trong tuần, và giờ.
- Dữ liệu này giúp phân tích thời gian chi tiết hơn.

### 4. Lấy mẫu lại dữ liệu theo ngày
```python
df_daily_avg = df_filtered.resample('D', on='datetime').mean()
print(df_daily_avg.head())
```
**Nguyên lý hoạt động:**
- Sử dụng phương thức `.resample('D')` để lấy trung bình dữ liệu theo ngày.
- Các giá trị nhiệt độ theo giờ sẽ được gộp thành một giá trị trung bình mỗi ngày.

### 5. Nội suy dữ liệu bị thiếu
```python
df_filtered.interpolate(method='linear', inplace=True)
print(df_filtered.isnull().sum())  # Kiểm tra xem còn giá trị null không
```
**Nguyên lý hoạt động:**
- Sử dụng nội suy tuyến tính (`linear interpolation`) để điền các giá trị bị thiếu trong dữ liệu.
- Giúp tránh lỗi khi phân tích và vẽ biểu đồ.

### 6. Tính xu hướng nhiệt độ theo tháng và vẽ biểu đồ
```python
import matplotlib.pyplot as plt

df_filtered['month'] = df_filtered['datetime'].dt.to_period('M')
monthly_avg_temp = df_filtered.groupby('month')['New York'].mean()

plt.figure(figsize=(10, 5))
monthly_avg_temp.plot(kind='line', marker='o', color='b', linestyle='-', linewidth=2, markersize=6)
plt.title("Xu hướng nhiệt độ trung bình theo tháng")
plt.xlabel("Tháng")
plt.ylabel("Nhiệt độ trung bình (Celsius)")
plt.grid(True)
plt.xticks(rotation=45)
plt.show()
```
**Nguyên lý hoạt động:**
- Trích xuất thông tin tháng từ cột `datetime`.
- Tính toán nhiệt độ trung bình theo từng tháng.
- Vẽ biểu đồ đường để thể hiện xu hướng nhiệt độ trung bình theo thời gian.

![image](https://github.com/user-attachments/assets/5f7fba9e-8325-4d70-a815-c51deadee453)




