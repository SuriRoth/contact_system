class Book:
    def __init__(self, title, author, ISBN, copies):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.copies = copies
        
    def __str__(self):
        return f"'{self.title}' by {self.author}, ISBN is {self.ISBN}, {self.copies} copies"
    
    def __repr__(self):
        return f'Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Copies: {self.copies} '
    

class Member:
    def __init__(self, name, memberID, borrowedBooks):
        self.name = name 
        self.memberID = memberID
        self.borrowedBooks = borrowedBooks
        
    def __str__(self):
        return f'{self.name} with a member ID of {self.memberID}, borrowed {self.borrowedBooks}.'
    
    def __repr__(self):
        return f'Name: {self.name}, Member ID: {self.memberID}, Borrowed Books: {self.borrowedBooks}'
    
    def borrowBook(self):
        print('You have borrowed a book.')
        
    def returnBook(self):
        print('You have returned your book')
        

class Library:
    def __init__(self, name, bookList, members):
        self.name = name
        self.books = bookList = {}
        self.members = members = []
        
    def __str__ (self):
        return f'{self.name}, books: {self.books}, member: {self.members}'
    
    def __repr__(self):
        return f'Name: {self.name}, Books: {self.books}, Members: {self.members}'
    
    def addBook(self):
        print('You added a book')
        
    def removeBook(self):
        print('You have removed a book from the library list.')
        
    def addMember(self):
        print('you added a member.')
        
    def removeMember(self):
        print('You removed a member.')
        
    def lendBook(self):
        print('You lent the book out')
        
    def returnBook(self):
        print('This book was returned')
