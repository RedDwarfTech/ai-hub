
from src.models.chat.rest_response import RestResponse


class SnapResponse(RestResponse):
    def __init__(self, result=None, resultCode="200"):
        super().__init__(result=result, resultCode=resultCode)

    def to_dict(self):
        return {
            "upload": self.uploaded
        }