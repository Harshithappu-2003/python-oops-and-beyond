## Date - 28th Nov 2024
## Author - Arpit Jain

## Task -> Create a new library Management System

## Algorithm
# 1. Class library = list of books, borrow, return, donate.
# 2. Class Student = requestbook, returnbook, donatebook.

class Library:
    def __init__(self, listofbooks):
        self.books = listofbooks

    def displaybooks(self):
        print("List of all available books in the library--------")
        for i in range(len(self.books)):
            print(f'{i} . {self.books[i]}')

    def borrow(self, name, bookname):
        if bookname not in self.books:
            print(f'{bookname} - Sorry, the book is not available in the library.')
        else:
            tracker.append({name: bookname})
            print(f'BOOK ISSUED: Congratulations, you have successfully checked out {bookname}.')
            self.books.remove(bookname)

    def returnBook(self, bookname):
        print(f"BOOK RETURNED: Thank you so much for returning {bookname}.")
        self.books.append(bookname)

    def donateBook(self, bookname):
        print(f'BOOK DONATED: Thank you so much for donating {bookname} to the Library. Have a good day!')
        self.books.append(bookname)


class Student:
    def requestBook(self):
        print('Welcome! You are looking to borrow a book...')
        self.book = input("Enter the book you want to borrow: ")
        return self.book

    def returnbookfromstudent(self):
        print('Welcome! You are looking to return a book...')
        name = input('Enter your name: ')
        self.book = input("Enter the book you want to return: ")
        if {name: self.book} in tracker:
            tracker.remove({name: self.book})
        return self.book

    def donationbook(self):
        print('Welcome! You are looking to donate a book...')
        self.book = input("Enter the book you want to donate: ")
        return self.book


if __name__ == "__main__":
    Aimerz_library = Library([
        "To Kill a Mockingbird",
        "The Great Gatsby",
        "1984",
        "Pride and Prejudice",
        "Harry Potter and the Sorcerer's Stone",
        "The Lord of the Rings: The Fellowship of the Ring",
        "The Catcher in the Rye",
        "Fahrenheit 451",
        "The Hobbit",
        "Gone with the Wind",
        "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe",
        "Brave New World",
        "Animal Farm",
        "The Shining",
        "The Grapes of Wrath",
        "The Picture of Dorian Gray",
        "Frankenstein",
        "The Scarlet Letter",
        "The Adventures of Sherlock Holmes",
        "Moby-Dick"
    ])
    student = Student()
    tracker = []

print('--- Welcome to Aimerz Library ---')
print('--- You can borrow, return, or donate books ---')
print('Choose from the respective actions: \
\n 1. List all available books \
\n 2. Request to borrow a book \
\n 3. Return a book \
\n 4. Donate a book \
\n 5. Track your issued books \
\n 6. Exit the portal')

while True:
    try:
        user_choice = int(input('Enter your choice between 1 to 6: '))
        if user_choice == 1:
            Aimerz_library.displaybooks()
        elif user_choice == 2:
            Aimerz_library.borrow(input('Enter your name: '), student.requestBook())
        elif user_choice == 3:
            Aimerz_library.returnBook(student.returnbookfromstudent())
        elif user_choice == 4:
            Aimerz_library.donateBook(student.donationbook())
        elif user_choice == 5:
            print('Welcome to the tracker Portal!')
            username = input('Enter your name: ')
            flag = 0  # Initialize flag
            for issue in tracker:
                for key, value in issue.items():
                    if key == username:
                        print(f'{key} has borrowed {value} book.')
                        flag = 1
                        break
            if flag == 0:
                print('No books issued to you.')
        elif user_choice == 6:
            print('Thank you so much for visiting our portal. See you next time!!!')
            break
        else:
            print('Invalid Response!')
    except ValueError:
        print('Please enter a valid numeric choice between 1 and 6.')
    except Exception as e:
        print(f'An error occurred: {e}')
