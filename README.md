# Portfolio Website

Modern AI Engineer & Software Engineer portfolio built using Flask, Python, Tailwind CSS, and responsive UI design.

---

# Live Demo

URL:

```text
https://shivang-portfolio.onrender.com
```

---

# Features

- Modern responsive UI
- Dark mode support
- Mobile-friendly navigation
- Resume download
- Skills section
- Experience timeline
- Projects showcase
- Education section
- Contact section
- SEO optimized
- OpenGraph & Twitter metadata
- Flask backend architecture
- YAML-based content management
- Production deployment using Render

---

# Tech Stack

## Backend

- Python
- Flask
- Jinja2

## Frontend

- HTML5
- Tailwind CSS
- JavaScript
- AOS Animation Library
- Lucide Icons
- Font Awesome

## Deployment

- Render
- Gunicorn
- GitHub

---

# Project Structure

```text
portfolio-website/
│
├── app.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── .gitignore
│
├── content/
│   ├── profile.yaml
│   ├── skills.yaml
│   ├── experience.yaml
│   └── education.yaml
│
├── templates/
│   ├── base.html
│   └── index.html
│
├── static/
│   ├── images/
│   ├── resume/
│   └── favicon.ico
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/ShivangModi/portfolio-website.git
```

---

## 2. Navigate To Project

```bash
cd portfolio-website
```

---

## 3. Create Conda Environment

```bash
conda create -n portfolio-env python=3.11 -y
```

---

## 4. Activate Environment

```bash
conda activate portfolio-env
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Locally

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

# Deployment

This project is deployed using:

- GitHub
- Render
- Gunicorn

---

# Deploy On Render

## Build Command

```text
pip install -r requirements.txt
```

## Start Command

```text
gunicorn app:app
```

---

# Environment

Python Version:

```text
Python 3.11
```

---

# SEO Features

- Meta description
- OpenGraph tags
- Twitter card support
- Favicon support
- Responsive design

---

# Future Improvements

- Blog section
- GitHub API integration
- Project filtering
- Contact form backend
- Visitor analytics
- Custom domain
- Docker support
- CI/CD pipeline

---

# Author

## Shivang Modi

AI Engineer & Software Engineer

- GitHub: https://github.com/ShivangModi
- LinkedIn: https://linkedin.com/in/shivang-modi

---

# Acknowledgements

- Flask
- Tailwind CSS
- Lucide Icons
- Font Awesome
- AOS Animation Library
- Render

