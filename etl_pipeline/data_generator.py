import csv
import uuid
import random
from faker import Faker

fake = Faker()

def generate_raw_users(file_path="raw_users.csv", total=10000):
    emails = []

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "user_id",
            "name",
            "email",
            "phone_number",
            "address",
            "signup_date"
        ])

        for _ in range(total):
            user_id = str(uuid.uuid4())
            name = fake.name().strip()

            # 5% duplicate emails
            if random.random() < 0.05 and emails:
                email = random.choice(emails)
            else:
                email = fake.email()
                emails.append(email)

            # 5% missing phone numbers
            phone_number = fake.phone_number() if random.random() > 0.05 else ""

            address = fake.address().replace("\n", ", ").strip()

            # Inconsistent date formats
            signup_date = random.choice([
                fake.date(pattern="%Y-%m-%d"),
                fake.date(pattern="%m/%d/%Y"),
                fake.date(pattern="%B %d, %Y")
            ])

            writer.writerow([
                user_id,
                name,
                email,
                phone_number,
                address,
                signup_date
            ])

    print("✅ raw_users.csv generated successfully")
