from flask import Flask, request
from flask.views import MethodView
from nltk import book

from extension import *
from models import Book, BookInfo


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
cors.init_app(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.cli.command()
def create():
    db.drop_all()
    db.create_all()
    Book.init_db()


class BookApi(MethodView):
    def get(self, book_id):
        if not book_id:
            books: [Book] = Book.query.all()
            results = [
                {
                    'id': book.id,
                    'isbn': book.isbn,
                    'book_address': book.book_address,
                    'book_title': book.info.book_title,
                    'book_author': book.info.book_author,
                    'book_publisher': book.info.book_publisher,
                    'book_type': book.info.book_type
                } for book in books
            ]
            return {
                'status': 'success',
                'message': '数据查询成功',
                'results': results
            }
        book: Book = Book.query.get(book_id)
        return {
            'status': 'success',
            'message': '数据查询成功',
            'result': {
                'id': book.id,
                'isbn': book.isbn,
                'book_address': book.book_address,
                'book_title': book.info.book_title,
                'book_author': book.info.book_author,
                'book_publisher': book.info.book_publisher,
                'book_type': book.info.book_type
            }
        }

    def post(self):
        form = request.json
        book = Book()
        book.id = form.get('id')
        book.isbn = form.get('isbn')
        book.book_address = form.get('book_address')
        book_info = BookInfo()
        book_info.isbn = form.get('isbn')
        book_info.book_title = form.get('book_title')
        book_info.book_author = form.get('book_author')
        book_info.book_publisher = form.get('book_publisher')
        book_info.book_type = form.get('book_type')
        book.info = book_info
        db.session.add(book)
        db.session.commit()

        return {
            'status': 'success',
            'message': '数据添加成功'
        }

    def delete(self, book_id):
        book = Book.query.get(book_id)
        db.session.delete(book)
        db.session.commit()

        return {
            'status': 'success',
            'message': '数据删除成功'
        }

    def put(self, book_id):
        form = request.json
        book = Book.query.get(book_id)
        book.isbn = form.get('isbn')
        book.book_address = form.get('book_address')
        book_info = BookInfo.query.get(book.isbn)
        book_info.book_title = form.get('book_title')
        book_info.book_author = form.get('book_author')
        book_info.book_publisher = form.get('book_publisher')
        book_info.book_type = form.get('book_type')
        db.session.commit()

        return {
            'status': 'success',
            'message': '数据更新成功'
        }


class BookInfoApi(MethodView):
    def get(self, isbn):
        if not isbn:
            book_infos: [BookInfo] = BookInfo.query.all()
            results = [
                {
                    'isbn': book_info.isbn,
                    'book_title': book_info.book_title,
                    'book_author': book_info.book_author,
                    'book_publisher': book_info.book_publisher,
                    'book_type': book_info.book_type
                } for book_info in book_infos
            ]
            return {
                'status': 'success',
                'message': '数据查询成功',
                'results': results
            }
        book_info: BookInfo = BookInfo.query.get(isbn)
        return {
            'status': 'success',
            'message': '数据查询成功',
            'result': {
                'isbn': book_info.isbn,
                'book_title': book_info.book_title,
                'book_author': book_info.book_author,
                'book_publisher': book_info.book_publisher,
                'book_type': book_info.book_type
            }
        }

    def post(self):
        form = request.json
        book_info = BookInfo()
        book_info.isbn = form.get('isbn')
        book_info.book_title = form.get('book_title')
        book_info.book_author = form.get('book_author')
        book_info.book_publisher = form.get('book_publisher')
        book_info.book_type = form.get('book_type')
        db.session.add(book_info)
        db.session.commit()

        return {
            'status': 'success',
            'message': '数据添加成功'
        }

    def delete(self, isbn):
        book_info = BookInfo.query.get(isbn)
        db.session.delete(book_info)
        db.session.commit()

        return {
            'status': 'success',
            'message': '数据删除成功'
        }

    def put(self, isbn):
        form = request.json
        book_info = BookInfo.query.get(isbn)
        book_info.book_title = form.get('book_title')
        book_info.book_author = form.get('book_author')
        book_info.book_publisher = form.get('book_publisher')
        book_info.book_type = form.get('book_type')
        db.session.commit()

        return {
            'status': 'success',
            'message': '数据更新成功'
        }


book_view = BookApi.as_view('book_api')
app.add_url_rule('/book/', defaults={'book_id': None}, view_func=book_view, methods=['GET'])
app.add_url_rule('/book/', view_func=book_view, methods=['POST'])
app.add_url_rule('/book/<int:book_id>', view_func=book_view, methods=['GET', 'PUT', 'DELETE'])
bookinfo_view = BookInfoApi.as_view('book_info_api')
app.add_url_rule('/book_info/', defaults={'isbn': None}, view_func=bookinfo_view, methods=['GET'])
app.add_url_rule('/book_info/', view_func=bookinfo_view, methods=['POST'])
app.add_url_rule('/book_info/<int:isbn>', view_func=bookinfo_view, methods=['GET', 'PUT', 'DELETE'])

if __name__ == '__main__':
    app.run('127.0.0.1', 5000)
