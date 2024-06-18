from flask import request, jsonify, blueprints
from flask.views import MethodView
from models import *


books_api = blueprints.Blueprint('books', __name__)


@books_api.route('/<isbn>', methods=['GET'])
def get_book_by_isbn(isbn):
    book_info = BookInfo.query.filter_by(isbn=isbn).first()
    if book_info is None:
        return jsonify({'error': 'Book not found'}), 404

    books = Book.query.filter_by(isbn=isbn).all()
    book_data = []
    for book in books:
        book_data.append({
            'id': book.id,
            'isbn': book.isbn,
            'book_address': book.book_address
        })

    data = {
        'isbn': book_info.isbn,
        'book_title': book_info.book_title,
        'book_author': book_info.book_author,
        'book_publisher': book_info.book_publisher,
        'book_type': book_info.book_type,
        'books': book_data
    }

    return jsonify(data), 200
