from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import learning_path, progress
from routers import auth

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount routers
app.include_router(learning_path.router)
app.include_router(progress.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Backend running successfully 🚀"}
