class PaymentKernel:

    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name: str, plugin):
        self.plugins[name] = plugin

    def process_payment(self, method: str, data: dict) -> bool:
        if method not in self.plugins:
            raise Exception("Método de pago no soportado")
        if data["amount"] <= 0:
            return False
        print(f"Procesando pago con: {method}")
        return self.plugins[method].authenticate(data)
        

