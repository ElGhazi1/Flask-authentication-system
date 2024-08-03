# Flask Web Application

This is a simple Flask web application with user authentication, database interaction, and a basic navigation system.

## Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Routes](#routes)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/flask-web-app.git
    cd flask-web-app
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure the database:
    - Ensure you have MySQL installed and running.
    - Create a database named `flaskapp1_db`.

5. Configure the application:
    - Update `__init__.py` with your database credentials.
    - Add the secret key to `__init__.py`.

## Configuration

In the `__init__.py` file, configure the MySQL database connection:

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskapp1_db'
app.config['MYSQL_PORT'] = 3306
app.config['SECRET_KEY'] = 'your_secret_key' // You can add any string like 'fjkdsjmfkjsqdkj sqmljsmfjsqmlkfdj mlqjerzapeiruzei jqmezapsjflkdfj'

## Usage
### Run the application
In the '/' root directory write this command : `python main.py`

## Project Structure
flask-web-app/
│
├── website/
│   ├── static/
│   │   ├── css/
│   │   │   ├── bootstrap.min.css
│   │   │   └── style.css
│   │   ├── js/
│   │   │   ├── bootstrap.min.js
│   │   │   └── script.js
│   │   └── img/
│   │       └── icon.png
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── contact.html
│   │   ├── about.html
│   │   ├── privacy.html
│   │   ├── login.html
│   │   └── sign_up.html
│   ├── __init__.py
│   ├── auth.py
│   ├── views.py
│   └── models.py
├── .gitignore
├── requirements.txt
└── README.md
