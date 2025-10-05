from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float, details: dict) -> bool: pass


class CardPaymentProcessor(PaymentProcessor):
    def __init__(self, merchant_id: str): self.merchant_id = merchant_id
    def pay(self, amount: float, details: dict) -> bool:
        card = details.get("card_number")
        if not card: return False
        print(f"[CardPayment] Charging ${amount:.2f} to card ending {card[-4:]}")
        return True


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, client_id: str): self.client_id = client_id
    def pay(self, amount: float, details: dict) -> bool:
        email = details.get("paypal_email")
        if not email: return False
        print(f"[PayPal] Charging ${amount:.2f} to PayPal account {email}")
        return True
