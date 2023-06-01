from typing import Optional
from pydantic import BaseModel

class CropParams(BaseModel):
    # 是否自动裁剪
    crop: str
    # 图片的宽度
    # width: Optional[int]
    # 图片的高度
    # height: Optional[int]
    # 类型：结婚照、驾照、四六级等等
    #type: Optional[str]

