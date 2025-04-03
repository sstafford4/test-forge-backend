# Test Forge Backend

[![Coverage Status](https://coveralls.io/repos/github/ucm-cse-prg/fastapi-app/badge.svg?branch=main)](https://coveralls.io/github/ucm-cse-prg/fastapi-app?branch=main)

This repository is for the back end of the Test Forge project, built using FastAPI, beanie, and MongoDB. 

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
    - [Installation](#installation)
    - [Configuration](#configuration)
    - [MongoDB Initialization](#mongodb-initialization)
    - [Running the Application](#running-the-application)
- [API Reference](#api-reference)
- [Development](#development)
    - [IDE Setup](#ide-setup)
    - [Testing](#testing)
    - [Docker](#docker)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The back-end code includes:

- Asynchronous programming with FastAPI.
- Integration with MongoDB using the Beanie ODM.
- CRUD operations for the Test Forge project.
- A command-line interface (via Typer) for server management.
- Containerization using Docker.
- Testing with pytest and static analysis with ruff.

## Project Structure

```
fastapi-app/
├── app
│   ├── api.py             # API endpoints (GET, POST, PATCH, DELETE)
│   ├── actions.py         # Business logic for CRUD operations
│   ├── cli.py             # CLI commands using Typer
│   ├── config.py          # Application configuration (MongoDB, admin email, etc.)
│   ├── dependencies.py    # Dependency injection and error handling decorators
│   ├── documents.py       # Database document schemas (Beanie and Pydantic models)
│   ├── exceptions.py      # Custom exception classes (e.g., InternalServerError, NotFound)
│   ├── mongo.py           # MongoDB connection initialization and Beanie setup
│   ├── models.py          # Pydantic models for Product and Category
│   └── schemas.py         # Request and response schemas for API endpoints
├── tests
│   ├── conftest.py        # Pytest fixtures (async HTTP client, event loop configuration)
│   └── test_api.py        # API endpoint tests (CRUD operations)
├── Dockerfile             # Containerization instructions for the application
├── docker-compose.yml     # Multi-service configuration (app and MongoDB)
├── requirements.txt       # Python dependencies
├── mypy.ini               # MyPy configuration for static type checking
└── README.md              # Project documentation (this file)
```

## Usage

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ucm-cse-prg/fastapi-app.git
   cd fastapi-app
   ```

2. **Install UV:**

   [Install UV](https://docs.astral.sh/uv/getting-started/installation/)

   For MacOS/Linux, run:

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Install the dependencies:**

   ```bash
   uv sync
   ```

### Configuration

The application configuration is managed in `app/config.py` and can be customized via environment variables or a `.env` file.

Example `.env` file:

```plaintext
MONGODB_URL=mongodb://localhost:27017
PORT=8000
```

### MongoDB Initialization

The MongoDB connection is initialized by the asynchronous `init_mongo()` function in `app/mongo.py`. The recommended way to run MongoDB locally is using Docker:

```bash
docker run -d -p 27017:27017 --name mongodb mongo
```

*Tip: You might need to create a custom network for proper DNS resolution in Docker setups.*

### Running the Application

Before running the application, ensure that MongoDB is installed and running on your machine. You can run the server in development mode with:

```bash
uv run fastapi-app
```

For more options, use:

```bash
uv run fastapi-app --help
```

You can also specify host, port, and MongoDB URL:

```bash
uv run fastapi-app --host <HOST> --port <PORT> --mongodb-url=mongodb://localhost:27017
```

Or, for a development shortcut:

```bash
uv run fastapi dev
```

## API Reference

The API endpoints (defined in `app/api.py`) include:

{{ ADD THESE LATER WHEN YOUVE MADE THEM }} 

You can view the interactive Swagger UI at:  
`http://fastapi-app:8000/docs`  
(Replace `fastapi-app` and port number with your configuration if needed.)

## Development

### IDE Setup

For a better development experience, consider using VSCode with the following extensions:
- Python
- Ruff
- MyPy Type Checker
- Pylance
- Copilot/Copilot Chat
- Docker
- MongoDB for VSCode

### Run the test suite using pytest:

```bash
uv run pytest --cov=app
```

##### Summary of All Tests

This project includes a comprehensive test suite for the API endpoints. The tests cover:

{{ ALSO ADD THIS AS YOU GO }} 

- **Error Handling:**
    - Triggering an internal server error by simulating a disconnect from the database, and verifying the system's error responses.

These tests ensure the reliability and robustness of the API in handling both valid and invalid scenarios.

### Run Ruff linting and static analysis:

```bash
uv run ruff check
```

### Run type checking with MyPy:

```bash
uv run mypy app
```

## Docker

You can build and run the application using Docker:

1. **Build the Docker image:**

   ```bash
   docker build -t fastapi-app .
   ```

2. **Alternatively, use Docker Compose to run both the app and MongoDB:**

   ```bash
   docker-compose up
   ```

## Contributing

Contributions are welcome! To contribute:

- Open an issue or submit a pull request with improvements or bug fixes.
- Follow existing coding standards and include tests when applicable.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
