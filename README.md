# 🌸 FormaCV – Smart Resume Builder

FormaCV is a modern and elegant **resume builder web application** built with **Django**, **Tailwind CSS**, and **JavaScript**.  
It allows users to **create**, **edit**, and **preview resumes in real-time**, similar to professional platforms like [FlowCV](https://flowcv.io).

---

## ✨ Features

✅ **Live Resume Preview** – Instantly see updates as you type  
✅ **Dynamic Sections** – Add multiple education, experience, and project entries  
✅ **Clean UI** – TailwindCSS-based modern and minimal interface  
✅ **Resume Export** – Generate beautiful downloadable PDF resumes  
✅ **Profile Photo Cropper** – Upload and crop your profile photo perfectly  
✅ **Responsive Design** – Works seamlessly on desktop and mobile  
✅ **Django-Powered Backend** – Manage all data with Django models  
✅ **Modular Setup** – Uses npm + Django for flexible and efficient development

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-------------|
| **Backend** | Django 5+ |
| **Frontend** | HTML, CSS, JavaScript, Tailwind CSS |
| **Styling Tools** | PostCSS, Autoprefixer |
| **Forms** | Django Crispy Forms (Bootstrap 5) |
| **Database** | SQLite (default) |
| **Build Tools** | npm + Tailwind CLI |

---

## ⚙️ Project Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/FormaCV.git
cd FormaCV
```

### 2️⃣ Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Install Tailwind CSS via npm
```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

### 5️⃣ Configure Tailwind
In your `tailwind.config.js`, make sure content paths look like this:
```js
content: [
  './templates/**/*.{html,js}',
  './resume/templates/**/*.{html,js}',
  './resume/static/js/*.js'
]
```

---

## 🎨 Development Workflow

When working locally, use **two terminals** 👇  

### 🧩 Terminal 1 — Run Django Server
```bash
python manage.py runserver
```

### 💅 Terminal 2 — Watch Tailwind Changes
```bash
npm run build
```

> 💡 This keeps Tailwind watching for changes and recompiling CSS automatically.

If you just want a production build once:
```bash
npx tailwindcss -i ./resume/static/css/styles.css -o ./resume/static/css/output.css --minify
```

---

## 📁 Folder Structure

```
FormaCV/
├── config/                # Django project configuration
├── resume/                # Core app (models, views, static, templates)
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── templates/
│   │   └── builder.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/
│   └── base.html
├── staticfiles/           # Collected static files for production
├── manage.py
├── package.json
└── tailwind.config.js
```

---

## 🧠 How It Works

FormaCV lets users visually build resumes step-by-step:

1. **Personal Information** – Add your name, title, photo, and about section.  
2. **Add Education, Experience, and Projects** – Dynamically add multiple entries.  
3. **Instant Preview** – See all updates live as you type or upload.  
4. **Export PDF** – Generate a polished and professional resume document.  

Everything is powered by Django’s backend and rendered in real-time with Tailwind CSS and JavaScript.

---

## 🧩 Core Models

| Model | Description |
|--------|--------------|
| `Resume` | Root model representing each CV |
| `PersonalDetail` | Stores name, contact info, photo, and bio |
| `Education` | Degree, school, years, and description |
| `Experience` | Job title, company, duration, and details |
| `Project` | Project title, subtitle, and description |

---

## 🧾 Common Commands

| Command | Description |
|----------|-------------|
| `python manage.py runserver` | Start Django local development server |
| `python manage.py makemigrations` | Create new database migrations |
| `python manage.py migrate` | Apply database migrations |
| `npm run build` | Run Tailwind in watch mode |
| `python manage.py collectstatic` | Collect all static files for deployment |

---

## 🚀 Deployment Guide

### 1️⃣ Build Tailwind for Production
```bash
npx tailwindcss -i ./resume/static/css/styles.css -o ./resume/static/css/output.css --minify
```

### 2️⃣ Update Django Settings
In `settings.py`:
```python
DEBUG = False
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

### 3️⃣ Collect Static Files
```bash
python manage.py collectstatic
```

### 4️⃣ Deploy to Server
You can deploy FormaCV on:
- [Render](https://render.com)
- [Railway](https://railway.app)
- [Vercel](https://vercel.com)
- [DigitalOcean](https://www.digitalocean.com)

---

## 💡 Features Roadmap

🟢 v1.0  
- [x] Resume Builder Base  
- [x] Live Preview  
- [x] Add Multiple Entries  
- [x] Export PDF  

🟡 v1.5  
- [ ] Add Skill Section  
- [ ] Theme Selector (Light/Dark Templates)  
- [ ] Editable Fonts and Colors  

🔵 v2.0  
- [ ] User Accounts & Authentication  
- [ ] Save/Load Resumes in Cloud  
- [ ] Public Resume Link Sharing  

---

## 🧑‍💻 Author

**Rizwan**  
📧 [mrizwan.sammo@gmail.com](mailto:mrizwan.sammo@gmail.com)  
💼 [ZeroByte Security](https://mixprobd.com)  
🧠 Developer & Designer of FormaCV  

---

## 🤝 Contributing

Contributions are always welcome!  
Here’s how you can help:

1. Fork this repository  
2. Create a new branch (`git checkout -b feature-name`)  
3. Make your changes and commit (`git commit -m "Add: New feature"`)  
4. Push to your fork (`git push origin feature-name`)  
5. Submit a Pull Request 🎉

---

## 🪪 License

This project is licensed under the **MIT License** — free to use, modify, and share with credit.

---

## 🌟 Support

If FormaCV helps you build your resume faster and easier, please **⭐ star this repository** on GitHub.  
It motivates continued development and future improvements!

---

> _FormaCV – A clean, fast, and modern way to build your professional resume._
