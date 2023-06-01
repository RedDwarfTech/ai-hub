class TooMuchFaceException(Exception):
    def __init__(self):
        self.message = f"too much face"
        super().__init__(self.message)