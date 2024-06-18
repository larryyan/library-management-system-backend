from flask import request, jsonify, blueprints
from flask.views import MethodView
from models import *


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
        if(BookInfo.query.get(form.get('isbn'))):
            return {
                'status': 'error',
                'message': '数据添加失败'
            }
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


book_info_api = blueprints.Blueprint('book_info', __name__)
bookinfo_view = BookInfoApi.as_view('book_info_api')
book_info_api.add_url_rule('/', defaults={'isbn': None}, view_func=bookinfo_view, methods=['GET'])
book_info_api.add_url_rule('/', view_func=bookinfo_view, methods=['POST'])
book_info_api.add_url_rule('/<int:isbn>', view_func=bookinfo_view, methods=['GET', 'PUT', 'DELETE'])