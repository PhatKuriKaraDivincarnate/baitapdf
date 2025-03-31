import kaggle

# 📌 Định nghĩa dataset cần tải
dataset = "selfishgene/historical-hourly-weather-data"  # ID của dataset trên Kaggle
save_path = "data/"  # Thư mục lưu dữ liệu

# 📌 Tải dataset về
print("🚀 Đang tải dữ liệu từ Kaggle...")
kaggle.api.dataset_download_files(dataset, path=save_path, unzip=True)

print("✅ Dữ liệu đã được tải về thư mục:", save_path)
