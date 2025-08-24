# Learning Log

A web application developed as part of the learning journey through "Python Crash Course" (3rd Edition) by Eric Matthes. This application allows users to create topics and make entries about their learning progress.

## ✨ Basic Features

- **User Authentication**: User registration and login system
- **Topic Management**: Create and view study topics
- **Entry Management**: Add and view learning entries
- **Data Protection**: Users can only access their own topics and entries

## 🛠️ Technologies Used

- **Python 3.x**
- **Django** (Web framework)
- **HTML** (Basic Django templates)
- **SQLite** (Development database)

## 📦 Installation and Setup

1. Clone the repository:
```bash
git clone https://github.com/feliperrs/learning-log.git
```

2. Navigate to the project directory:
```bash
cd learning-log
```

3. Create a virtual environment (recommended):
```bash
python -m venv ll_env
```

4. Activate the virtual environment:
- Windows:
```bash
ll_env\Scripts\activate
```
- Linux/Mac:
```bash
source ll_env/bin/activate
```

5. Install dependencies:
```bash
pip install django
```

6. Apply database migrations:
```bash
python manage.py migrate
```

7. Start the development server:
```bash
python manage.py runserver
```

8. Access the application at: `http://localhost:8000` or `http://127.0.0.1:8000`

## 📚 Learning Context

This project was developed following the 3rd edition of "Python Crash Course", covering chapters 18-20 which include:

- Setting up a Django project
- Creating data models
- Building views and templates
- Implementing user authentication
- Working with forms and template inheritance

## ⚠️ Implementation Notes

This is an educational project that faithfully follows the book's implementation, focusing on core Django concepts with minimal styling.

## 📖 Reference

- Matthes, E. (2023). *Python Crash Course, 3rd Edition: A Hands-On, Project-Based Introduction to Programming*. No Starch Press.

---

*Educational project developed as part of learning Django through the 3rd edition of "Python Crash Course". This implementation follows the book's content, focusing on fundamental Django concepts.*
