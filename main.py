from core.Kernel import PaymentKernel
from plugins.card import CardAuthenticator
from plugins.paypal import PayPalAuthenticator
from plugins.banktransfer import BankTransferAuthenticator

class PaymentService:

    def __init__(self):
        self.kernel = PaymentKernel()
        self._load_plugins()

    def _load_plugins(self):
        self.kernel.register_plugin("card", CardAuthenticator())
        self.kernel.register_plugin("paypal", PayPalAuthenticator())
        self.kernel.register_plugin("bank_transfer", BankTransferAuthenticator())
        
    def authenticate(self, method: str, data: dict) -> bool:
        return self.kernel.authenticate_payment(method, data)
