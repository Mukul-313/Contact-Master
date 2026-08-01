class Library():
    def __init__(self):
        self.noBooks=0
        self.books=[]

    def addbook(self,book):
        self.books.append(book)
        self.noBooks=len(self.books)

    def showinfo(self):
        print(f"The Library has {self.noBooks} books. The books are")
        for book in self.books:
            print(book)



l1=Library()
l1.addbook("Harry Potter")
l1.addbook("Rich Dad Poor Dad")
l1.addbook("Python Basics")
l1.showinfo()
