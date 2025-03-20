from flask import Flask, request, jsonify
import pandas as pd
from datetime import datetime

app = Flask(__name__)

df = pd.read_csv('/Users/kovas/Prjktr/homework/Milestone_7(Ancient)/database.csv')

employees = df.to_dict(orient='records')

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


@app.route('/birthdays', methods=['GET'])
def get_birthdays():
    month = request.args.get('month')
    department = request.args.get('department')
    
    month = month[:3].capitalize()
    filtered_employees = [
        emp for emp in employees
        if emp["birthday"] and emp["birthday"].startswith(month) and emp["department"].lower() == department.lower()
    ]
    
    return jsonify({
        "total": len(filtered_employees),
        "employees": filtered_employees
    })

@app.route('/anniversaries', methods=['GET'])
def get_anniversaries():
    month = request.args.get('month')
    department = request.args.get('department')
    
    month = month[:3].capitalize()
    filtered_employees = [
        emp for emp in employees
        if emp["anniversary"] and emp["anniversary"].startswith(month) and emp["department"].lower() == department.lower()
    ]
    
    return jsonify({
        "total": len(filtered_employees),
        "employees": filtered_employees
    })


if __name__ == '__main__':
    # Запуск сервера Flask
    app.run(debug=True)