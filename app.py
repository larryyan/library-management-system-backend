import json
import secrets

from flask import Flask, request, jsonify

from extension import *
from models import *
from api.book_info import *
from api.books import *
from api.reader import *
from api.borrow import *
from flask_jwt_extended import *


app = Flask(__name__)
app.register_blueprint(book_info_api, url_prefix='/api/book_info')
app.register_blueprint(books_api, url_prefix='/api/book')
app.register_blueprint(reader_api, url_prefix='/api/reader')
app.register_blueprint(borrow_api, url_prefix='/api/borrow')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = "216065749160164515428165282787934462756"
db.init_app(app)
cors.init_app(app)
jwt = JWTManager(app)


@app.route('/api/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    # 这部分需要看下POST请求的格式
    data = request.get_data()
    data = json.loads(data)
    uid = data.get('uid', None)
    password = data.get('password', None)
    if not uid:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    if Reader.query.filter_by(id=uid, reader_password=password).first() is None:
        return jsonify({"msg": "Bad username or password"}), 401
    access_token = create_access_token(identity=uid)
    return jsonify(access_token=access_token), 200


@app.route('/api/protected', methods=['GET'])
@jwt_required()
def protected():
    now_user = get_jwt_identity()
    return jsonify(logged_in_as=now_user), 200


@app.cli.command()
def create():
    db.drop_all()
    db.create_all()
    init_db()


if __name__ == '__main__':
    app.run('127.0.0.1', 5000)
