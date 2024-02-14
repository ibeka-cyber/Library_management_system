class library:
    space ="\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n"
    #----------------------- __init__ and __del__-----------------------------------
    def __init__(self,fileName):
        self.fileName=fileName
        self.file=open(self.fileName,"a+")
        
        
    def __del__(self):
        self.file.close()
    
    #------------------------------------------------------------------------------
    #----------------------- Library operations -----------------------------------
    #------------------------------------------------------------------------------
    
    #~~~~~~~~~~~~~~~~~~~~ Go to the first row of the file ~~~~~~~~~~~~~~~~~~~~
    def file_seek(self):
        self.file.seek(0)
        self.lines=self.file.readlines()
        
    #~~~~~~~~~~~~~~~~~~~~ List the book in the txt file ~~~~~~~~~~~~~~~~~~~~
    def listBooks(self): 
        self.file_seek()
        for i in range(len(self.lines)):
            book_name,book_author,book_year,book_page_num=self.lines[i].split(",")
            print(f"Book Name:{book_name}, Author Name:{book_author}")
        print(self.space)
    
    #~~~~~~~~~~~~~~~~~~~~ Add the book to the library ~~~~~~~~~~~~~~~~~~~~~~~~~~
    def addBook(self,book_name,book_author,book_year,book_page_num):
        book = ','.join([book_name, book_author, book_year,book_page_num]) + "\n"
        self.file.write(book)
        print(f"{book_name} named book has been added")
        print(self.space)
        
    #~~~~~~~~~~~~~~~~~~~~ Remove the book from the library ~~~~~~~~~~~~~~~~~~~~
    def removeBook(self,selected_book_name):
        exist=self.check_book(selected_book_name)
        print(exist)
        if exist:
            self.file_seek()
            new_lines=[]
            for i in range(len(self.lines)):
                book_name,book_author,book_year,book_page_num=self.lines[i].split(",")
                
                if book_name != selected_book_name and self.lines[i] not in new_lines:
                    new_lines.append(self.lines[i])
                    
            with open(self.fileName, "w") as f:
                for line in new_lines:
                    self.file.writelines(line)
            print(f"{selected_book_name} is removed")
            print(self.space)
        else:
            print(f"{selected_book_name} is not exist")
            
    #~~~~~~~~~~~~~~~~~~~~ Check the exist of the book ~~~~~~~~~~~~~~~~~~~~
    def check_book(self,selected_book_name):
        self.file_seek()
        exist=False
        for i in range(len(self.lines)):
            book_name=self.lines[i].split(",")[0]
            print(book_name)
            if book_name == selected_book_name:
                exist=True
        return exist
    
#~~~~~~~~~~~~~~~~~~~~ Show Menu ~~~~~~~~~~~~~~~~~~~~
def menu():
    print("""
********** MENU ****************
1)List Books
2)Add Book
3)Remove Book
q)Exit
********************************
          """)
while True:
    lib=library("books.txt")
    menu()
    choice=input("Make your choice 1 or 2 or 3: \n")
    
    if choice=="1":
        lib.listBooks()
    
    elif choice=="2":
        book_name=input("Enter the book name: ")
        book_author=input("Enter the book author: ")
        book_year=input("Enter the book year: ")
        book_page_num=input("Enter the number of pages: ")
        lib.addBook(book_name,book_author,book_year,book_page_num)
        
    elif choice=="3":
        selected_book=input("Enter book name: ")
        lib.removeBook(selected_book)  
        
    elif choice=="q" or choice=="Q":
        print("program terminated")
        print(lib.space)
        break
    else:
        print("please choose 1,2 or 3")
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        