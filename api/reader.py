from flask import request, jsonify, blueprints
from flask.views import MethodView
from models import *


reader_api = blueprints.Blueprint('reader', __name__)


class Reader(MethodView):

    # 获取读者信息
    def get(self, reader_id):
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

    # 创建读者
    def post(self):
        data = request.get_json()
        reader = Reader()
        reader.reader_name = data.get('reader_name')
        reader.reader_password = data.get('reader_password')
        reader.reader_department = data.get('reader_department')
        reader.reader_phone = data.get('reader_phone')

        db.session.add(reader)
        db.session.commit()

        return jsonify({'message': 'Reader created successfully'}), 201

    # 删除读者
    def delete(self, reader_id):
        reader = Reader.query.get(reader_id)
        if reader is None:
            return jsonify({'error': 'Reader not found'}), 404

        db.session.delete(reader)
        db.session.commit()

        return jsonify({'message': 'Reader deleted successfully'}), 200

    # 更新读者
    def put(self, reader_id):
        data = request.get_json()
        reader = Reader.query.get(reader_id)
        if reader is None:
            return jsonify({'error': 'Reader not found'}), 404

        reader.reader_name = data.get('reader_name')
        reader.reader_department = data.get('reader_department')
        reader.reader_phone = data.get('reader_phone')

        db.session.commit()

        return jsonify({'message': 'Reader updated successfully'}), 200


reader_view = Reader.as_view("reader_api", __name__)
reader_api.add_url_rule('/', view_func=reader_view, methods=['POST'])
reader_api.add_url_rule('/<int:reader_id>', view_func=reader_view, methods=['GET', 'PUT', 'DELETE'])