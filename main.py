def get_shelfs_book(number):
    for i in range(number):
        shelf = input("На какую полку поставить книгу: ")
        name_book = input("Название книги: ")
        author = input("Автор книги: ")

        book_format = {
            "name": name_book,
            "author": author
            }
        
        with open("Library.txt","a") as file:
            file.write("Shelf {} {}\n".format(shelf, book_format))
    return "книги добавлены"


def read_file_library():
    with open("Library.txt","r") as file:
        for line in file:
            print(line)


def main():
    number = int(input("какое количестно книг вам надо добавить?: "))
    print(get_shelfs_book(number))
    read_file_library()


if __name__ == "__main__":
    main()
