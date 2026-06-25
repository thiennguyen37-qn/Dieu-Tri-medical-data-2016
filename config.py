"""Cấu hình dùng chung cho các notebook của dự án Disease 2016.

Tập trung các đường dẫn dữ liệu, seed ngẫu nhiên và tham số geocoding vào một nơi
để các notebook (01 -> 04) cùng tham chiếu, tránh hard-code lặp lại.
"""
from pathlib import Path

# Thư mục gốc của dự án (nơi chứa file config.py này)
ROOT = Path(__file__).resolve().parent

# ----- Dữ liệu -----
DATA_DIR = ROOT / "data"
RAW_XLSX = DATA_DIR / "raw" / "SoLieuCPDieuTri2016.xlsx"   # dữ liệu gốc
PROCESSED_DIR = DATA_DIR / "processed"
CLEANED_PKL = PROCESSED_DIR / "01_cleaned.pkl"             # output của notebook 01
MODEL_DF_PKL = PROCESSED_DIR / "model_df.pkl"              # output của notebook 02
MODEL_DF_CSV = PROCESSED_DIR / "model_df.csv"

# ----- Tái lập kết quả -----
RANDOM_SEED = 42

# ----- Geocoding (Nominatim / OpenStreetMap) -----
GEOCODER_USER_AGENT = "disease-2016-geocoder"
GEOCODER_MIN_DELAY = 1.1    # số giây tối thiểu giữa 2 request (tuân thủ giới hạn Nominatim)
GEOCODER_TIMEOUT = 10       # số giây chờ phản hồi mỗi request (mặc định geopy chỉ 1s -> hay timeout)
GEOCODER_MAX_RETRIES = 3    # số lần thử lại khi gặp lỗi mạng tạm thời
