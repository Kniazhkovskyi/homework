from flask import Flask, request, jsonify
import pandas as pd
from datetime import datetime
import os

DATABASE_PATH = os.path.join(os.path.dirname(__file__), '..', 'Milestone_7Ancient', 'database.csv')

app = Flask(__name__)

try:
    df = pd.read_csv(DATABASE_PATH)
    employees = df.to_dict(orient='records')
except Exception as e:
    print(f"Error reading database: {e}")
    employees = []

def convert_date_to_string(date):
    try:
        date_obj = datetime.strptime(date, "%b %d")
    except ValueError:
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            return date_obj.strftime("%b %d")
        except ValueError:
            return None
    return date_obj.strftime("%b %d")

def filter_employees_by_month_and_department(employees, field_name, month, department):
    month = month[:3].capitalize()
    return [
        emp for emp in employees
        if emp.get(field_name) and emp[field_name].startswith(month)
        and emp.get("department", "").lower() == department.lower()
    ]

@app.route('/birthdays', methods=['GET'])
def get_birthdays():
    month = request.args.get('month')
    department = request.args.get('department')
    
    if not month or not department:
        return jsonify({"error": "Missing required parameters"}), 400

    filtered_employees = filter_employees_by_month_and_department(employees, "birthday", month, department)
    
    return jsonify({
        "total": len(filtered_employees),
        "employees": filtered_employees
    })

@app.route('/anniversaries', methods=['GET'])
def get_anniversaries():
    month = request.args.get('month')
    department = request.args.get('department')
    
    if not month or not department:
        return jsonify({"error": "Missing required parameters"}), 400

    filtered_employees = filter_employees_by_month_and_department(employees, "anniversary", month, department)
    
    return jsonify({
        "total": len(filtered_employees),
        "employees": filtered_employees
    })

if __name__ == '__main__':
    # Запуск сервера Flask
    app.run(debug=True)
    