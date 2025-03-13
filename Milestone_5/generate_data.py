import csv
import random
from faker import Faker

fake = Faker()

# spisok otdelov
departments = ["Admin", "Uristu", "Management", "Finance", "IT", "Operations"]

# sotrudniki
num_employees = 100

with open("database.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "hiring_date", "department", "birthday"])

    for _ in range(num_employees):
        name = fake.name()
        hiring_date = fake.date_between(start_date="-10y", end_date="today")
        department = random.choice(departments)
        birthday = fake.date_of_birth(minimum_age=25, maximum_age=60)

        writer.writerow([name, hiring_date, department, birthday])

print(f"✅ Файл 'database.csv' успешно создан с {num_employees} сотрудниками!")
