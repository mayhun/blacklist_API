from pydantic import BaseModel, HttpUrl

"""
URL Check Requests 정의
"""
class URLCheckRequest(BaseModel):
    url: HttpUrl
