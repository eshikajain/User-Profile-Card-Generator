# User Profile Card Generator

A simple and interactive web application built using **Python Flask, HTML, and CSS** that allows users to create personalized profile cards by entering their details.

## Features

- Enter your full name and short bio.
- Add a profile image using an image URL.
- Include your job role and location.
- Generate a profile card dynamically.
- Display a default avatar when no image is provided.
- Validate user inputs.
- Clean, responsive, and user-friendly interface.

## Technologies Used

- **Python** – Backend programming
- **Flask** – Web framework
- **HTML** – Structure of the application
- **CSS** – Styling and responsive design

## Project Structure

```text
User-Profile-Card-Generator/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
│
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/eshikajain/User-Profile-Card-Generator.git
```

### 2. Navigate to the project folder

```bash
cd User-Profile-Card-Generator
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Flask

```bash
pip install flask
```

### 6. Run the application

```bash
python app.py
```

### 7. Open in browser

Visit:

```text
http://127.0.0.1:5000/
```

## How It Works

1. The user enters profile information in the form.
2. The frontend sends the information to the Flask backend using a POST request.
3. Flask receives and validates the submitted data.
4. The backend passes the profile details to the HTML template.
5. The generated profile card is displayed on the webpage.

## Learning Outcomes

- Understanding Flask application structure.
- Working with GET and POST requests.
- Handling HTML form data.
- Connecting frontend forms with a Python backend.
- Passing dynamic data from Flask to HTML using Jinja2 templates.

## Author

**Eshika Jain**

GitHub: [@eshikajain](https://github.com/eshikajain)
