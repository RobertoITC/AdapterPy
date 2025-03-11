from abc import ABC, abstractmethod

class PayPalService:
    def send_payment(self, amount: float):
        print(f"Sending payment of amount: {amount} to PayPal")

class StripeService:
    def make_charge(self, amount: float):
        print(f"Sending payment of amount: {amount} to Stripe")

class MercadoPagoService:
    def pay(self, amount: float):
        print(f"Sending payment of amount: {amount} to MercadoPago")


# Interfaz de pago

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

# Clases adaptadoras
class PayPalAdapter(PaymentProcessor):
    def __init__(self, service: PayPalService):
        self.paypal_service = service

    def process_payment(self, amount):
        self.paypal_service.send_payment(amount)


class StripeAdapter(PaymentProcessor):
    def __init__(self, service: StripeService):
        self.stripe_service = service

    def process_payment(self, amount):
        self.stripe_service.make_charge(amount)

class MercadoPagoAdapter(PaymentProcessor):
    def __init__(self, service: MercadoPagoService):
        self.mercadopago_service = service

    def process_payment(self, amount):
        self.mercadopago_service.pay(amount)


def main():
    payment_amount     = 100
    paypal_processor   = PayPalAdapter(PayPalService())
    print('Using PayPal...')
    paypal_processor.process_payment(payment_amount)

    payment_amount = 175
    stripe_processor = StripeAdapter(StripeService())
    print('Using Stripe...')
    stripe_processor.process_payment(payment_amount)

    payment_amount = 250
    mercadopago_processor = MercadoPagoAdapter(MercadoPagoService())
    print('Using MercadoPago...')
    mercadopago_processor.process_payment(payment_amount)

if __name__ == '__main__':
    main()

