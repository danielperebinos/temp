# VET Map

## Scope

The purpose of this project is to:

- **Efficiently manage institution data**: Import, store, and retrieve institution details via Django Admin and provide
  API endpoints for accessing this data.
- **Streamline data management**: Allow for seamless import from Excel and editing of institution information.
- **Provide API access**: Expose institution data through DRF APIs for list and retrieve operations.

---

## Architecture Overview

The project consists of the following components:

- **Django Admin**: Customized with the Unfold theme, providing an intuitive interface for managing institutions.
- **Django REST Framework (DRF)**: Exposes API endpoints for listing and retrieving institution data.
- **PostgreSQL**: Serves as the primary database for storing institution data.
- **Nginx**: Used to serve static files and act as a reverse proxy for the Django application.

This architecture ensures scalability, maintainability, and ease of data management.

---

## Local Development

To set up and run the project locally, follow the instructions below:

### 1. Using Docker Compose

- To start the project locally, use the `compose.yaml` file with the following command:
  ```bash
  docker compose up --build -d
  ```
- For running tests, ensure the services are up and configured as needed.

### 2. Local Environment Setup

If you prefer running the project without Docker:

1. Create a Python virtual environment named `.venv`:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # For Windows: .venv\Scripts\activate
   ```
2. Install poetry:
   ```bash
   pip install poetry
   ```
3. Install dependencies:
   ```bash
   poetry install
   ```
3. Run the development server:
   ```bash
   python manage.py runserver
   ```

---

## Environment Variables

To ensure proper functionality, the project requires specific environment variables to be set. These variables should be
defined in a `.env` file and loaded into the application at runtime.

#### **General Configuration**

- **`ENVIRONMENT`**: Defines the environment in which the application runs. Common values are `development`, `staging`,
  or `production`.
- **`SECRET_KEY`**: A secret key used for cryptographic signing in Django. This should be a long, random, and unique
  string.

#### **Database Configuration (PostgreSQL)**

These variables define the connection settings for the PostgreSQL database:

- **`POSTGRES_NAME`**: The name of the database used by Django.
- **`POSTGRES_USER`**: The username for connecting to the database.
- **`POSTGRES_PASSWORD`**: The password associated with the database user.
- **`POSTGRES_HOST`**: The hostname or IP address where PostgreSQL is running. If using Docker, this is typically the
  name of the database service (e.g., `postgres`).
- **`POSTGRES_PORT`**: The port number on which PostgreSQL is running (default is `5432`).

Ensure that these variables are correctly set before starting the application to prevent connection issues.

```env
ENVIRONMENT=development
SECRET_KEY=your_django_secret_key

POSTGRES_NAME=database_name
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_HOST=database_host
POSTGRES_PORT=database_port
```

---

## Branching Model Description

The project follows a standard branching model with the following main branches:

- **`develop`**: The development branch where active development takes place.
- **`stage`**: Used for staging and pre-production testing.
- **`master`**: The production-ready branch containing stable code.

### Branch Naming Conventions

For additional branches, the following naming conventions are used:

- **Feature branches**:\
  Use the prefix `features/` followed by the branch name.\
  Example:
  ```plaintext
  features/name-of-the-branch
  ```
- **Bugfix branches**:\
  Use the prefix `bugfix/` followed by the branch name.\
  Example:
  ```plaintext
  bugfix/name-of-the-branch
  ```

---

### **Deployment Order and Configuration**

Deploying the project requires following a specific order to ensure all components function correctly. The services must
be deployed in the following sequence:

1. **PostgreSQL**
    - Start the PostgreSQL database first.
    - Ensure the necessary environment variables for database connection are set in the `.env` file (
      e.g., `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, etc.).

2. **Django Application**
    - After PostgreSQL is running, deploy the Django application.
    - Django will use the database credentials from the `.env` file to connect to PostgreSQL.
    - Run database migrations and collect static files before starting the application.

3. **Nginx**
    - There is no need to deploy a separate Nginx instance.
    - The configuration must reference the `nginx.conf` file, which handles:
        - Serving static files.
        - Forwarding all other requests to the Django application.

---

### **System Requirements**

To ensure smooth deployment, the virtual machine should meet the following minimum requirements:

- **Operating System**: Linux (Ubuntu 20.04+ recommended)
- **CPU**: At least 2 vCPUs
- **RAM**: Minimum 4GB
- **Disk Space**: At least 20GB of available storage
- **Docker**: Installed and properly configured

Refer to the `compose.yaml` file for additional service orchestration details.