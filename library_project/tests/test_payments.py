from library.payments import CardPaymentProcessor, PaypalPaymentProcessor

def test_card_payment_success():
    card_proc = CardPaymentProcessor("m1")
    assert card_proc.pay(10.0, {"card_number": "4242424242424242"})

def test_paypal_failure():
    paypal = PaypalPaymentProcessor("c1")
    assert not paypal.pay(5.0, {})
