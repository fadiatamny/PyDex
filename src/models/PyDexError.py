class PyDexError(Exception):
    def __init__(self, message: str, status_code: int = 500):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)