# Sử dụng Python 3.10
FROM python:3.10

# Đặt thư mục làm việc
WORKDIR /app

# Copy file vào container
COPY . .

# Cài đặt thư viện
RUN pip install --no-cache-dir -r requirements.txt

# Chạy ứng dụng
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]