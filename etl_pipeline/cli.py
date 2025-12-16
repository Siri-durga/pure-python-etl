import argparse

from etl_pipeline.data_generator import generate_raw_users
from etl_pipeline.extractor import extract_csv
from etl_pipeline.transformer import transform_data
from etl_pipeline.database import load_to_db


def main():
    parser = argparse.ArgumentParser(
        description="Pure Python ETL Pipeline for Synthetic User Data"
    )

    parser.add_argument(
        "command",
        choices=["generate", "extract", "transform", "load", "full-pipeline"],
        help="ETL command to run"
    )

    args = parser.parse_args()

    if args.command == "generate":
        generate_raw_users()

    elif args.command == "extract":
        data = extract_csv()
        print(f"Extracted {len(data)} records")

    elif args.command == "transform":
        data = extract_csv()
        cleaned = transform_data(data)
        print(f"Transformed {len(cleaned)} records")

    elif args.command == "load":
        data = extract_csv()
        cleaned = transform_data(data)
        load_to_db(cleaned)
        print("Data loaded into users.db")

    elif args.command == "full-pipeline":
        generate_raw_users()
        data = extract_csv()
        cleaned = transform_data(data)
        load_to_db(cleaned)
        print("Full ETL pipeline executed successfully")


if __name__ == "__main__":
    main()
