# 🤖 AI Chatbot using Search Algorithms (BFS, DFS, Best-First)

## 📌 Project Overview

This project is an **AI-based chatbot** that uses classical search algorithms such as **Breadth-First Search (BFS), Depth-First Search (DFS), and Best-First Search** to retrieve responses from a structured knowledge base.

The chatbot is capable of handling both **informational queries** (like admission, fees, courses) and **general conversation** (like hi, hello, thanks), making it interactive and user-friendly.

It includes a **modern web-based user interface** built using HTML, CSS, and JavaScript, and a backend powered by Python (Flask).

---

## 🚀 Features

* 💬 Interactive chatbot interface (modern UI)
* 🧠 Uses AI search algorithms (BFS, DFS, Best-First)
* 🔍 Keyword-based NLP matching
* 📂 JSON-based knowledge base
* 🎛️ Algorithm selection (switch between BFS, DFS, Best-First)
* ⌨️ Press **Enter** to send messages
* 🗑️ Clear chat functionality
* 🌐 Web-based (runs in browser)

---

## 🏗️ Project Structure

```
chatbot_web/
│── app.py
│── knowledge_base.json
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
```

---

## ⚙️ Technologies Used

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (Flask)
* **Data Storage:** JSON
* **Algorithms:** BFS, DFS, Best-First Search

---

## 🧠 How It Works

1. User enters a query in the chatbot UI
2. Input is processed using **keyword matching (NLP)**
3. The system identifies the relevant topic
4. Selected **search algorithm (BFS/DFS/Best-First)** traverses the knowledge base
5. The correct response is retrieved
6. Response is displayed in the chat interface

---

## 🔍 Search Algorithms Used

### 🟢 Breadth-First Search (BFS)

* Explores nodes **level by level**
* Guarantees shortest path
* Uses **Queue**

### 🔵 Depth-First Search (DFS)

* Explores **deep into one branch**
* Uses **Recursion/Stack**

### 🟡 Best-First Search

* Uses **heuristic function**
* Chooses most promising node first
* Faster and optimized

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

```
pip install flask
```

### 2️⃣ Run Server

```
python app.py
```

### 3️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

## 📊 Example Queries

* "Tell me about admission"
* "What are the fees?"
* "Courses available"
* "Hi / Hello"
* "Thanks"

---

## ⚠️ Limitations

* Uses basic keyword matching (not advanced NLP)
* Only predefined responses are supported
* No learning capability (not ML-based)

---

## 🔮 Future Scope

* Integrate advanced NLP (NLTK, spaCy)
* Add voice-based interaction
* Deploy online (cloud hosting)
* Use Machine Learning for dynamic responses
* Database integration (MongoDB/MySQL)

---

## 🎯 Conclusion

This project demonstrates how **AI search algorithms** can be applied to build an interactive chatbot system. It bridges theoretical concepts of Artificial Intelligence with real-world implementation.

---

## 📚 References

* Python Documentation: https://docs.python.org
* Flask Documentation: https://flask.palletsprojects.com
* GeeksforGeeks (AI Algorithms)
* Artificial Intelligence: A Modern Approach – Russell & Norvig

---

## 👨‍💻 Author

**Ravi Ranjan Kumar**

---

## ⭐ Note

This project is created for academic purposes to demonstrate AI concepts using search algorithms.
