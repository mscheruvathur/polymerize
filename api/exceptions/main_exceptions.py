class ServiceException(Exception):
    
    def __init__(self, message, status=400):
        self.message = message
        self.status = 500 if status is None else status
        super().__init__()