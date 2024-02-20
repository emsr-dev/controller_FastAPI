from fastapi import APIRouter
from starlette.responses import FileResponse

root_router = APIRouter()


@root_router.get('/')
def root_request():
    return FileResponse('src/web/templates/root.html')
