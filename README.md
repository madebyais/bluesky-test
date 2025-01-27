# bluesky-test

## Overview

This project is a demo of a web app that scrapes all types of Pokemon from the website and saves them into a local database. It also provides an API to retrieve the data from the database.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
  - [Using Docker Compose](#using-docker-compose)
  - [Manual Setup](#manual-setup)
- [Folder Structure](#folder-structure)
- [Troubleshooting](#troubleshooting)

## Requirements

- Python 3.11 or higher
- Docker
- Docker Compose

## Getting Started

### Using Docker Compose

1. Clone the repository, and configure the environment variables
```bash
git clone https://github.com/madebyais/bluesky-test.git
cp .env.example .env
```

2. Run the docker compose
```bash
docker compose up -d
```

3. Access the API
```bash
http://localhost:8000/docs
```

### Manual Setup

1. Clone the repository
```bash
git clone https://github.com/madebyais/bluesky-test.git
```

2. Install the deps, and configure the environment variables
```bash
make install
cp .env.example .env
```

3. Run database migration
```bash
make migrate
```

4. Run the scraper
```bash
make scraper
```

5. Run the API
```bash
make start
```

## Folder Structure

| Folder/File         | Description |
|---------------------|----------------------------------------------|
| DOCUMENTATION.md    | Project documentation and requirements       |
| Dockerfile          | Instructions for building the Docker image   |
| Makefile            | Contains commands for project management     |
| README.md           | Project overview and setup instructions      |
| docker-compose.yaml | Docker Compose configuration file            |
| main.py             | Entry point for the FastAPI application      |
| migrate.py          | Script for database migration                |
| modules/            | Contains the core modules of the application |
| ├── base/           | Base classes and utilities                   |
| ├── pokemon/        | Pokemon-related models, services, and routes |
| └── scraper/        | Web scraping functionality                   |
| resources/          | Additional resources and utilities           |
| scraper.py          | Script for scraping Pokemon data             |
| .env.example        | Example environment variable configuration   |
| requirements.txt    | List of Python dependencies                  |

```text
.
├── DOCUMENTATION.md
├── Dockerfile
├── Makefile
├── README.md
├── docker-compose.yaml
├── main.py
├── migrate.py
├── modules
│   ├── base
│   │   ├── __init__.py
│   │   ├── model.py
│   │   └── router.py
│   ├── pokemon
│   │   ├── __init__.py
│   │   ├── middleware.py
│   │   ├── model.py
│   │   ├── repository.py
│   │   ├── router.py
│   │   └── service.py
│   └── scraper
│       ├── __init__.py
│       └── service.py
├── requirements.txt
├── research.ipynb
├── resources
│   ├── __init__.py
│   └── database.py
├── scraper.py
```

## Troubleshooting

If you have any issues, please open an issue on GitHub.
