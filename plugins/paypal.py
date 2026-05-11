from core.interfaces import PaymentAuthenticator

class PayPalAuthenticator(PaymentAuthenticator):

    def authenticate(self, data: dict) -> bool:
        email = data.get("email", "")
        return email.endswith("@paypal.com")  # simulación
