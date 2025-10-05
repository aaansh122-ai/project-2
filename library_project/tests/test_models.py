from library.models import PrintedBook, EBook

def test_printedbook_late_fee():
    pb = PrintedBook("111", "Printed", "Author", copies=2)
    assert pb.calculate_late_fee(3) == 1.5

def test_ebook_late_fee():
    eb = EBook("222", "E-Book", "Author")
    assert eb.calculate_late_fee(5) == 1.0
