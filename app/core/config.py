import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

# 환경 변수
load_dotenv()
"""
DB 연결
"""
class Settings:
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: int = int(os.getenv("DB_PORT", 3306))
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = quote_plus(os.getenv("DB_PASSWORD"))
    DB_NAME: str = os.getenv("DB_NAME")

    SQLALCHEMY_DATABASE_URL = (
        f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


settings = Settings()
