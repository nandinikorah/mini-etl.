import csv


def extract(file_path):
    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    print(f"Extracted rows: {len(rows)}")
    return rows


if __name__ == "__main__":
    extract("input.csv")