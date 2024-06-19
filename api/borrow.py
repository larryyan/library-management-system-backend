from datetime import datetime
from flask import request, jsonify, blueprints
from flask.views import MethodView
from models import *


class BorrowApi(MethodView):
    def post(self):
        data = request.get_json()
        reader_id = data.get('reader_id')
        book_id = data.get('book_id')
        borrow_time = datetime.now()
        return_time = data.get('return_time')

        reader = Reader.query.get(reader_id)
        book = Book.query.get(book_id)

        if reader is None or book is None:
            return jsonify({'error': 'Invalid reader or book'}), 400

        borrow = Borrow(reader_id=reader_id, book_id=book_id, borrow_time=borrow_time, return_time=return_time)
        db.session.add(borrow)
        db.session.commit()

        return jsonify({'message': 'Borrow created successfully'}), 201

    def delete(self, book_id, reader_id):
        borrow = Borrow.query.filter_by(book_id=book_id, reader_id=reader_id).first()
        if borrow is None:
            return jsonify({'error': 'Borrow not found'}), 404

        db.session.delete(borrow)
        db.session.commit()

        return jsonify({'message': 'Borrow deleted successfully'}), 200

    def put(self, book_id, reader_id):
        data = request.get_json()
        borrow = Borrow.query.filter_by(book_id=book_id, reader_id=reader_id).first()
        if borrow is None:
            return jsonify({'error': 'Borrow not found'}), 404

        borrow.reader_id = data.get('reader_id')
        borrow.book_id = data.get('book_id')
        borrow.borrow_time = data.get('borrow_time')
        borrow.return_time = data.get('return_time')

        db.session.commit()

        return jsonify({'message': 'Borrow updated successfully'}), 200

    def get(self, reader_id):
        borrows = Borrow.query.filter_by(reader_id=reader_id).all()
        borrow_data = []
        for borrow in borrows:
            borrow_data.append({
                'reader_id': borrow.reader_id,
                'book_id': borrow.book_id,
                'borrow_time': borrow.borrow_time,
                'return_time': borrow.return_time
            })

        return jsonify(borrow_data), 200


borrow_api = blueprints.Blueprint('borrow', __name__)
borrow_view = BorrowApi.as_view('borrow_api')
borrow_api.add_url_rule('/', view_func=borrow_view, methods=['POST'])
borrow_api.add_url_rule('/<int:book_id>/<int:reader_id>', view_func=borrow_view, methods=['DELETE', 'PUT'])
borrow_api.add_url_rule('/<int:reader_id>', view_func=borrow_view, methods=['GET'])