from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

books = [
    {"id": 1, "author": "Роберт Кийосаки", "title": "Богатый папа, бедный папа", "rented": []},
    {"id": 2, "author": "Вадим Зеланд", "title": "Трансерфинг реальности", "rented": []},
    {"id": 3, "author": "Джордж Клейсон", "title": "Самый богатый человек в Вавилоне", "rented": []},
    {"id": 4, "author": "Оскар Хартманн", "title": "Просто делай! Делай просто!", "rented": []},
    {"id": 5, "author": "Сунь Цзы", "title": "Искусство войны", "rented": []},
    {"id": 6, "author": "Айн Рэнд", "title": "Атлант расправил плечи", "rented": []},
    {"id": 7, "author": "Джон Кехо", "title": "Подсознание может всё!", "rented": []},
    {"id": 8, "author": "Роберт Чалдини", "title": "Психология влияния", "rented": []},
    {"id": 9, "author": "Бен Хоровиц", "title": "Легко не будет", "rented": []},
    {"id": 10, "author": "Наполеон Хилл", "title": "Думай и богатей", "rented": []},
    {"id": 11, "author": "Джен Синсеро", "title": "НИ СЫ", "rented": []},
    {"id": 12, "author": "Марк Мэнсон", "title": "Тонкое искусство пофигизма", "rented": []},
    {"id": 13, "author": "Экхарт Толле", "title": "Сила настоящего", "rented": []},
    {"id": 14, "author": "Виктор Франкл", "title": "Сказать жизни 'Да'", "rented": []},
    {"id": 15, "author": "Брайан Моран и Майкл Леннингтон", "title": "12 недель в году", "rented": []},
    {"id": 16, "author": "Брайан Трейси", "title": "Выйди из зоны комфорта", "rented": []},
    {"id": 17, "author": "Дейл Карнеги", "title": "Как перестать беспокоиться и начать жить", "rented": []},
    {"id": 18, "author": "Даниэль Канеман", "title": "Думай медленно... решай быстро", "rented": []},
    {"id": 19, "author": "Валерий Синельников", "title": "Возлюби болезнь свою", "rented": []},
    {"id": 20, "author": "Андрей Курпатов", "title": "Красная таблетка", "rented": []},
    {"id": 21, "author": "Эл Хэлрод", "title": "Магия утра", "rented": []},
    {"id": 22, "author": "Робин Шарма", "title": "Монах, который продал свой 'Феррари'", "rented": []},
    {"id": 23, "author": "Барбара Шер", "title": "Мечтать не вредно", "rented": []},
    {"id": 24, "author": "Роберт Кийосаки", "title": "Квадрант денежного потока", "rented": []},
    {"id": 25, "author": "Джеймс Аллен", "title": "Как человек мыслит", "rented": []},
]

@app.route('/books', methods=['GET'])
def get_books():
    author = request.args.get('author')
    title = request.args.get('title')

    filtered_books = [
        book for book in books if (author and author.lower() in book['author'].lower()) or 
                                    (title and title.lower() in book['title'].lower())
    ]

    if not filtered_books:
        return jsonify({"message": "No books found"}), 404
    
    return jsonify(filtered_books), 200


@app.route('/rent', methods=['POST'])
def rent_book():
    data = request.get_json()
    book_id = data.get('id')
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    if not book_id or not start_date or not end_date:
        return jsonify({"message": "Missing required fields"}), 400

    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        return jsonify({"message": "Invalid date format"}), 400

    book = next((book for book in books if book["id"] == book_id), None)
    if not book:
        return jsonify({"message": "Book not found"}), 404

    for rented in book["rented"]:
        if not (end_date <= rented["start_date"] or start_date >= rented["end_date"]):
            return jsonify({"message": "The book is already rented for these dates"}), 400

    book["rented"].append({"start_date": start_date, "end_date": end_date})

    return jsonify({"message": "Book successfully rented"}), 200


if __name__ == '__main__':
    app.run(debug=True)