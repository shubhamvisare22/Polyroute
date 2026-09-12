from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Polyroute")
app.include_router(router=router)

