books = []

while True:
    print("\n1. Add Book\n2. Remove Book\n3. View Books\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
    elif choice == "2":
        book = input("Enter book name to remove: ")
        books.remove(book)
    elif choice == "3":
        for book in books:
            print(book)
    elif choice == "4":
        break
    else:
        print("Invalid option.")