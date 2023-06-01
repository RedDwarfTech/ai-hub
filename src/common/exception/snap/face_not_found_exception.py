class FaceNotFoundException(Exception):
    def __init__(self):
        self.message = f"face not found"
        super().__init__(self.message)