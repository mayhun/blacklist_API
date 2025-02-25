from fastapi import FastAPI
from app.routes import blacklist


app = FastAPI(title="Black List Check")

@app.get("/")
def root():
    return {"message": "BE-SVC"}

# router setting
app.include_router(blacklist.router, prefix="/blacklist", tags=["Blacklist"])