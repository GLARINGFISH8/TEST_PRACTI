def is_palindrome(s):
    if not(isinstance(s, str)):
        raise TypeError

    return s == s[::-1]


def average(lst):
    if not(isinstance(lst, list)):
        raise TypeError

    for i in lst:
        if not(isinstance(i, int) or isinstance(i, float)) or i == True or i == False:
            raise TypeError


    if not lst:
        raise ValueError("List is empty")
    return round(sum(lst) / len(lst), 2)



class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if not(isinstance(amount, int) or isinstance(amount, float)):
            raise TypeError
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance



# Рефакторинг
class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book not in self.books:
            self.books[book] = 1
        else:
            self.books[book] += 1

    def remove_book(self, book):
        if book in self.books:
            self.books[book] -= 1
            if self.books[book] == 0:
                del self.books[book]
        else:
            print("Book not found")

    def find_book(self, book):
        return self.books.get(book, 0) > 0

# Легаси код для тестов
import unittest

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        self.library.add_book("Book A")
        self.assertTrue(self.library.find_book("Book A"))
        self.assertFalse(self.library.find_book("Book B"))

    def test_remove_book(self):
        self.library.add_book("Book A")
        self.library.add_book("Book A")
        self.library.remove_book("Book A")
        self.assertTrue(self.library.find_book("Book A"))
        self.library.remove_book("Book A")
        self.assertFalse(self.library.find_book("Book A"))
        self.library.add_book("Book B")
        self.library.remove_book("Book B")

    def test_find_book(self):
        self.library.add_book("Book A")
        self.assertTrue(self.library.find_book("Book A"))
        self.library.remove_book("Book A")
        self.assertFalse(self.library.find_book("Book A"))

if __name__ == '__main__':
    unittest.main()
