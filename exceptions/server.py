class DatabaseConnectionError(Exception):
    def __init__(self, host: str, port: int):
        super().__init__()
        self.host = host
        self.port = port

    def __str__(self):
        return f"Error connecting to Database host: {self.host}, port: {self.port}"
