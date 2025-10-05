from datetime import datetime, timedelta
from typing import List, Optional
from .models import Book
from .payments import PaymentProcessor

class BorrowRecord:
    def __init__(self, book_isbn, user_id, borrowed_date, due_date):
        self.book_isbn = book_isbn
        self.user_id = user_id
        self.borrowed_date = borrowed_date
        self.due_date = due_date
        self.returned_date = None
        self.fee_paid = 0.0

    def days_late(self, at_date=None):
        actual = self.returned_date or (at_date or datetime.utcnow())
        return max(0, (actual.date() - self.due_date.date()).days)


class Library:
    def __init__(self):
        self._inventory = {}
        self._borrowed_records: List[BorrowRecord] = []

    def add_book(self, book: Book): self._inventory[book.isbn] = book
    def get_book(self, isbn): return self._inventory.get(isbn)

    def checkout(self, isbn, user_id, loan_days=14):
        book = self.get_book(isbn)
        if not book: raise ValueError("Book not found")
        if book.copies <= 0: raise ValueError("No copies available")
        book.remove_copy()
        rec = BorrowRecord(isbn, user_id, datetime.utcnow(), datetime.utcnow() + timedelta(days=loan_days))
        self._borrowed_records.append(rec)
        return rec

    def return_book(self, isbn, user_id, return_date=None, payment_processor=None, payment_details=None):
        record = next((r for r in self._borrowed_records if r.book_isbn == isbn and r.user_id == user_id and r.returned_date is None), None)
        if not record: raise ValueError("Borrow record not found")
        record.returned_date = return_date or datetime.utcnow()
        book = self.get_book(isbn)
        days_late = record.days_late(record.returned_date)
        fee = book.calculate_late_fee(days_late)
        if fee > 0 and payment_processor:
            if not payment_processor.pay(fee, payment_details or {}):
                raise RuntimeError("Payment failed")
            record.fee_paid = fee
        book.return_copy()
        return fee
