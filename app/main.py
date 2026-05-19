from fastapi import FastAPI

from app.routers import auth, employees

app = FastAPI()

app.include_router(auth.router)
app.include_router(employees.router)


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}
