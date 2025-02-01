from fastapi import FastAPI
from app.routes import users, items

app = FastAPI(title="My Python Web API")

# Include route files (like MapControllers)
app.include_router(users.router)
app.include_router(items.router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to My Python API"}
