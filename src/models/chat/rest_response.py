class RestResponse:
    def __init__(self, msg="", result=None, resultCode="200", statusCode="200"):
        self.msg = msg
        self.result = result if result else {}
        self.resultCode = resultCode
        self.statusCode = statusCode

    def to_dict(self):
        return {
            "msg": self.msg,
            "result": self.result,
            "resultCode": self.resultCode,
            "statusCode": self.statusCode
        }