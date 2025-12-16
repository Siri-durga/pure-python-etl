@"

\# Pure Python ETL Pipeline



\## Overview

This project implements a complete ETL (Extract, Transform, Load) pipeline using pure Python.

The pipeline generates synthetic user data, introduces controlled data quality issues, applies

data cleaning and transformation logic, and loads the processed data into a SQLite database.



The entire workflow is executable via a command-line interface, making it easy to test,

extend, and evaluate.



---



\## Features

\- Synthetic data generation using Faker

\- CSV-based extraction layer

\- Data validation, cleaning, and deduplication

\- SQLite-based persistent storage

\- Modular ETL architecture

\- CLI-driven execution



---



\## Technology Stack

\- Python 3.x

\- SQLite (via sqlite3)

\- Faker

\- argparse



---



\## Project Structure

pure\_python\_etl/

│

├── etl\_pipeline/

│   ├── \_\_init\_\_.py

│   ├── data\_generator.py   # Generates synthetic raw data

│   ├── extractor.py        # Reads data from CSV

│   ├── transformer.py      # Cleans and transforms data

│   ├── database.py         # Loads data into SQLite

│   └── cli.py              # Command-line interface

│

├── raw\_users.csv            # Generated raw dataset

├── users.db                 # SQLite database

├── requirements.txt

├── pyproject.toml

└── README.md



---



\## Setup Instructions



\### 1. Create Virtual Environment

```powershell

python -m venv venv

venv\\Scripts\\Activate



2. Install Dependencies

powershell

Copy code

pip install -r requirements.txt

CLI Usage

All commands must be executed from the project root directory.



Generate Raw Data

powershell

Copy code

python -m etl\_pipeline.cli generate

Extract Data

powershell

Copy code

python -m etl\_pipeline.cli extract

Transform Data

powershell

Copy code

python -m etl\_pipeline.cli transform

Load Data into Database

powershell

Copy code

python -m etl\_pipeline.cli load

Run Full ETL Pipeline

powershell

Copy code

python -m etl\_pipeline.cli full-pipeline



\##Output Details

The raw CSV contains 10,000 synthetic user records.



Data cleaning removes invalid records and duplicates.



Final row count in the database is reduced due to email-based deduplication.



Cleaned data is stored in users.db under the users table.



\##Design Considerations

The pipeline avoids external ETL frameworks to demonstrate core Python proficiency.



Each stage is modular to allow independent testing and reuse.



CLI-based execution aligns with real-world data engineering workflows.



\#Author

Durga Lalitha Sri Varshitha



