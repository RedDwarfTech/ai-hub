import uuid

from fastapi import UploadFile

from src.orm.mapper.snap_files import SnapFiles
import rembg
from PIL import Image, ImageDraw, ImageFont

from src.tool.graphics.recognize import recognize_face


class ProcessSnap():

    def recognize_face(self):
        pass

    def remove_background(self, file_full_path: str):
        img = Image.open(file_full_path)
        output = rembg.remove(img)
        back_remove_folder = '/opt/snap/photo/rembg/'
        full_path = back_remove_folder + str(uuid.uuid4()) + ".png"
        output.save(full_path)
        return full_path

    def fill_background(self, bg_removed_path: str):
        # 打开人像图片
        image = Image.open(bg_removed_path)
        # 创建一个同样大小的纯色图片
        background = Image.new('RGBA', image.size, color=(255, 0, 0, 255))
        # 将人像图片粘贴到背景图片上
        background.paste(image, (0, 0), image)
        complete_path = '/opt/snap/photo/dist/'
        complete_full_path = complete_path + str(uuid.uuid4()) + ".png"
        # 保存图片
        background.save(complete_full_path)
        return complete_full_path

    def add_watermark(self, file_full_path: str):
        # 打开图片
        img = Image.open(file_full_path)
        # 在图片上绘制水印
        draw = ImageDraw.Draw(img)
        text = "watermark"
        font = ImageFont.truetype('/System/Library/Fonts/SFNS.ttf', size=20)
        draw.text((img.width - img.width/1.15, img.height - img.height/3.2), text,font=font, fill=(255, 255, 255, 128))
        watermark_path = '/opt/snap/photo/stamp/'
        watermark_full_path = watermark_path + str(uuid.uuid4()) + ".png"
        # 保存图片
        img.save(watermark_full_path)
        return watermark_full_path

    def generate_result(self):
        pass

    def process_image(self,img_full_path:str, file: UploadFile, params: str):
        crop_full_path = recognize_face(img_full_path,params)
        bg_removed_path = self.remove_background(crop_full_path)
        complete_path = self.fill_background(bg_removed_path)
        watermark_path = self.add_watermark(bg_removed_path)
        snap_file = SnapFiles()
        snap_files = snap_file.insert_snap_files(file.filename,complete_path,watermark_path)
        return snap_files
