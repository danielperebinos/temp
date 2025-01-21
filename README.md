# VET Map

## Scope

The purpose of this project is to:

- **Efficiently manage institution data**: Import, store, and retrieve institution details via Django Admin and provide API endpoints for accessing this data.
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

The following environment variables need to be configured for the project to work correctly:

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

## Services to Deploy and How

The project includes the following services:

- **Django Application**: Manages the backend logic and API endpoints.
- **PostgreSQL**: Stores all project data.
- **Nginx**: Serves static files and acts as a reverse proxy for the Django application.

For deploying these services:

- Use Docker Compose to manage and deploy services.
- Ensure environment variables are correctly configured in your `.env` file.

Refer to the `compose.yaml` file for further details on how services are orchestrated.

