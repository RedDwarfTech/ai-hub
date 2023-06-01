
import json
from src.models.chat.rest_response import RestResponse
from src.common.exception.snap.too_much_face_exception import TooMuchFaceException
from src.models.snap.photo.upload_response import SnapResponse
from src.common.exception.snap.face_not_found_exception import FaceNotFoundException
from fastapi.responses import JSONResponse


async def face_not_found_exception_handler(request, exc):
    resp = SnapResponse("")
    resp.statusCode = "200"
    resp.resultCode = "SNAP_FACE_NOT_FOUND"
    return resp


async def too_much_face_exception_handler(request, exc):
    resp = RestResponse(msg = "未识别到人脸",result="",resultCode="TOO_MUCH_FACE")
    return JSONResponse(content=resp.to_dict(), status_code = 200)
