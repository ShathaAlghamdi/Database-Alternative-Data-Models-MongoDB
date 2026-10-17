# Database-Alternative-Data-Models-MongoDB

## MongoDB Document Database — Proof of Concept

### Project Overview

This project explores the Document Data Model using MongoDB, Python, PyMongo, and Docker.

The proof of concept demonstrates how MongoDB stores flexible, JSON-like documents and supports basic database operations.

## 🛠️ Technologies & Tools

<p align="left">
  <img src="https://img.shields.io/badge/MongoDB_8.0-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB 8.0" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/Python_3-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3" />
  <img src="https://img.shields.io/badge/PyMongo-00684A?style=for-the-badge&logo=mongodb&logoColor=white" alt="PyMongo" />
</p>


## Getting Started

After cloning or forking this repository, follow the steps below to run the application.

Before starting, make sure you have:

1. Docker Desktop installed and running.
2. Python 3 installed on your computer.

### 1. Check Docker

Open your terminal and check that Docker is installed:

```bash
docker --version
```

Make sure Docker Engine is running:

```bash
docker info
```

### 2. Start MongoDB

Run MongoDB using the official Docker image:

```bash
docker run -d \
  --name holberton-mongo \
  -p 127.0.0.1:27017:27017 \
  -v holberton-mongo-data:/data/db \
  mongo:8.0
```

If the container already exists but is stopped, use:

```bash
docker start holberton-mongo
```

Check the running container:

```bash
docker ps
```

**Note:** This MongoDB setup is intended for local development only.

### 3. Set Up the Python Environment

Make sure you are in your project directory and using the regular terminal, not the MongoDB shell (`mongosh`).

Create a virtual environment to avoid conflicts with other Python projects:

```bash
python3 -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Application

```bash
python main.py
```

The application connects to MongoDB and demonstrates the database operations.

## Features Demonstrated

- Connect to MongoDB with PyMongo
- Insert and retrieve documents
- Flexible document schema
- Nested-field and array queries
- Update nested fields
- Delete documents
- Indexing experiment

## Database Structure

**Database:** `library_db`

**Collection:** `books`

The collection stores book titles, author details, prices, tags, and optional fields such as publisher information.

## Purpose

The goal of this project is to demonstrate MongoDB's document-oriented structure and explore its strengths, limitations, and differences compared with relational databases.