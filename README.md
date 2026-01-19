# Mini School Management System (Python)

This is a simple School Management System built using Python.  
The project is designed to practice **Object-Oriented Programming (OOP)** and **File Handling** concepts.

---

## Project Objectives

- Understand class and object creation
- Practice file handling for persistent data storage
- Implement encapsulation using private variables
- Ensure data is not lost after program termination

---

## Concepts Used

- Object-Oriented Programming (OOP)
  - Class
  - Object
  - Encapsulation
- File Handling
  - Read
  - Write
  - Append

---


## Class Design

# Course Class
- Stores course name
- Provides a method to get course name

# Student Class
- Stores student name and roll
- Stores enrolled courses in a list
- Uses a **private variable** for password
- Uses a **getter method** to access password securely

---

## File Handling

- When a student enrolls in a course, the data is saved in `students.txt`
- Data is stored using **append mode**
- Data remains available even after restarting the program

---

## Encapsulation

- Student password is declared as a private variable
- Password cannot be accessed directly from outside the class
- Password is accessed using a getter method
- Password is **not printed** for security reasons

---

## How to Run

```bash
python main.py

