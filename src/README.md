## Requirements

- Python
- MySQL database
- pip

## Installation

1. Clone the repository:
   git clone https://github.com/zamkovijvitalik/lab6.git
   cd lab6


2. Install dependencies
   pip install -r requirements.txt
   pip install fastapi uvicorn sqlalchemy pymysql

3. Configure the database
   Open database.py and update your MySQL connection string:
   DATABASE_URL = "mysql+pymysql://root@localhost:3306/neutaa"

   Make sure the database neutaa exists. If not, create it using MySQL:
   CREATE DATABASE neutaa;

4. Run the API server
   uvicorn main:app --reload
   Once the server is running, you can access:
   http://127.0.0.1:8000/docs