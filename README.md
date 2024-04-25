# Backend

Welcome to the backend of the Planteria application, powered by Django version 5.0.4.

## Table of Contents

- [Packages](#packages)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Roadmap](#roadmap)

## Packages

The following packages are utilized for this project:

- **djangorestframework:** 1.11.3
- **django-cors-headers:** 4.3.1
- **psycopg[binary]:** 3.1.18
- **python-dotenv:** 16.0.0
- **PyJWT:** 2.8.0

## Features

These features are integrated into this project:

- **RESTful API:** Allows communication with the frontend with versioning support.
- **CORS:** Cross-Origin Resource Sharing enabled for localhost and 127.0.0.1 during development.
- **PostgreSQL Integration:** Utilizing the PostgreSQL database for data management.
- ~~**Initial Data Population:** Preparing your database with essential initial data for smooth operation.~~
- **Authentication and Authorization:** Secure JWT token-based authentication and authorization mechanism.

## Installation

### Docker
Execute the `docker-compose.yml` file at the root. It will automatically start the backend and database servers.

### Alternative
If you decide not to use Docker, then make sure to replace all environment variables in the backend project.

1. For CORS:
    - `CLIENT_IP`, `CLIENT_PORT` 
    - Used in `settings.py` to determine which origins are allowed to interact with the backend.
2. For PostgreSQL:
    - `POSTGRES_HOST`, `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_PORT`
    - Used in `settings.py` for the database connection.
3. For Django Admin Dashboard:
    - `DJANGO_SUPERUSER_EMAIL`, `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_PASSWORD`
    - Used in `entrypoint.sh` to create a superuser for the Django admin dashboard.
4. For JWT Auth:
    - `DJANGO_JWT_SECRET`
    - Used to encode and decode the JWT token used for user authentication and authorization.

Using conda/pip, run:
```bash
pip install -r requirements.txt
```
## Usage

### Django
If you are using Docker, then all servers should already be up and running. The links to the servers will be shown in the terminal.

For the backend, something like this:

```bash
api-1               | Starting development server at http://0.0.0.0:8000/
```
Accessible by going to http://localhost:8000/. You will encounter a 404 page not found error, and all available endpoints will be listed:

1. `admin/`
1. `api/v1/`

### Database

#### Docker
If you are using Docker, you should see an output like this when PGAdmin is running:
```bash
pgadmin4_container  | [INFO] Listening at: http://[::]:80
```

Accessible by going to http://localhost:8888/.


1. Log in with the predefined credentials from the .env file.
2. Click on "Add New Server".
3. Set a name for the server in the General tab, i.e. AppName.
4. In the Connection tab, do the following mapping:
    - Host name/address = POSTGRES_HOST
    - Port = POSTGRES_PORT
    - Maintenance database = POSTGRES_DB
    - Username = POSTGRES_USER
    - Password = POSTGRES_PASSWORD
5. Click save, and your PostgreSQL-Database should appear in the Object Explorer on the left.

#### Non-Docker
If Docker isn't your preferred choice or isn't available, you can still run the backend. Make sure you have adjusted the configuration for the database connection. Follow these steps:


1. **Generate SQL queries:**
    ```bash
    python manage.py makemigrations
    ```

2. **Execute SQL queries:**

    ```bash
    python manage.py migrate
    ```

3. **Create Superuser for Admin Dashboard:**
    
    ```bash
    python manage.py createsuperuser --name admin --email admin@example.com
    ```
    A prompt will pop-up asking for a password.

4. **Populate Initial Data (if required):**

    TODO

5. **Run the server:**
    ```bash
    python manage.py runserver
    ```

This command will first create all necessary queries based on the Django project files and execute them. Afterwards, a superuser is created so you can access the Admin Dashboard of Django. Finally, the database server is run.


## Endpoints
The prefix for the API is `api/v1`.

1. ``api/v1/plants``
2. ``api/v1/plants/<int:id>``
3. ``api/v1/auth/register``
4. ``api/v1/auth/login``
5. ``api/v1/auth/logout``
6. ``api/v1/user``

## Roadmap
- [ ] Implement Swagger for API documentation
- [ ] Add AI for object detection of plants
    - [ ] If possible, add suggestions like interval of irrigation, exposure to sunlight

- [ ] More