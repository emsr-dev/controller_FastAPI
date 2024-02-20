from fastapi import FastAPI
from .components import root_router, volume_router, play_router

app = FastAPI()

app.include_router(root_router)
app.include_router(volume_router)
app.include_router(play_router)
