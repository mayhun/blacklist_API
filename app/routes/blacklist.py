from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import func, or_, and_
from app.db.database import get_db
from app.models.blacklist import MalUrls
from app.schemas.blacklist import URLCheckRequest
import time
from tldextract import extract

router = APIRouter()

@router.post("/check")
async def check_blacklist(request: URLCheckRequest, db: AsyncSession = Depends(get_db)):
    start = time.time()
    url = str(request.url)

    # 도메인 추출
    extracted = extract(url)
    domain = f"{extracted.domain}.{extracted.suffix}"

    # 쿼리 작성
    stmt = select(MalUrls).where(
        or_(
            and_(  # 정확히 일치하는 경우
                MalUrls.url_crc == func.CRC32(url),
                MalUrls.url == url
            ),
            MalUrls.url.like(f"%{domain}%")  # 도메인이 포함된 경우
        )
    )
    result = await db.execute(stmt)
    entries = result.scalars().all()

    # 결과 처리
    status = "normal"
    source = None
    for entry in entries:
        if entry.url == url:    # 정확히 일치하면 malware
            status = "malware"
            source = entry.source
            break  
        elif domain in entry.url: # 도에인이 일치시 suspect
            status = "suspect"
            source = entry.source

    tt = time.time() - start
    return {
        "status": status,
        "time": tt,
        "source": source
    }
