
# Week 5 Mini Project: SQL Database and CRUD Operations

This project demonstrates how to connect to an SQLite database, perform CRUD operations, and automate the testing process using GitLab CI/CD.

## Project Overview

This project connects to a SQLite database, performs CRUD (Create, Read, Update, Delete) operations, and demonstrates the use of SQL queries. The project is set up to run in a Continuous Integration/Continuous Deployment (CI/CD) pipeline where the `.db` file is loaded and tested.

## Deliverables

- Python script (`src/main.py`) for CRUD operations
- Test script (`tests/test_main.py`) for unit testing
- `.gitlab-ci.yml` for CI/CD pipeline
- **Screenshot of successful CRUD operations:**

![CRUD Operations Output](crud.png)

## CRUD Operations Explanation

The following operations were performed on the `users` table:

1. **Create**: Inserted two users (`Alice` and `Bob`).
2. **Read**: Retrieved and displayed the users from the database.
   - Output: `[(1, 'Alice', 30), (2, 'Bob', 25)]`
3. **Update**: Updated `Alice` to `Alice Smith` and changed her age to 31.
   - Output after update: `[(1, 'Alice Smith', 31), (2, 'Bob', 25)]`
4. **Delete**: Deleted `Bob` from the table.
   - Output after deletion: `[(1, 'Alice Smith', 31)]`

The operations were successful as shown in the screenshot above. The database was correctly updated at each step.


## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/nogibjj/zichun-miniproject-5.git
   ```

2. Run the Python script:
   ```bash
   python3 src/main.py
   ```

3. Check the `.db` file is created and populated by running:
   ```bash
   sqlite3 week5_project.db
   ```

## CI/CD Pipeline

The GitLab pipeline will automatically run the Python script and log the output for testing the database operations.
