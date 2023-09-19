class Book:
    def __init__(self, name, author, genre, availability):
        self.name = name
        self.author = author
        self.genre = genre
        self.availability = availability

    def __str__(self):
        return self.name + self.author + self.genre


def library_load():
    book_sort = 0
    books = []

    with open("Books.txt", 'r') as all_books:
        all_info = all_books.read()
        all_info = all_info.split(",")
        all_info = [no_white.strip() for no_white in all_info]

        for i in all_info:
            if book_sort == 0:
                book_name = i
                book_sort += 1

            elif book_sort == 1:
                book_author = i
                book_sort += 1

            elif book_sort == 2:
                book_genre = i
                book_sort += 1

            elif book_sort == 3:
                book_availability = i
                book = Book(book_name, book_author, book_genre, book_availability)
                books.append(book)
                book_sort = 0
        all_books.close()
    return books


def add_book(books):
    book_name = input("What's the name of the book that you would like to add?: ")
    book_author = input("What's the name of the author of this book?: ")
    book_genre = input("What's the genre of this book?: ")
    book_availability = "1"

    book = Book(book_name, book_author, book_genre, book_availability)
    books.append(book)
    with open("books.txt", 'a') as all_books:
        all_books.write(",\n" + book.name + ", " + book.author + ", " + book.genre + ", " + book.availability)
        all_books.close()


def remove_book(book_name):
    books = library_load()
    with open("books.txt", 'w') as all_books:

        line = None
        for i, info in enumerate(books):
            if book_name == info.name:
                line = i
            else:
                pass

        for i, info in enumerate(books):
            if i != line:
                if i != len(books) - 1:
                    all_books.write(info.name + ", " + info.author + ", " + info.genre + ", " + info.availability +
                                    ",\n")
                else:
                    all_books.write(info.name + ", " + info.author + ", " + info.genre + ", " + info.availability)
            else:
                pass
        all_books.close()


def borrow_return_book(action, book_name):
    books = library_load()
    line = None
    with open("books.txt", 'w') as all_books:

        for i, info in enumerate(books):
            if info.name == book_name:
                line = i
            else:
                pass

        if action == 0:
            for i, info in enumerate(books):
                if i != line:
                    if i != len(books) - 1:
                        all_books.write(info.name + ", " + info.author + ", " + info.genre + ", " + info.availability +
                                        ",\n")
                    else:
                        all_books.write(info.name + ", " + info.author + ", " + info.genre + ", " + info.availability)
                else:
                    info.availability = "0"
                    if i != len(books) - 1:
                        all_books.write(info.name + ", " + info.author + ", " + info.genre + ", " + info.availability +
                                        ",\n")
                    else:
                        all_books.write(info.name + ", " + info.author + ", " + info.genre + ", " + info.availability)

        if action == 1:
            for i, info in enumerate(books):
                if i != line:
                    if i != len(books) - 1:
                        all_books.write(info.name + ", " + info.author + ", " + info.genre + ", " + info.availability +
                                        ",\n")
                    else:
                        all_books.write(info.name + ", " + info.author + ", " + info.genre + ", " + info.availability)
                else:
                    info.availability = "1"
                    if i != len(books) - 1:
                        all_books.write(info.name + ", " + info.author + ", " + info.genre + ", " + info.availability +
                                        ",\n")
                    else:
                        all_books.write(info.name + ", " + info.author + ", " + info.genre + ", " + info.availability)
    all_books.close()


def main():
    while True:
        books = library_load()
        print("1. Display all available books\n2. Add a book from the library\n3. Remove a book from the library\n"
              "4. Borrow a book\n5. Return a book\n6. Exit the library\n")
        option = int(input("Please choose an option: "))

        if option == 1:
            print("This is the list of currently available books: \n")
            for a, i in enumerate(books):
                if i.availability == "1":
                    if a == len(books) - 1:
                        print("Name: " + i.name + "  " + "Author: " + i.author + "  " + "Genre: " + i.genre + "\n")
                    else:
                        print("Name: " + i.name + "  " + "Author: " + i.author + "  " + "Genre: " + i.genre)
                else:
                    pass
        elif option == 2:
            print("Please answer the below questions:")
            add_book(books)
        elif option == 3:
            book_delete = input("What book would you like to delete?: ")
            remove_book(book_delete)
        elif option == 4:
            book_borrow = input("What book would you like to borrow?: ")
            borrow_return_book(0, book_borrow)
            print("Thank you for using the library!\n")
        elif option == 5:
            book_return = input("What book would you like to return?: ")
            borrow_return_book(1, book_return)
            print("Thank you for returning the book\n")
        elif option == 6:
            break
        else:
            pass


if __name__ == "__main__":
    main()
