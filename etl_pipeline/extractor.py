import csv

def extract_csv(file_path="raw_users.csv"):
    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)
