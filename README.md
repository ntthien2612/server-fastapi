# FastAPI Project

This is a FastAPI project with the following structure:

- **app/**: Main source code.
- **tests/**: Test cases.
- **docker/**: Docker configuration.
- **scripts/**: Helper scripts.
- **.env**: Environment variables.
- **requirements.txt**: Python dependencies.

## How to run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

1️⃣ Build và chạy container

docker-compose up --build

Chạy lệnh sau để dừng và xóa container:
docker-compose down

1️⃣ restart container

docker-compose up --build -d

Xóa images, volumes, networks (nếu cần):
docker rmi $(docker images -q) && docker volume rm $(docker volume ls -q) && docker network prune -f