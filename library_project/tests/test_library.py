from datetime import timedelta
from library.models import PrintedBook
from library.library_system import Library
from library.payments import CardPaymentProcessor

def test_checkout_and_return():
    lib = Library()
    pb = PrintedBook("333", "Title", "Author", copies=1)
    lib.add_book(pb)
    rec = lib.checkout("333", "user1", loan_days=1)
    late_return = rec.due_date + timedelta(days=2)
    card_proc = CardPaymentProcessor("m1")
    fee = lib.return_book("333", "user1", return_date=late_return, payment_processor=card_proc, payment_details={"card_number": "1234"})
    assert fee == pb.calculate_late_fee(2)
