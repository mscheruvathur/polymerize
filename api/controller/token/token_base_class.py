from abc import ABC, abstractmethod

class TokenBaseClass(ABC):

    @abstractmethod
    def generate_access_token(self, user):
        pass


    @abstractmethod
    def generate_refresh_token(self, key):
        pass


    @abstractmethod
    def generate_tokens(self, user):
        pass


    @abstractmethod
    def create_tokens(self, user):
        pass