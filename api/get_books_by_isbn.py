from flask import request, jsonify, blueprints
from flask.views import MethodView
from models import *


class BooksApi(MethodView):
    def get(self, isbn):
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

    # 图书的增加
    def post(self):
        data = request.get_json()
        book = Book()
        book_info = BookInfo.query.filter_by(isbn=data.get('isbn')).first()
        book.book_address = data.get('book_address')
        if book_info is None:
            book_info = BookInfo()
            book_info.isbn = data.get('isbn')
            book_info.book_title = data.get('book_title')
            book_info.book_author = data.get('book_author')
            book_info.book_publisher = data.get('book_publisher')
            book_info.book_type = data.get('book_type')
            db.session.add(book_info)
        book.info = book_info
        db.session.add(book)
        db.session.commit()

        return jsonify({'status': 'success', 'message': '数据添加成功'}), 200

    # 图书的删除
    def delete(self, isbn):
        book = Book.query.filter_by(isbn=isbn).first()
        if book is None:
            return jsonify({'error': 'Book not found'}), 404

        db.session.delete(book)
        db.session.commit()

        return jsonify({'status': 'success', 'message': '数据删除成功'}), 200


books_api = blueprints.Blueprint('books_api', __name__)
book_view = BooksApi.as_view('books_api')
books_api.add_url_rule('/', view_func=book_view, methods=['POST'])
books_api.add_url_rule('/<int:isbn>', view_func=book_view, methods=['GET', 'DELETE'])