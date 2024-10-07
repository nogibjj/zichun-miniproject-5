
# Week 5 Mini Project: SQL Database and CRUD Operations

This project demonstrates how to connect to an SQLite database, perform CRUD operations, and automate the testing process using GitLab CI/CD.

## Project Overview

This project connects to a SQLite database, performs CRUD (Create, Read, Update, Delete) operations, and demonstrates the use of SQL queries. The project is set up to run in a Continuous Integration/Continuous Deployment (CI/CD) pipeline where the `.db` file is loaded and tested.

## Deliverables

- Python script (`main.py`) for CRUD operations
- Test script (`test_main.py`) for unit testing
- `.gitlab-ci.yml` for CI/CD pipeline
- **Screenshot or of successful database operations:**

![CRUD Operations Log](screenshot_log.png)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/YOUR_REPO_NAME.git
   ```

2. Run the Python script:
   ```bash
   python3 main.py
   ```

3. Check the `.db` file is created and populated by running:
   ```bash
   sqlite3 week5_project.db
   ```

## CI/CD Pipeline

The GitLab pipeline will automatically run the Python script and log the output for testing the database operations.
