# Lofy 🌟

A modern social media platform built with Django that allows users to share posts, images, videos, and connect with friends.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Models](#models)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

Lofy is a full-featured social media platform where users can create and share different types of content including text posts, images, videos, reels, and carousels. The platform includes comprehensive user authentication, social login integration, and privacy controls.

## ✨ Features

### User Authentication & Management
- 🔐 **User Registration & Login** - Complete signup and login system with custom user model
- 📧 **Email Verification** - Automated email confirmation for new accounts
- 🔑 **Password Management** - Password reset and change functionality via email
- 🌐 **Social Authentication** - OAuth integration with Google, GitHub, and Apple ID
- 👤 **Custom User Model** - Extended user profile with phone number and email confirmation status

### Content Management
- 📝 **Multiple Post Types** - Support for:
  - Text posts
  - Image posts
  - Video posts
  - Reels
  - Carousel posts (multiple images)
- 📷 **Media Uploads** - File upload support for images and videos
- 🎵 **Music Integration** - Attach songs to posts
- 📍 **Location Tagging** - Add location information to posts
- 👥 **User Tagging** - Tag other users in posts
- 💬 **Comments System** - Nested comments with replies support
- 👍 **Engagement Tracking** - Likes, comments, shares, and saves counter

### Privacy & Security
- 🔒 **Visibility Controls** - Three visibility levels:
  - Public (everyone)
  - Friends (friends only)
  - Private (only me)
- 🗄️ **Archive Posts** - Archive posts without deleting them
- 🚩 **Report System** - Flag inappropriate content
- 🔐 **Login Required** - Protected views with authentication decorators

### Additional Features
- 📱 **Responsive Design** - Static files included for accounts module
- 📊 **Admin Interface** - Django admin panel for content moderation
- 🗃️ **Database** - SQLite database for development (PostgreSQL ready)
- 🎨 **Custom Forms** - Styled forms with Bootstrap classes

## 🛠️ Tech Stack

### Backend
- **Django 5.2.4** - High-level Python web framework
- **Python 3.x** - Programming language
- **SQLite** - Database (development)
- **PostgreSQL** - Database (production-ready via psycopg2)

### Authentication & Security
- **Django Social Auth** - OAuth integration (social-auth-app-django 5.5.1)
- **PyJWT 2.10.1** - JSON Web Token implementation
- **Cryptography 45.0.5** - Cryptographic recipes and primitives

### Key Dependencies
- **python-dotenv** - Environment variable management
- **Pillow** - Image processing (implied by ImageField usage)
- **requests** - HTTP library for API calls

## 📁 Project Structure

```
Lofy/
├── accounts/                 # User authentication & management
│   ├── models.py            # Custom User model
│   ├── views.py             # Auth views (signup, login, password reset)
│   ├── forms.py             # User forms (signup, login)
│   ├── urls.py              # Auth URL patterns
│   ├── static/              # CSS and JS for auth pages
│   └── templates/           # Auth templates (login, signup, etc.)
├── core/                     # Main application logic
│   ├── models.py            # Post and Comment models
│   ├── views.py             # Core views (home, post creation)
│   ├── forms.py             # Post creation forms
│   ├── urls.py              # Core URL patterns
│   └── templates/           # Core templates
├── lofy/                     # Project settings
│   ├── settings.py          # Django settings & configuration
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI application
├── media/                    # User-uploaded media files
│   └── post_media/          # Post media storage
├── front/                    # Frontend static files
│   └── Lofy-LogIn/          # Login page assets
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── db.sqlite3               # SQLite database
└── README.md                # This file
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Steps

1. **Clone the repository**
```bash
git clone <repository-url>
cd Lofy
```

2. **Create a virtual environment**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a `.env` file in the project root:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True

# Google OAuth
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your-google-client-id
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your-google-client-secret

# GitHub OAuth
SOCIAL_AUTH_GITHUB_KEY=your-github-client-id
SOCIAL_AUTH_GITHUB_SECRET=your-github-client-secret

# Email Configuration (Gmail example)
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

5. **Apply migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create a superuser**
```bash
python manage.py createsuperuser
```

7. **Run the development server**
```bash
python manage.py runserver
```

8. **Access the application**
- Main site: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## ⚙️ Configuration

### Database Configuration

**Development (SQLite - Default):**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
```

**Production (PostgreSQL):**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lofy_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Email Configuration

The project uses Gmail SMTP for sending emails. Configure in settings.py:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

**Note:** For Gmail, you need to use an App Password, not your regular password.

### Social Authentication Setup

#### Google OAuth
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable Google+ API
4. Create OAuth 2.0 credentials
5. Add authorized redirect URIs: `http://localhost:8000/auth/complete/google-oauth2/`
6. Copy Client ID and Secret to `.env`

#### GitHub OAuth
1. Go to GitHub Settings > Developer settings > OAuth Apps
2. Create a new OAuth App
3. Set Authorization callback URL: `http://localhost:8000/auth/complete/github/`
4. Copy Client ID and Secret to `.env`

## 📖 Usage

### Creating a Post

1. Log in to your account
2. Navigate to `/postcreation/`
3. Fill in the post details:
   - Title
   - Caption (optional)
   - Upload media (image/video)
   - Add song name (optional)
   - Add location (optional)
   - Select post type
   - Choose visibility level
4. Submit the form

### Viewing Posts

- Home page displays all public posts in reverse chronological order
- Posts show:
  - Publisher username
  - Title and caption
  - Media content
  - Engagement metrics (likes, comments, shares, saves)
  - Tagged users
  - Publication date

### User Authentication

**Sign Up:**
- Visit `/accounts/signup/`
- Fill in username, email, phone number, and password
- Confirm via email

**Log In:**
- Visit `/accounts/login/`
- Enter username and password
- Or use social login (Google/GitHub)

**Password Reset:**
- Visit `/accounts/password_reset/`
- Enter your email
- Follow the reset link in your email

## 🗄️ Models

### User Model
```python
class User(AbstractUser):
    Phone_Number = CharField(max_length=15)
    email = EmailField()
    email_confirmed = BooleanField(default=True)
```

### Post Model
```python
class Post(models.Model):
    publisher = ForeignKey(User)
    title = CharField(max_length=100)
    caption = TextField()
    media = FileField(upload_to='post_media/')
    song = CharField(max_length=255)
    location = CharField(max_length=255)
    post_type = CharField(choices=POST_TYPE)
    likes_count = PositiveIntegerField(default=0)
    comments_count = PositiveIntegerField(default=0)
    shares_count = PositiveIntegerField(default=0)
    saves_count = PositiveIntegerField(default=0)
    tagged_users = ManyToManyField(User)
    visibility = CharField(choices=VISIBILITY_CHOICES)
    is_archived = BooleanField(default=False)
    is_reported = BooleanField(default=False)
    date_published = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
```

### Comment Model
```python
class Comment(models.Model):
    publisher = ForeignKey(User)
    post = ForeignKey(Post)
    content = TextField()
    parent = ForeignKey('self')  # For nested replies
    likes_count = PositiveSmallIntegerField(default=0)
    replies_count = PositiveSmallIntegerField(default=0)
    edited = BooleanField(default=False)
    date_published = DateTimeField(auto_now_add=True)
```

## 🛣️ API Endpoints

### Authentication
- `GET/POST /accounts/signup/` - User registration
- `GET/POST /accounts/login/` - User login
- `GET /accounts/logout/` - User logout
- `GET/POST /accounts/password_reset/` - Request password reset
- `GET/POST /accounts/password_change/` - Change password
- `GET /accounts/email_confirmtion/<uid>/<token>` - Email verification

### Social Auth
- `GET /auth/login/google-oauth2/` - Google login
- `GET /auth/login/github/` - GitHub login
- `GET /auth/login/apple-id/` - Apple ID login

### Core
- `GET /` - Home page (public posts feed)
- `GET/POST /postcreation/` - Create new post

### Admin
- `GET /admin/` - Django admin panel

## 🔮 Planned Features

Based on the project notes, these features are planned for future implementation:

- 🎵 **Music API Integration** - Select songs from an external API
- 🖼️ **Carousel Feature** - Enhanced multi-image posts
- 🎬 **Enhanced Post Types** - Better differentiation between reels, videos, and images
- 👥 **Advanced User Tagging** - Tag users by username with backend validation

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

## 🙏 Acknowledgments

- Django documentation and community
- Django Social Auth contributors
- All open-source libraries used in this project

---

**Made with ❤️ using Django**
