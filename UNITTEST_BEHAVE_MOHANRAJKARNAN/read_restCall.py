import requests

def fetch_book_data(bookId):
    """
    This method will get book id as input and return json.
    """
    url=f'https://openlibrary.org/books/{bookId}.json'
    try:
        return requests.get(url=url, verify=False)
    except Exception as e:
        print(f"This exception has raised from read_restCall.py {e}")
    