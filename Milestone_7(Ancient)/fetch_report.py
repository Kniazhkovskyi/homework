import requests
import sys

def fetch_report(month, department):
    url = f"http://127.0.0.1:5000/birthdays?month={month}&department={department}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Report for {department} department for {month} fetched.")
        print(f"Total: {data['total']}")
        print("Employees:")
        for employee in data['employees']:
            print(f"- {employee['birthday']}, {employee['name']}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python fetch_report.py <month> <department>")
    else:
        month = sys.argv[1]
        department = sys.argv[2]
        fetch_report(month, department)