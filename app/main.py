from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import task_router, auth_router  # Import các router của API
from app.core.database import Base, engine  # Kết nối DB

# Khởi tạo bảng nếu chưa tồn tại
Base.metadata.create_all(bind=engine)

# Khởi tạo ứng dụng FastAPI
app = FastAPI(
    title="Task Management API",
    description="A simple FastAPI Task Manager with MySQL & Alembic",
    version="1.0.0"
)

# Cấu hình CORS (cho phép frontend truy cập API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Chấp nhận tất cả domain (chỉnh sửa nếu cần)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Đăng ký các router
app.include_router(task_router.router, prefix="/api/tasks", tags=["Tasks"])
app.include_router(auth_router.router, prefix="/api/auth", tags=["Auth"])