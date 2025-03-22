import requests
import sys

def search_books(author=None, title=None):
    url = 'http://127.0.0.1:5000/books'
    params = {}
    if author:
        params['author'] = author
    if title:
        params['title'] = title

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        books = response.json()
        print(f"Books found: {len(books)}")
        for book in books:
            print(f"- {book['title']} by {book['author']}")
    else:
        print(f"Error: {response.json()['message']}")

def rent_book(book_id, start_date, end_date):
    url = 'http://127.0.0.1:5000/rent'
    data = {
        "id": book_id,
        "start_date": start_date,
        "end_date": end_date
    }
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        print(f"Book rented successfully.")
    else:
        print(f"Error: {response.json()['message']}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python client.py <command> [parameters]")
    else:
        command = sys.argv[1]

        if command == "search":
            if len(sys.argv) == 4:
                search_books(author=sys.argv[2], title=sys.argv[3])
            elif len(sys.argv) == 3:
                search_books(author=sys.argv[2])
            else:
                print("Usage: python client.py search <author> [title]")
        elif command == "rent":
            if len(sys.argv) == 5:
                rent_book(int(sys.argv[2]), sys.argv[3], sys.argv[4])
            else:
                print("Usage: python client.py rent <book_id> <start_date> <end_date>")
        else:
            print("Unknown command")