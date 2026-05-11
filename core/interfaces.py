from abc import ABC, abstractmethod

class PaymentAuthenticator(ABC):

    @abstractmethod
    def authenticate(self, data: dict) -> bool:
        pass

