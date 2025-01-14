# Flick Share

Modern Django web app for seamless Flickr content sharing

## OverView
<div align="center">
  <img src="https://github.com/user-attachments/assets/e246ff39-531e-447f-863b-ca8ac1a4974a" width="49%" />
  <img src="https://github.com/user-attachments/assets/c98d7f47-e91b-43f6-8b04-2262c33eab91" width="49%" />
</div>
<div align="center">
  <img src="https://github.com/user-attachments/assets/57de34e6-8f23-492d-ad9f-3059cfb88c91" width="49%" />
  <img src="https://github.com/user-attachments/assets/d7775101-e4e4-4fbb-b6d3-9022f15330f0" width="49%" />
</div>
<div align="center">
  <img src="https://github.com/user-attachments/assets/70be54e7-8d7c-424d-9473-0eb51688f09b" width="49%" />
  <img src="https://github.com/user-attachments/assets/dee09401-248f-4331-bf09-0c893578abe8" width="49%" />
</div>
<div align="center">
  <img src="https://github.com/user-attachments/assets/d89d6120-d0f2-46b2-b23a-a85f6c0a0bb7" width="49%" />
  <img src="https://github.com/user-attachments/assets/62ed9514-6f15-4c43-950c-47414bca2538" width="49%" />
</div>
<div align="center">
  <img src="https://github.com/user-attachments/assets/a63575c7-cbd6-4c1c-86de-467c2aecf4ff" width="49%" />
  <img src="https://github.com/user-attachments/assets/49edce3c-2add-4e00-9f41-954fdec0daa3" width="49%" />
</div>

## Features

### Post Management
- Share Flickr posts instantly via web scraping
- Add custom captions to posts
- Edit and delete your own posts
- View posts in a modern, responsive interface

### Social Interaction
- Comment on posts
- Private messaging with encryption
- User following system

### User Management
- Email-based authentication
- Customizable user profiles
- Account settings management
- Secure account deletion option

### Technical Features
- Responsive design across all devices
- Web scraping for Flickr content
- Encrypted messaging system
- HTMX for dynamic interactions
- Modern UI with Tailwind CSS and Alpine.js

## Tech Stack
- Backend: Django 5.1.4
- Frontend: HTMX, Tailwind CSS, Alpine.js
- Database: PostgreSQL
- Additional: Cryptography for message encryption

## Installation

1. Clone the repository
```bash
git clone https://github.com/auriorajaa/flick_share.git
cd flick_share
```

2. Create and activate virtual environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create `.env` file in the `a_core` directory with the following content:
```
ENVIRONMENT=development
SECRET_KEY=your-secret-key
ENCRYPT_KEY=your-encrypt-key
DATABASE_URL=postgres://postgres:your-password@localhost:5432/flick_share_db
```

5. Set up PostgreSQL database
```bash
# Access PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE flick_share_db;

# Exit PostgreSQL
\q
```

6. Run migrations
```bash
python manage.py migrate
```

7. Create admin user
```bash
python manage.py createsuperuser
```

8. Start development server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` to access the application.

## Project Structure
```
flick_share/
├── a_core/         # Main project settings
│   └── .env        # Environment variables
├── ...             # Other folder
├── venv/           # Virtual environment (not in repo)
└── manage.py
```

## Environment Setup

Required environment variables in `a_core/.env`:
- `ENVIRONMENT`: Set to 'development' for local development
- `SECRET_KEY`: Django secret key
- `ENCRYPT_KEY`: Message encryption key
- `DATABASE_URL`: PostgreSQL connection URL

## Note
- Virtual environment (`venv/`) and environment files (`.env`) are not included in the repository
- Make sure PostgreSQL is running before starting the application
- Keep your encryption and secret keys secure

## License

This project is licensed under the MIT License.
