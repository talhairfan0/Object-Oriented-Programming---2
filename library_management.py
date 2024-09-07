class labrary:

    def __init__(self , list_of_books , name) :
        self.bookslist = list_of_name
        self.name = name
        self.landDict = {}

    def displayBooks(self):
        print("we have the folloeing books in labrary",self.name)
        for book in self.bookslist:
            print(book)


    def lendbook(self,user,book):
        if book in self.bookslist:
            print("sorry ! this book is not avilible  in our library.")
        elif book in self.lendDict:
            print("this book not avilible in this time.this book is already being used by",self.lendDict[book])    
        else:
            self.lendDict[book].user
            print("lender-book database has been updated.you can take this book now. ")  

    def addBook(self , book):
        self.bookslist.append(book)
        print(book , "has been added in the book list")











    
booksList=[
    "html","css","jv","py","c++","jv scrift"
]

libraryName = "histry libraray"