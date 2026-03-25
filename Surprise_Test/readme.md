# 📝 Smart To-Do Manager

## 📌 Overview

The **Smart To-Do Manager** is a modern, responsive web application designed to help users efficiently manage their daily tasks. It allows users to create, organize, filter, and track tasks based on priority and deadlines.

The application is built using **HTML, Bootstrap 5, JavaScript, and localStorage**, ensuring a clean UI, smooth performance, and persistent data storage without requiring a backend.

---

## 🎯 Objective

The primary objective of this project is to:

* Provide an intuitive interface for task management
* Improve productivity through task prioritization and deadline tracking
* Demonstrate frontend development concepts such as DOM manipulation, event handling, and performance optimization using debounce

---

## 🚀 Features

### ✅ Task Management

* Add new tasks with:

  * Title
  * Priority (Low, Medium, High)
  * Deadline
* Prevents adding empty tasks

---

### 🔄 Task Actions

* Mark tasks as **Completed / Pending**
* Delete tasks permanently

---

### 🔍 Filtering (with Debounce)

* View tasks by:

  * All
  * Completed
  * Pending
* Uses **debounce (300ms)** to optimize performance

---

### 📊 Sorting

* Sort tasks by:

  * Priority (High → Low)
  * Deadline (Nearest first)

---

### 📈 Task Counters

Displays real-time statistics:

* Total tasks
* Completed tasks
* Pending tasks

---

### ⚠️ Overdue Highlight

* Tasks with deadlines earlier than the current date are highlighted
* Helps identify urgent or missed tasks

---

### 💾 Data Persistence

* Uses **localStorage** to store tasks
* Data remains saved even after page refresh

---

### 📱 Responsive Design

* Built with **Bootstrap 5**
* Works seamlessly across mobile, tablet, and desktop devices

---

## 🛠️ Tech Stack

* **HTML5** – Structure
* **CSS3 / Bootstrap 5** – Styling & responsiveness
* **JavaScript (ES6)** – Functionality
* **localStorage** – Data persistence

---

## 🧠 Key Concepts Used

* DOM Manipulation
* Event Handling
* Array Methods (`map`, `filter`, `sort`)
* Debounce Technique
* Local Storage API
* Conditional Rendering

---

## 📂 Project Structure

```
Smart-ToDo-Manager/
│
├── index.html   # Main application file (HTML + CSS + JS)
└── README.md    # Project documentation
```

---

## ▶️ How to Run

1. Download or clone the repository
2. Open `index.html` in any browser
3. Start adding and managing tasks

---

## 💡 Future Enhancements

* Add **search functionality with debounce**
* Implement **edit/update task feature**
* Add **dark mode**
* Integrate backend (Node.js / Firebase)
* Add notifications or reminders

---

## 📌 Conclusion

The Smart To-Do Manager is a practical implementation of core frontend development concepts. It demonstrates how to build an interactive, responsive, and optimized application using only client-side technologies.

---

## 👤 Author

* Developed by: Ravi Ranjan
* 25MCA20098

---
