from flask import request, jsonify, blueprints
from flask.views import MethodView
from models import *


reader_api = blueprints.Blueprint('reader', __name__)


@reader_api.route('/<int:reader_id>/borrows', methods=['GET'])
def get_reader_borrows(reader_id):
    reader = Reader.query.get(reader_id)
    if reader is None:
        return jsonify({'error': 'Reader not found'}), 404

    borrows = Borrow.query.filter_by(reader_id=reader_id).all()
    borrow_data = []
    for borrow in borrows:
        book = Book.query.get(borrow.book_id)
        borrow_data.append({
            'id': borrow.id,
            'book_id': borrow.book_id,
            'book_title': book.info.book_title,
            'borrow_time': borrow.borrow_time,
            'return_time': borrow.return_time
        })

    data = {
        'reader_id': reader.id,
        'reader_name': reader.reader_name,
        'borrows': borrow_data
    }

    return jsonify(data), 200


@reader_api.route('/<int:reader_id>', methods=['GET'])
def get_reader(reader_id):
    reader = Reader.query.get(reader_id)
    if reader is None:
        return jsonify({'error': 'Reader not found'}), 404

    data = {
        'id': reader.id,
        'reader_name': reader.reader_name,
        'reader_department': reader.reader_department,
        'reader_phone': reader.reader_phone
    }

    return jsonify(data), 200