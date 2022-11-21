from exceptions.main_exceptions import ServiceException

class CompanyException(ServiceException):
    
    def __init__(self, message, status):
        self.message = message
        self.status = 500 if status is None else status
        super().__init__(message)