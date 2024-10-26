# Management Application

A Django-based management application that includes employee management, attendance tracking, and basic reporting functionalities.

## Features

- **Employee Management**: Add and manage employee details, including attendance tracking.
- **Attendance Tracking**: Mark attendance for employees on specific dates.
- **Basic Reporting**: Generate reports showing the count of employees in each department.

## Technologies Used

- Django
- Django REST Framework
- SQLite - inbuilt database
- Python 3.x

## Installation

**Note**
To avoid installing dependencies globally, it’s best to use a virtual environment. This project includes a .venv folder, which should be removed and recreated for each developer working on the project. After removing .venv, create a new virtual environment using the commands in Setup, and install dependencies.

Virtual Environment Setup Commands:
   python -m venv .venv
   .venv\Scripts\activate 

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/management_application.git
   cd management_application

2. Install the dependencies in requirements.txt file

3. Run the follwoing commands:
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser - to create django admin (optional)
   python manage.py runserver - to run the localhost.



