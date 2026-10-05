import csv


def extract(file_path):
    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    print(f"Extracted rows: {len(rows)}")
    return rows


def transform(rows):
    cleaned_rows = []

    for row in rows:
        cleaned_rows.append({
            "customer_id": row["customer_id"].strip(),
            "customer_name": row["customer_name"].strip().title(),
            "city": row["city"].strip().title(),
        })

    return cleaned_rows


def load(rows, file_path):
    columns = ["customer_id", "customer_name", "city"]

    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Loaded rows: {len(rows)} into {file_path}")


if __name__ == "__main__":
    raw_rows = extract("input.csv")
    clean_rows = transform(raw_rows)
    load(clean_rows, "output.csv")