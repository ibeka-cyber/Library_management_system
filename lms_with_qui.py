import tkinter as tk
import tkinter.messagebox as msg
#xxxxxxxxxxxxxxxxxxxxxxxxx Lib Class xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
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
        books=[]
        for i in range(len(self.lines)):
            book_name,book_author,book_year,book_page_num=self.lines[i].split(",")
            books.append([book_name,book_author])
            print(f"Book Name:{book_name}, Author Name:{book_author}")
        print(self.space)
        return books
    
    #~~~~~~~~~~~~~~~~~~~~ Add the book to the library ~~~~~~~~~~~~~~~~~~~~~~~~~~
    def addBook(self,book_name,book_author,book_year,book_page_num):
        book = ','.join([book_name, book_author, book_year,book_page_num]) + "\n"
        self.file.write(book)
        result=f"{book_name} named book has been added"+self.space
        print(f"{book_name} named book has been added")
        print(self.space)
        return result
    #~~~~~~~~~~~~~~~~~~~~ Remove the book from the library ~~~~~~~~~~~~~~~~~~~~
    def removeBook(self,selected_book_name):
        exist=self.check_book(selected_book_name)
        remove=False
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
            remove=True
            print(f"{selected_book_name} is removed")
            print(self.space)
        else:
            print(f"{selected_book_name} is not exist")
        
        return remove
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
    menu="""*********************************************
1)List Books
2)Add Book
3)Remove Book
q)Exit
*********************************************"""
          
    print(menu)
    return menu
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#---Form attributes---
lib=library("books.txt")
libForm=tk.Tk()
libForm.title("Library Menu")
libForm.geometry("435x571+700+150")
libForm.resizable(False,False)
libForm.iconbitmap(default="books.ico")
photo = tk.PhotoImage(file="design.png")
label=tk.Label(text="",image=photo)
label.pack()

#--Menu--
menu=tk.Label(libForm,fg="#593515", bg="#d1d0ce",font="Halvetica 10",text=menu())
menu.place(x=173,y=105,width=270)

#--choice menu--
def Go():
    #--choice operation--
    if choice_entry.get()=="1":
        ListBook()

    elif choice_entry.get()=="2":
        AddBook_features()
        
    elif choice_entry.get()=="3":
        RemoveBook()
        
    elif choice_entry.get()=="q" or choice_entry.get()=="Q":
        Exit()
    elif choice_entry.get()=="":
        msg.showwarning("Choice is empty!","Choice can not be empty!")
    else:
        msg.showwarning("Choice is empty!","Please make your choice 1 or 2 or 3")

#-- Add Attributes hidding --
def addForget():
      bookName.place_forget()
      bookName_entry.place_forget()
      bookAuthor.place_forget()
      bookAuthor_entry.place_forget()
      bookYear.place_forget()
      bookYear_entry.place_forget()
      bookPageNum.place_forget()
      bookPageNum_entry.place_forget()
      bookAuthor_entry.place_forget()
      AddBookButton.place_forget()
      bookTitle.place_forget()
      addBook_removeBook_warn.place_forget()
      bookName_entry.delete(0,"end")
      bookAuthor_entry.delete(0,"end")
      bookPageNum_entry.delete(0,"end")
      bookYear_entry.delete(0,"end")
      addBook_removeBook_warn.config(text="")

#-- Remove attributes hidding -- 
def removeForget():
    addForget()
    removeBook.place_forget()
    removeBook_entry.place_forget()
    removeButton.place_forget()
    removeBook_entry.place_forget()
    remBook.place_forget()
    removeBook_warn.place_forget()
    removeBook_warn.config(text="")
    removeBook_entry.delete(0,"end")

#-- List attributes hidding -- 
def listforget():
    listBook.place_forget()
    listTitle.place_forget()

#-- listBook -- 
def ListBook():
    addForget()
    removeForget()
    listTitle.place(x=250,y=290)
    listBook.place( width=250,heigh=200,x=177,y=280)
    books=lib.listBooks()
    if len(books)==0:
        listBook.config(text="There aren't any books in the library")
    else:
        new_text = "\n".join([f"Book Name: {book[0]}, Author: {book[1]}" for book in books])
        listBook.config(text=new_text)

