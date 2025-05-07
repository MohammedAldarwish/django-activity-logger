# django-activity-logger


## Features

- Logs request method (GET, POST, etc.)
- Logs request path
- Logs IP address
- Logs user agent
- Logs action type based on request method
- Logs response status code
- Logs timestamp
- Compatible with custom user models

## Installation

1. Clone the repository:

```bash
git clone https://github.com/MohammedAldarwish/django-activity-logger.git
```

2. Create a virtual environment and activate it
```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```
3. install the requiremnts
```bash
pip install -r requirements.txt
```
4. Make migrations and migrate
```bash
python manage.py makemigrations
python manage.py migrate
```
