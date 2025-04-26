class Library:
    book_list = []

    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)

class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability
        Library.entry_book(self)

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"Book: '{self.__title}' borrowed successfully")
        else:
            print(f"Sorry! book: '{self.__title}' is not available")

    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"Book: '{self.__title}' returned successfully")
        else:
            print(f"Book: '{self.__title}' is not borrowed")

    def view_book_info(self):
        status = "Available" if self.__availability else "Not available"
        print(
            f"ID: {self.__book_id}, Title: '{self.__title}', Author: {self.__author}, Status: {status}")


Book(101, "Python", "Karim")
Book(102, "Java", "Rahim Khan")
Book(103, "C++", "Sabbir Aalom")
Book(104, "Bangla", "Promoth Chowdhury")
Book(105, "English", "Shakespare")
Book(106, "Deyal", "Humayun Ahmed")
Book(107, "Pother Pechaly", "Vibutivushon")
Book(108, "Shesher kobita", "Rabindranath Tagor")
Book(109, "Samyabadi", "Kazi Nazrul")

while True:
    print('\n--------Welcome to the Library---------')
    print('1. View all books')
    print('2. Borrow Book')
    print('3. Return Book')
    print('4. Exit')

    option = input('Enter your choice from number 1 to 4:')
    books = Library.book_list
    if option == "1":
        print('\nLibrary books:')
        for book in books:
            book.view_book_info()
    elif option == "2":
        book_id = int(input('Enter book id to borrow:'))
        flag = True
        for book in books:
            if book._Book__book_id == book_id:
                book.borrow_book()
                flag = False
        if flag:
            print('Book with this ID does not exist.')
    elif option == "3":
        book_id = int(input('Enter book id to return:'))
        flag = True
        for book in books:
            if book._Book__book_id == book_id:
                book.return_book()
                flag = False
        if flag:
            print('Book with this ID does not exist.')
    elif option == "4":
        break
    else:
        print('Chosed wrong option, Enter a number between 1 to 4')