#--AddBook attributes showing--
def AddBook_features():
    removeForget()
    listforget()
    bookTitle.place(x=230,y=290)
    bookName.place(x=180,y=330)
    bookName_entry.place(x=310,y=330,width=110)
    bookAuthor.place(x=180,y=360)
    bookAuthor_entry.place(x=310,y=360,width=110)
    bookYear.place(x=180,y=390)
    bookYear_entry.place(x=310,y=390,width=110)
    bookPageNum.place(x=180,y=420)
    bookPageNum_entry.place(x=310,y=420,width=110)
    AddBookButton.place(x=215,y=450,width=165)
    addBook_removeBook_warn.place(x=200,y=480,width=200)

#--AddBook--
def AddBook():
    book_name=bookName_entry.get()
    book_author=bookAuthor_entry.get()
    book_year=bookYear_entry.get()
    book_page_num=bookPageNum_entry.get()
    if book_name=="" or book_author=="" or book_year=="" or book_page_num=="":
        addBook_removeBook_warn.config(text="** Books features can not be empty! **")
    else:
        lib.addBook(book_name, book_author, book_year, book_page_num)  
        addBook_removeBook_warn.config(text="** Book has been added **")

#--RemoveBook attributes showing--
def RemoveBook():
    addForget()
    listforget()    

    remBook.place(x=230,y=290)
    removeBook.place(x=200,y=330)
    removeBook_entry.place(x=290,y=330,width=110)
    removeButton.place(x=290,y=360,width=110)
    removeBook_warn.place(x=200,y=400,width=200)

#--RemoveBook--
def RemoveBook_lib():
    selected_book_name=removeBook_entry.get()
    if selected_book_name=="":
        removeBook_warn.config(text="** Book name can not be empty! **")
    else:
        book_exist=lib.check_book(selected_book_name)
        if book_exist:
            removed=lib.removeBook(selected_book_name)
            if removed:
                removeBook_warn.config(text="** Book has been removed **")
            else:
                removeBook_warn.config(text="** Book did not remove **")         
        else:
            removeBook_warn.config(text="** Book is not exist **")

#--Exit--
def Exit():
    libForm.destroy()

#ListBook Attributes
listBook=tk.Label(libForm,text=ListBook,bg="#d1d0ce",fg="#593515")
listBook.place_forget()
listTitle=tk.Label(libForm,text="List Books",font="Halvetica 12 bold underline",bg="#d1d0ce",fg="#593515")

#AddBook Attributes
bookTitle=tk.Label(libForm,text="Book Features",font="Halvetica 12 bold underline",bg="#d1d0ce",fg="#593515")
bookName=tk.Label(libForm,text="Book Name:",bg="#d1d0ce",fg="#593515")
bookName_entry=tk.Entry(libForm,text="",bg="#938572",fg="white")
bookAuthor=tk.Label(libForm,text="Book Author:",bg="#d1d0ce",fg="#593515")
bookAuthor_entry=tk.Entry(libForm,text="",bg="#938572",fg="white")
bookYear=tk.Label(libForm,text="Book Year:",bg="#d1d0ce",fg="#593515")
bookYear_entry=tk.Entry(libForm,text="",bg="#938572",fg="white")
bookPageNum=tk.Label(libForm,text="Book Number of Page:",bg="#d1d0ce",fg="#593515")
bookPageNum_entry=tk.Entry(libForm,text="",bg="#938572",fg="white")
AddBookButton=tk.Button(libForm,text="Add Book",bg="#563d1f",fg="white",command=AddBook)
addBook_removeBook_warn=tk.Label(libForm,text=" ",fg="#593515",bg="#d1d0ce")

#RemoveBook Attributes
remBook=tk.Label(libForm,text="Remove Book Feature",font="Halvetica 10 bold underline",bg="#d1d0ce",fg="#593515")
removeBook=tk.Label(libForm,text="Book name: ",bg="#d1d0ce",fg="#593515")
removeBook_entry=tk.Entry(libForm,text="",bg="#938572",fg="white")
removeButton=tk.Button(libForm,text="Remove",command=RemoveBook_lib,bg="#563d1f",fg="white")
removeButton_entry=tk.Entry(libForm,text="")
removeBook_warn=tk.Label(libForm,text=" ",fg="#593515",bg="#d1d0ce")

#--Choice Entry--
choice=tk.Label(libForm,text="Make Your Choice: ",bg="#d1d0ce",fg="#593515",font="Arial 8 bold")
choice.place(x=180,y=215)
choice_entry=tk.Entry(bg="#938572",fg="white")
choice_entry.place(x=297,y=215,width=120,height=20)

go_button=tk.Button(libForm,text="Go",bg="#563d1f",fg="white",font="Halvetica 10 bold",command=Go)
go_button.place(x=298,y=240,width=120,height=25)

libForm.mainloop()