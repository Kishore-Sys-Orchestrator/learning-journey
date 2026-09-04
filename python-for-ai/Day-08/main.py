print("----------Welcome to book store----------\n")

lines = []
def add_a_book(book_name,author_name):
    with open("test_file.txt","a") as f:
        f.write(f"Book name: {book_name} |")
        f.write(f"Author name: {author_name}\n")

    print(f"Your {book_name} is added.")


   
def book_delete(book_to_delete):
    remaining_book = []
    with open("test_file.txt","r") as f:
        for line in f:
            parts = line.strip().split('|')
            title = parts[0].replace("Book name: ","").strip()
            if title != book_to_delete:
                    remaining_book.append(line)
    with open("test_file.txt","w") as f:
        f.writelines(remaining_book)
    print("Updated books list:")
    with open("test_file.txt","r") as f:
        for line in f:
            print(line.strip())
def show():
    with open("test_file.txt","r") as f:
        for line in f:
            print(line.strip())

found = False
def search(book_to_search):
    found_book = []
    with open("test_file.txt","r") as f:
        for line in f:
            parts = line.strip().split('|')
            title = parts[0].replace("Book name: ","").strip()
            if title == book_to_search:
                found = True
                found_book.append(line.strip())
    if found != True:
        print(f"There is no book called {book_to_search}")
    else:
        print(found_book)
    return found_book

while(1):

    choice_of_work = int(input("Enter your choice from below\n"
                        "1. Add a book\n"
                        "2. Remove a book\n"
                        "3. Show all the book\n"
                        "4. Search a book\n"
                        "5. Exit\n"
                        ))



    if choice_of_work == 1:
        book_name = input("Enter the book name: ")
        author = input("Enter the author name: ")
        if book_name != "" or author != "":
            add_a_book(book_name,author)
        else:
            print("Please enter valid book name")
    elif choice_of_work == 2:
        book_to_delete = input("Enter the book name: ")
        if book_to_delete != "":
            book_delete(book_to_delete)
        else:
            print("please enter valid book name")
    elif choice_of_work == 3:
        show()
    elif choice_of_work == 4:
        book_to_search = input("Enter the book name: ")
        if book_to_search != "":
            search(book_to_search)
        else:
            print("please enter valid book name")
    elif choice_of_work == 5:
        break
    else:
        print("Please enter the valid choice")