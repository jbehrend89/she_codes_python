class Book:

    def __init__(self, title, author, num_pages, current_page):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.current_page = current_page
        self.bookmarked_page = 1
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Number of Pages: {self.num_pages}"

    def bookmark_page(self, specific_bookmark):
        self.bookmarked_page = self.current_page

    def turn_page(self, forward):
        if forward:
            self.current_page = self.current_page + 1
        else:
            self.current_page = self.current_page - 1

    # go directly to specific page number
    def specific_page(self, page_num):
        self.current_page = page_num

    # bookmark a specific page number, i.e. not just the current page
    def specific_bookmark(self, spec_bookmark_num):
        pass

    # automatically go back to the start of the book (i.e. page 1) when the user turns to the final page
    def start_again(self, end):
        if end:
            self.current_page = self.num_pages - self.num_pages
            
    



book1 = Book("Great Expectations", "Charles Dickens", 340, 2)
print(book1.title)
print(book1.author)

book2 = Book("To Kill a Mockingbird", "Harper Lee", 298, 30)
print(book2.title)

print()
print(book1)
print(book2)

print(book2.current_page)
print(book2.bookmarked_page)
book2.turn_page(True)
book2.turn_page(True)
book2.turn_page(True)
book2.turn_page(True)
book2.turn_page(True)
book2.turn_page(True)
print(book2.current_page)
book2.bookmark_page()
print(book2.bookmarked_page)

book2.specific_page(60)
print(book2.current_page)
