from fastapi import Depends, FastAPI
import uvicorn
from src.common.exception.snap.face_not_found_exception import FaceNotFoundException
from src.common.exception.snap.too_much_face_exception import TooMuchFaceException
from src.common.exception.snap_exception_handler import face_not_found_exception_handler, too_much_face_exception_handler
from src.common.dependency import has_access
from src.routers import users,chat
from src.routers.images import images
from src.routers.common.health import health_check

app = FastAPI()

PROTECTED = [Depends(has_access)]

app.include_router(
    users.router,
    dependencies=PROTECTED
)
app.include_router(
    chat.router,
    dependencies=PROTECTED
)
app.include_router(
    images.router,
    dependencies=PROTECTED
)
app.include_router(
    health_check.router
)

app.add_exception_handler(TooMuchFaceException,too_much_face_exception_handler)
app.add_exception_handler(FaceNotFoundException, face_not_found_exception_handler)
