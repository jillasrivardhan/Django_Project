# 🚀 Django Authentication System

<p align="center">
  <img src="https://img.shields.io/badge/Django-4.x-092E20?style=for-the-badge&logo=django" alt="Django">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite" alt="SQLite">
  <img src="https://img.shields.io/badge/Authentication-Session%20Based-success?style=for-the-badge" alt="Authentication">
</p>

<p align="center">
A beginner-friendly <strong>Django Authentication System</strong> featuring user registration, login, logout, session management, and a protected dashboard. This project demonstrates the fundamentals of building secure user authentication in Django.
</p>

---

# 📖 About

This project is a simple authentication system built using the Django framework. It allows users to register an account, log in securely, access a protected dashboard, and log out using session-based authentication.

It serves as an excellent starting point for learning Django project structure, URL routing, models, views, templates, and session management.

---

# ✨ Features

- 👤 User Registration
- 🔐 User Login
- 🚪 User Logout
- 🗂️ Session-Based Authentication
- 🛡️ Protected Dashboard
- 💾 SQLite Database
- 📱 Responsive User Interface
- 🎯 Beginner-Friendly Project Structure

---

# 📂 Project Structure

```text
Django_Project/
│
├── Django_Project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── my_app/
│   ├── migrations/
│   ├── templates/
│   │   ├── index.html
│   │   ├── Register.html
│   │   ├── Login.html
│   │   ├── dashboard.html
│   │   └── screenshots/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

# 🛠️ Technologies Used

- Python 3.x
- Django
- HTML5
- CSS3
- SQLite3

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/jillasrivardhan/Django_Project.git
```

## 2. Navigate to the Project Folder

```bash
cd Django_Project
```

## 3. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install django
```

or

```bash
pip install -r requirements.txt
```

---

## 5. Apply Database Migrations

```bash
python manage.py migrate
```

---

## 6. Start the Development Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

# 🖥️ Application Workflow

```text
Home Page
     │
     ▼
Register
     │
     ▼
Login
     │
     ▼
Dashboard
     │
     ▼
Logout
```

---

# 📚 Features Demonstrated

- Django Project Structure
- URL Routing
- Models
- Views
- Templates
- Form Handling
- Database Operations
- Session Management
- User Authentication Workflow
- Redirects
- CRUD Fundamentals

---

# 🗃️ Database

The project uses **SQLite**, Django's default lightweight database.

The user model stores:

- Name
- Email
- Password
- Registration Date

---

# 📸 Screenshots

The repository includes screenshots for:

- 🏠 Home Page
- 📝 Registration Page
- 🔑 Login Page
- 📊 Dashboard

You can find them in:

```text
my_app/templates/screenshots/
```

---

# 🎯 Learning Outcomes

After exploring this project, you will understand:

- How Django projects are organized
- Creating models and database tables
- Handling user registration
- Authenticating users
- Managing sessions
- Rendering templates
- Protecting routes
- Building a complete authentication workflow

---

# 🚀 Future Improvements

- 🔒 Password Hashing
- 📧 Email Verification
- 🔑 Password Reset
- 👤 User Profile Page
- ✏️ Edit Profile
- 📸 Profile Image Upload
- Remember Me Option
- Responsive Dashboard
- Django Messages Framework
- Django Authentication System (`django.contrib.auth`)
- PostgreSQL/MySQL Support
- Docker Deployment

---

# 🤝 Contributing

Contributions are welcome!

1. Fork this repository.
2. Create a feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push to your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub. It motivates future improvements and helps others discover the project.

---

# 📄 License

This project is open-source and intended for educational and learning purposes.

---

# 👨‍💻 Author

**Sri Vardhan**

**Python Developer • Django Learner • AI Enthusiast**

Passionate about building full-stack web applications, learning modern backend development, and creating practical projects with Python and Django.

---

<p align="center">

### ⭐ Learn • Build • Deploy • Grow ⭐

**Happy Coding! 🚀**

</p>
