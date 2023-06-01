
from src.models.chat.rest_response import RestResponse


class TextResponse(RestResponse):
    def __init__(self, uploaded=''):
        super().__init__(result=uploaded)
