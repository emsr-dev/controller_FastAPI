from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse

from .components import volume_router, play_router

app = FastAPI()

origins = ['https://buben.bavamoor.net']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST'],
    allow_headers=["*"]
)


app.include_router(volume_router)
app.include_router(play_router)


@app.get('/')
async def root():
    return FileResponse('src/web/templates/root.html')
