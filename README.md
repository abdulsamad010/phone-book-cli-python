# 📖 Phone Book CLI Application

A simple command-line Phone Book application built with Python that allows users to add, view, edit, and delete contacts.

The project uses Python file handling to store contact information locally in a text file, allowing contacts to remain available after the application is closed.

## ✨ Features

- ➕ Add new contacts
- 📋 View all saved contacts
- ✏️ Edit existing contacts
- 🗑️ Delete contacts
- 💾 Store contact data locally using a text file
- 🖥️ Simple menu-driven command-line interface

## 🛠️ Technologies Used

- Python
- Python File Handling
- Command-Line Interface (CLI)
- Text File Storage

## 📂 Project Structure

```text
phone-book-cli-python/
├── Phone_Book_Project.py
├── data.txt
├── README.md
└── LICENSE
```

## ⚙️ How It Works

The application displays a menu with five available operations:

```text
1. Add New Contact
2. Delete a Contact
3. View All Contacts
4. Edit a Contact
5. Close Application
```

Contact records are stored in `data.txt` using the following format:

```text
Name,PhoneNumber
```

The application reads and updates this file according to the operation selected by the user.

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/abdulsamad010/phone-book-cli-python.git
cd phone-book-cli-python
```

### Run the Application

```bash
python Phone_Book_Project.py
```

Make sure Python is installed on your system before running the application.

## 📚 Learning Outcomes

Through this project, I practiced:

- Python loops and conditional statements
- User input handling
- Reading, writing, and appending data to files
- Working with lists and strings
- Implementing basic CRUD-style operations
- Building a menu-driven command-line application
- Persisting data locally without using a database

## 🔮 Future Improvements

- Add input validation and error handling
- Prevent duplicate phone numbers
- Implement exact phone-number matching
- Add contact search functionality
- Refactor the application using functions and classes
- Replace text-file storage with SQLite

## 👤 Author

**Abdul Samad**

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
