# Disease 2016 — Phân tích & dự đoán thời gian điều trị

## Bài toán

Dữ liệu là **số liệu chi phí điều trị năm 2016** (`data/raw/SoLieuCPDieuTri2016.xlsx`,
~68.000 lượt khám/điều trị, chủ yếu ở Bình Định). Mỗi dòng gồm thông tin bệnh nhân
(năm sinh, dân tộc, địa chỉ), chẩn đoán (mã ICD-10), ngày vào/ra, tổng chi phí và phần
BHYT thanh toán.

Mục tiêu: từ đặc trưng nhân khẩu học, địa lý và nhóm bệnh (ICD), **dự đoán thời gian
điều trị** của bệnh nhân — vừa ở dạng hồi quy (số ngày), vừa ở dạng phân loại
(Ngắn / Trung bình / Dài) có xử lý mất cân bằng lớp bằng SMOTE.

Quy trình được tách thành 4 notebook chạy tuần tự, truyền dữ liệu qua thư mục
`data/processed/`:

| Notebook | Nhiệm vụ | Input | Output |
|---|---|---|---|
| `01_cleaning.ipynb` | Làm sạch dữ liệu: bỏ cột thừa, sửa giá trị lỗi, tạo cột Tuổi, chuẩn hóa địa danh | `data/raw/*.xlsx` | `data/processed/01_cleaned.pkl` |
| `02_feature_engineering.ipynb` | Tạo Vùng miền, gom nhóm dân tộc, **geocode địa chỉ qua API**, mã hóa nhóm bệnh ICD | `01_cleaned.pkl` | `data/processed/model_df.{pkl,csv}` |
| `03_eda.ipynb` | Trực quan hóa phân bố thời gian điều trị và vị trí địa lý | `model_df.pkl` | (biểu đồ) |
| `04_modeling.ipynb` | Huấn luyện & đánh giá mô hình (Linear / RandomForest + SMOTE) | `model_df.pkl` | (kết quả) |

Các đường dẫn, seed ngẫu nhiên và tham số geocoding được tập trung trong
[`config.py`](config.py).

## Cách chạy

### 1. Tạo môi trường ảo và cài thư viện

```bash
python -m venv venv
venv\Scripts\activate          # Windows (PowerShell/CMD)
# source venv/bin/activate     # macOS/Linux
pip install -r requirements.txt
```

### 2. Chọn kernel

Mở notebook trong VS Code / Jupyter và chọn kernel **"Python (Dieu Tri venv)"**
(hoặc trỏ tới `venv/Scripts/python.exe`). Các notebook đã gắn sẵn kernel này.

### 3. Chạy notebook theo thứ tự

Chạy lần lượt `01` → `02` → `03` / `04`. Mỗi notebook tự nạp dữ liệu từ bước trước
nên cần chạy đúng thứ tự ít nhất một lần.

> ⚠️ **Notebook 02** geocode địa chỉ trực tiếp qua API Nominatim (OpenStreetMap),
> giới hạn ~1 request/giây nên mất **~20 phút**. Chạy xong, các file
> `data/processed/model_df.*` được lưu lại để `03`/`04` dùng mà không phải geocode lại.
