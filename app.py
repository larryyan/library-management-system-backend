import secrets

from flask import Flask, request, jsonify

from extension import *
from models import *
from api.book_info import *
from api.get_books_by_isbn import *
from api.reader import *
from api.borrow import *
from flask_jwt_extended import JWTManager


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



@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.cli.command()
def create():
    db.drop_all()
    db.create_all()
    init_db()


if __name__ == '__main__':
    app.run('127.0.0.1', 5000)
