from datetime import datetime

def standardize_date(date_str):
    formats = ["%Y-%m-%d", "%m/%d/%Y", "%B %d, %Y"]

    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue

    return None

def transform_data(rows):
    cleaned_rows = []
    seen_emails = set()

    for row in rows:
        email = row["email"].strip()

        # Remove duplicate emails
        if email in seen_emails:
            continue
        seen_emails.add(email)

        row["name"] = row["name"].strip()
        row["email"] = email
        row["address"] = row["address"].strip()

        # Handle missing phone numbers
        row["phone_number"] = row["phone_number"].strip() or None

        # Standardize date
        row["signup_date"] = standardize_date(row["signup_date"])

        cleaned_rows.append(row)

    return cleaned_rows
