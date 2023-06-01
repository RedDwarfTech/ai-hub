import json
import uuid
import cv2
import os
import sys

from src.common.exception.snap.face_not_found_exception import FaceNotFoundException
from src.common.exception.snap.too_much_face_exception import TooMuchFaceException


def recognize_face(file_full_path: str, params: str):
    # https://stackoverflow.com/questions/75958707/is-it-possible-to-get-the-project-root-dir-in-python-fastapi-app
    root_path = os.path.abspath(os.path.dirname(__file__))
    config_path = root_path + "/haarcascade_frontalface_default.xml"
    # 实例化人脸分类器
    face_cascade = cv2.CascadeClassifier(config_path)  # xml来源于资源文件。
    # 读取测试图片
    img = cv2.imread(file_full_path, cv2.IMREAD_COLOR)
    # 将原彩色图转换成灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 开始在灰度图上检测人脸，输出是人脸区域的外接矩形框
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=1)
    
    
    # 遍历人脸检测结果
    for (x, y, w, h) in faces:
        # 计算扩展后的裁剪区域范围
        x = max(x - int(0.5 * w), 0)
        y = max(y - int(0.5 * h), 0)
        w = min(x + w + int(0.5 * w), img.shape[1])
        h = min(y + h + int(0.5 * h), img.shape[0])

        # Limit the values to the boundaries of the image
        x = max(x, 0)
        y = max(y, 0)
        w = min(w, img.shape[1]-x)
        h = min(h, img.shape[0]-y)

        # 在原彩色图上画人脸矩形框
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
    face_count = len(faces)
    if face_count == 0:
        raise FaceNotFoundException()
    if face_count > 1:
        raise TooMuchFaceException()
    # 选择正确且最接近屏幕中心的人脸
    if(len(faces)) > 0:
        best_face = faces[0]
        best_face_distance = abs((best_face[0]+best_face[2]/2)-img.shape[1]/2)
        for face in faces:
            distance = abs((face[0]+face[2]/2)-img.shape[1]/2)
            if distance < best_face_distance:
                best_face = face
                best_face_distance = distance
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # 剪切人脸区域
        x, y, w, h = best_face

        # 计算扩展后的裁剪区域范围
        x = max(x - int(0.5 * w), 0)
        y = max(y - int(0.5 * h), 0)
        w = min(x + w + int(0.5 * w), img.shape[1])
        h = min(y + h + int(0.5 * h), img.shape[0])

        # Limit the values to the boundaries of the image
        x = max(x, 0)
        y = max(y, 0)
        w = min(w, img.shape[1]-x)
        h = min(h, img.shape[0]-y)

        face_img = img[y:y+h, x:x+w]
        params_obj = json.loads(params)
        # 调整头像大小到合适的证件照尺寸
        face_img = cv2.resize(face_img, (params_obj['width'], params_obj['height']))
        crop_path = '/opt/snap/photo/crop/'
        crop_full_path = crop_path + str(uuid.uuid4()) + ".jpg"
        # 保存头像到单独的文件中
        cv2.imwrite(crop_full_path, face_img)
        return crop_full_path
