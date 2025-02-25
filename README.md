# 🚀 FastAPI Blacklist Check Service

이 프로젝트는 **FastAPI**로 개발된 웹 백엔드 서비스입니다.  
현재 기능은 주로 **URL 블랙리스트 확인**에 중점을 두고 있으며, 추후에 **회원가입 및 로그인 기능**이 추가될 예정입니다.

---

## 📌 **기능**

- ✅ **블랙리스트 확인**  
  제출된 URL이 블랙리스트에 등록되어 있는지 확인합니다.

- ✅ **비동기 처리**  
  동시 요청 100건 이상을 빠르게 처리할 수 있도록 최적화되었습니다.


- 🚧 **회원가입 및 로그인** (추후 개발 예정)

---

## ⚙️ **기술 스택**

- **Backend Framework**: FastAPI
- **Database**: MySQL (SQLAlchemy + AsyncMySQL)
- **Asynchronous Handling**: Aiohttp, Asyncio
- **Containerization**: Docker, Docker Compose

---

## 📂 **프로젝트 구조**

```
BE-SVC/ 
├── app/ 
│ ├── core/ 
│ │ └── config.py # 설정 파일 
│ ├── db/ 
│ │ └── database.py # 데이터베이스 연결 설정 
│ ├── models/ 
│ │ └── blacklist.py # 데이터베이스 모델 정의 
│ ├── routes/ 
│ │ └── blacklist.py # 블랙리스트 관련 라우터 
│ ├── schemas/ 
│ │ └── blacklist.py # 블랙리스트 요청 및 응답 스키마 
│ └── main.py # 메인 스키마 정의 
│ 
├── .env # 환경 변수 파일 
├── .gitignore # Git 관리에서 제외할 파일 목록 
├── docker-compose.yml # Docker Compose 설정 파일 
├── Dockerfile # Docker 설정 파일 
├── README.md # 프로젝트 설명서 
└── requirements.txt # 필요한 Python 패키지 목록

```

## 🔑 **환경 변수 (.env 파일 설정)**

애플리케이션 실행을 위해 다음 환경 변수를 설정해야 합니다:
```bash
DB_HOST=localhost 
DB_PORT=3306
DB_USER={user}
DB_PASSWORD={DB_PASSWORD}
DB_NAME={DB_NAME}
```

## 🛠️ **API 엔드포인트**
### 🔍 1. URL 블랙리스트 확인
- Endpoint: POST /blacklist/check
- 요청 데이터 형식:
```json
{
  "url": "https://example.com/test-url"
}
```
- 응답 데이터 형식
```json
{
  "is_blacklisted": "malware",
  "time": 0.0123,  # 요청 처리 시간 (초 단위)
  "source": "Noladefense"
}
```
## 📌 **추후 개발 예정 기능**

### 🔒 회원가입 및 로그인 기능 (JWT 기반 인증)
### 📊 블랙리스트 통계 대시보드