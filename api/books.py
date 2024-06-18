from flask import request, jsonify, blueprints
from flask.views import MethodView
from models import *
from sqlalchemy import func


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

    # 添加图书
    def post(self):
        data = request.get_json()
        book = Book()
        book.isbn = data.get('isbn')
        book_info = BookInfo.query.filter_by(isbn=data.get('isbn')).first()
        if book_info is None:
            return jsonify({'error': 'BookInfo not found'}), 404
        book.info = book_info
        book.book_address = data.get('book_address')
        db.session.add(book)
        db.session.commit()

        return jsonify({'status': 'success', 'message': '数据添加成功'}), 200

    # 图书的删除
    def put(self, id):
        data = request.get_json()
        book = Book.query.filter_by(id=id).first()
        if book is None:
            return jsonify({'error': 'Book not found'}), 404
        book.book_address = data.get('book_address')
        book_info = BookInfo.query.filter_by(isbn=data.get('isbn')).first()
        if book_info is None:
            return jsonify({'error': 'BookInfo not found'}), 404
        book.info = book_info

        db.session.commit()

        return jsonify({'status': 'success', 'message': '数据更新成功'}), 200

    def delete(self, id):
        book = Book.query.filter_by(id=id).first()
        isbn = book.isbn
        if book is None:
            return jsonify({'error': 'Book not found'}), 404
        db.session.delete(book)
        db.session.commit()

        return jsonify({'status': 'success', 'message': '数据删除成功'}), 200


books_api = blueprints.Blueprint('books_api', __name__)
book_view = BooksApi.as_view('books_api')
books_api.add_url_rule('/', view_func=book_view, methods=['POST'])
books_api.add_url_rule('/<int:id>', view_func=book_view, methods=['DELETE', 'PUT'])
books_api.add_url_rule('/<int:isbn>', view_func=book_view, methods=['GET'])