import pandas as pd

class BookLover:
    """This is a BookLover class.""" 
    # constructor
    def __init__(self, name, email, fav_genre, num_books = 0, 
                 book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        #Assert statements to ensure parameter types are correct
        assert isinstance(name, str), "Name must be a string"
        assert isinstance(email, str), "Email must be a string"
        assert isinstance(fav_genre, str), "Favorite genre must be a string"
        assert isinstance(num_books, int), "Number of books must be an integer"
        assert isinstance(book_list, pd.DataFrame), "Book list must be a pandas dataframe"
        
        #Assert statements to ensure the book lover's input dataframe is correctly constructed
        assert len(book_list.columns) == 2, "The dataframe must only have two columns"
        assert book_list.columns[0] == 'book_name', "First column must be titled 'book_name'"
        assert book_list.columns[1] == 'book_rating', "Second column must be titled 'book_rating'"
        
        
        self.name = name # string type
        self.email = email # string type
        self.fav_genre = fav_genre # string type
        self.num_books = num_books # integer type
        self.book_list = book_list
        
        
    # adds a book to the book list
    def add_book(self, book_name, rating):
        assert isinstance(book_name, str), "Book name must be a string"
        assert isinstance(rating, int), "Rating must be an integer"
        assert (rating >= 0 and rating <= 5), "Rating must be between 0 and 5"
        name_list = self.book_list['book_name'].tolist()
        if book_name not in name_list:
            self.num_books += 1
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        else:
            print('This book already exists in the book list!')
        
    # checks to see if the book lover has already read a certain book or not
    def has_read(self, book_name):
        assert isinstance(book_name, str), "Book name must be a string"
        name_list = self.book_list['book_name'].tolist()
        if book_name in name_list:
            return True
        else:
            return False
    
    # tells us the number of books the book lover has read
    def num_books_read(self):
        return self.num_books
    
    # returns a filtered dataframe of the book lover's most favorite books
    def fav_books(self):
        return self.book_list[self.book_list.book_rating > 3]