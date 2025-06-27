Django Blog Application
A full-featured blog platform built with Django, allowing users to create, manage, and publish blog posts securely and easily.

🔗 Live Demo: https://your-render-app.onrender.com





🚀 Features
🔐 User Authentication
Secure signup with password confirmation

Login/logout functionality

Session management

📝 Blog Management
Create, edit, and delete blog posts

View personal posts (/mypost/)

Browse all public posts (/home/)

🔒 Security
Password hashing

CSRF protection

Ownership verification

Admin privileges for staff

🛠️ Technology Stack
Component	Technology
Backend	Django 4.2 (Python)
Frontend	HTML5 + Bootstrap 5
Database	SQLite (Dev) / PostgreSQL (Prod)
Templates	Django Template Language
Authentication	Django Auth System
Deployment	Render.com

📁 File Structure
<details> <summary><strong>Click to view project structure</strong></summary>
blog_app/
├── blog/                  
│   ├── migrations/        
│   ├── templates/blog/    
│   ├── admin.py           
│   ├── apps.py            
│   ├── models.py          
│   ├── tests.py           
│   ├── urls.py            
│   └── views.py           
├── blog_app/              
│   ├── settings.py        
│   ├── urls.py            
│   └── wsgi.py            
├── manage.py              
└── requirements.txt       
</details>
🧠 Key Components
models.py
python:
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
views.py
Handles authentication (signup, login, logout)

Create, update, delete blog posts

User-specific filtering (My Posts)

Templates
Responsive UI using Bootstrap

Base layout with template inheritance

Dynamic rendering of user content

💻 Installation & Local Setup
bash:
# Clone the repository
git clone https://github.com/yourusername/blog-app.git
cd blog-app

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Run the development server
python manage.py runserver
Visit http://localhost:8000 to access the application.

⚙️ Configuration
Environment Variables (.env)
env

DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
💡 Create a .env file or copy from .env.example.

✨ Usage
👤 User Registration
Visit / to register

Requires username and password

✍️ Creating Posts
Go to /newpost/ after logging in

Enter title and content

📋 Managing Content
View all: /home/

View your own: /mypost/

Edit: /update/<post_id>/

Delete: /delete/<post_id>/

☁️ Deployment (Render)
1. Create a Render Account
Visit render.com

2. Create New Web Service
Connect GitHub repo

Settings:

Runtime: Python 3

Build Command:

bash:
pip install -r requirements.txt && python manage.py collectstatic --noinput
Start Command:

bash:
gunicorn blog_app.wsgi:application
3. Environment Variables
env
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=your-postgresql-url
4. Deploy!
Render builds and deploys automatically.

Visit the URL provided by Render.

🔐 Admin Access
Access Admin Panel
Visit: /admin/

Login using superuser credentials

Manage Site
Blog posts

Users

Activity


🐞 Troubleshooting
Problem	Solution
Static files not loading	Run python manage.py collectstatic
Database issues	Check DATABASE_URL format
Login problems	Ensure superuser is created

🚧 Future Improvements
User profile pages

Comment system

Rich text editor for posts

Password reset functionality

Social media sharing

🤝 Contributing
bash
# Fork the repository
# Create a branch
git checkout -b feature/your-feature

# Commit changes
git commit -am "Add feature"

# Push to GitHub
git push origin feature/your-feature

# Open Pull Request


🙌 Credits
Made with 💻 using Django
Created by Jayavardhan Yerubandi
