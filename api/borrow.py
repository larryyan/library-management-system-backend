from datetime import datetime
from flask import request, jsonify, blueprints
from flask.views import MethodView
from models import *


borrow_api = blueprints.Blueprint('borrow', __name__)

@borrow_api.route('/', methods=['POST'])
def create_borrow():
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