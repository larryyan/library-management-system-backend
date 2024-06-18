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
app.register_blueprint(book_info_api, url_prefix='/book_info')
app.register_blueprint(books_api, url_prefix='/book')
app.register_blueprint(reader_api, url_prefix='/reader')
app.register_blueprint(borrow_api, url_prefix='/borrow')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = "216065749160164515428165282787934462756"
db.init_app(app)
cors.init_app(app)
jwt = JWTManager(app)

"""
@app.route("/login", methods=["POST"])
def login():
    uid = request.json['uid']
    password = request.json['password']

    if not uid:
        return jsonify({"msg": "用户编号丢失"}), 400
    if not password:
        return jsonify({"msg": "用户密码丢失"}), 400

    user = Reader.query.filter_by(reader_id=uid, reader_password=password).first()

    if user is None:
        return jsonify({'success': False, 'message': '用户编号或密码错误'}), 401

    access_token = create_access_token(identity=uid)
    return jsonify({'success': True, 'token': access_token}), 200


@app.route('/verify-token', methods=['POST'])
@jwt_required
def verify_token():
    return jsonify({'success': True}), 200


@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    now_user = get_jwt_identity()
    return jsonify(logged_in_as=now_user), 200
"""

@app.cli.command()
def create():
    db.drop_all()
    db.create_all()
    init_db()


if __name__ == '__main__':
    app.run('127.0.0.1', 5000)
