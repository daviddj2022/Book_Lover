import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self): 
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_name = "War of the Worlds"
        test_object.add_book(book_name, 4)
        
        name_list = test_object.book_list['book_name'].tolist()
        test_value = (book_name in name_list)
        message = "The book is not in the list"
        self.assertTrue(test_value, message)

    def test_2_add_book(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_name = "War of the Worlds"
        test_object.add_book(book_name, 4)
        test_object.add_book(book_name, 4)
        
        test_value = len(test_object.book_list)
        expected = 1
        message = "The test value is not equal to the expected value"
        self.assertEqual(test_value, expected, message)

    def test_3_has_read(self): 
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_name = "War of the Worlds"
        test_object.add_book(book_name, 4)
        
        test_value = test_object.has_read(book_name)
        message = "The test value is False"
        self.assertTrue(test_value, message)

    def test_4_has_read(self): 
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_name = "War of the Worlds"
        test_object.add_book(book_name, 4)
        other_book = "The Great Gatsby"
        
        test_value = test_object.has_read(other_book)
        message = "The test value is True"
        self.assertFalse(test_value, message)

    def test_5_num_books_read(self): 
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("The Great Gatsby", 5)
        test_object.add_book("Quitting is Great", 0)
        test_object.add_book("Great Expectations", 4)
        test_object.add_book("Something Fun", 2)
        
        test_value = test_object.num_books_read()
        expected = 5
        message = "The test value is not equal to the expected value"
        self.assertEqual(test_value, expected, message)

    def test_6_fav_books(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("The Great Gatsby", 5)
        test_object.add_book("Quitting is Great", 0)
        test_object.add_book("Great Expectations", 4)
        test_object.add_book("Something Fun", 2)
        
        test_value = len(test_object.fav_books().book_rating)
        expected = 3
        message = "The test value is not equal to the expected value"
        self.assertEqual(test_value, expected, message)

if __name__ == '__main__':

    unittest.main(verbosity=3)