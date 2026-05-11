from core.interfaces import PaymentAuthenticator

class BankTransferAuthenticator(PaymentAuthenticator):
    def authenticate(self, data):
        return data.get("reference") is not None
