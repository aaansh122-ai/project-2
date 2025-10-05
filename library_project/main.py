from library.models import PrintedBook, EBook
from library.library_system import Library
from library.payments import CardPaymentProcessor
from datetime import timedelta

def demo():
    lib = Library()
    pb = PrintedBook("isbn-0001", "Python 101", "A. Dev", 2)
    eb = EBook("isbn-0002", "E-Python", "A. Dev")
    lib.add_book(pb); lib.add_book(eb)
    rec = lib.checkout("isbn-0001", "alice", 7)
    late_date = rec.due_date + timedelta(days=4)
    processor = CardPaymentProcessor("merchant-xyz")
    fee = lib.return_book("isbn-0001", "alice", return_date=late_date, payment_processor=processor, payment_details={"card_number": "4242424242424242"})
    print("Late fee charged:", fee)

if __name__ == "__main__": demo()
