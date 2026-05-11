from core.interfaces import PaymentAuthenticator

class CardAuthenticator(PaymentAuthenticator):

    def authenticate(self, data: dict) -> bool:
        card_number = data.get("card_number", "")
        return card_number.startswith("4")  # simulación
