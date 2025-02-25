from sqlalchemy import Column, Integer, String, DateTime
from app.db.database import Base

"""
MySQL 테이블 정의
"""

class MalUrls(Base):
    __tablename__ = "mal_urls"

    mal_id = Column(Integer, primary_key=True, autoincrement=True)  # id
    url = Column(String(2083), nullable=False)                      # URL
    url_crc = Column(Integer, nullable=True)                        # URL CRC32
    source = Column(String(255))                                    # 수집 출처
    create_dt = Column(DateTime)                                    # 수집 시간