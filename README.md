# BIU Shoes Database Project

This is a database project I built for the "Database Systems" course at Bar-Ilan University.
The goal was to design and implement a complete inventory management system for a shoe store chain ("BIU Shoes") using MySQL and Python.

## What's in this project?
I built a relational database from scratch, covering the entire process:
* Schema Design: Designed normalized tables for shoes, sizes (with conversion logic), customers, and orders.
* Data Generation: Wrote Python scripts to automatically populate the database with mock data.
* Complex Queries: Implemented advanced SQL queries (Joins, Unions, Views) to analyze sales revenue and inventory levels.

## Project Structure
The code is split into 35 specific scripts (as required by the assignment guidelines), each performing a specific task:

* q1.py - Initializing the Database.
* q2 series - Creating the tables (DDL).
* q3 series - Inserting data into the tables.
* q4-q6 - Altering tables and updating data structures.
* q7-q12 - Running business analytics queries (e.g., finding best-selling items, unsold stock).

## Technologies
* Language: Python 3
* Database: MySQL
* Library: mysql-connector-python

## How to run it
1. Clone the repo.
2. Make sure you have a MySQL server running on port 3307 (or change the port in the scripts).
3. Install the connector: pip install mysql-connector-python
4. Run the scripts in order (starting from q1.py).

---
Created by Roee Haim