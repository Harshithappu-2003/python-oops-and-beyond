# Library Management System

## Introduction

The Library Management System is a Python-based console application designed to simplify the management of a library. It allows users to borrow, return, and donate books, along with tracking borrowed books. This system is implemented using Object-Oriented Programming (OOP) principles to ensure scalability and maintainability.

## Features

Display Books
List all the books currently available in the library.

## Borrow a Book

Users can borrow a book by providing their name and the title of the book. If the book is unavailable, the user is notified.

## Return a Book

Users can return previously borrowed books, and the system updates the library records accordingly.

## Donate a Book

Users can donate books to the library, which will then be added to the list of available books.

## Track Borrowed Books

Allows users to view the list of books they have borrowed.

## Exit

Safely exit the application.

## How It Works

Classes
Library Class

## Manages the list of books available in the library

Handles operations like displaying books, borrowing books, returning books, and donating books.
Student Class

## Facilitates user interactions like requesting a book, returning a book, or donating a book

## Attributes and Methods

Library Class
__init__(self, listofbooks)
Initializes the library with a predefined list of books.

displaybooks()
Displays the list of all available books.

borrow(name, bookname)
Allows users to borrow a book if it is available. Updates the library records and tracks the borrowed book.

returnBook(bookname)
Allows users to return a book to the library. Updates the library records.

donateBook(bookname)
Adds a donated book to the library's collection.

Student Class
requestBook()
Prompts the user to enter the book they want to borrow.

returnbookfromstudent()
Handles the book return process and removes the record from the tracker.

donationbook()
Handles the donation process and adds the book to the library.

## Usage Instructions

Run the Script
Execute the Python script (app.py) in your terminal or preferred IDE.

## Future Improvements

Add a search functionality to find books by title or author.
Implement a database for persistent storage of books and user transactions.
Create a graphical user interface (GUI) for better usability.
Add user authentication for better security and personalization.

## Requirements

Python 3.x
Ensure you have Python installed. You can download it from python.org.
