import csv
import argparse
from datetime import datetime


def load_data(file_path):
    employees = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)  # Читаем CSV как словарь
        for row in reader:
            employees.append(row)
    return employees


def filter_by_month(employees, month):
    month = int(month)
    birthdays = []
    hire_anniversaries = []

    for emp in employees:
        birth_month = datetime.strptime(emp["birthday"], "%Y-%m-%d").month
        hire_month = datetime.strptime(emp["hiring_date"], "%Y-%m-%d").month

        if birth_month == month:
            birthdays.append(emp["name"])
        if hire_month == month:
            hire_anniversaries.append(emp["name"])

    return birthdays, hire_anniversaries


def main():
    parser = argparse.ArgumentParser(description="birthday and hiring date.")
    parser.add_argument("file", help="Имя файла базы данных (CSV)")
    parser.add_argument("month", type=int, help="Номер месяца (1-12)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Name")

    args = parser.parse_args()

    employees = load_data(args.file)

    birthdays, hire_anniversaries = filter_by_month(employees, args.month)

    print(f"📅 В {args.month}-м месяце:")
    print(f"🎂 Birthday: {len(birthdays)}")
    print(f"🎉 Hiring date: {len(hire_anniversaries)}")

    if args.verbose:
        if birthdays:
            print("\n🎂 Сотрудники с днем рождения:")
            for name in birthdays:
                print(f"- {name}")

        if hire_anniversaries:
            print("\n🎉 Сотрудники с годовщиной найма:")
            for name in hire_anniversaries:
                print(f"- {name}")


if __name__ == "__main__":
    main()
