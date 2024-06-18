from extension import db


class BookInfo(db.Model):
    __tablename__ = 'book_info'
    isbn = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(255), nullable=False)
    book_author = db.Column(db.String(255), nullable=False)
    book_publisher = db.Column(db.String(255), nullable=False)
    book_type = db.Column(db.String(255), nullable=False)


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.ForeignKey('book_info.isbn'), nullable=False)
    book_address = db.Column(db.String(255), nullable=False)
    info = db.relationship('BookInfo', backref='info', lazy=True)

    @staticmethod
    def init_db():
        rets = [
            (1, 9787506365437, '书架1', '活着', '余华', '北京作家出版社', '小说'),
            (2, 9787536692930, '书架2', '三体', '刘慈欣', '重庆出版社', '科幻'),
            (3, 9787536692930, '书架1', '三体', '刘慈欣', '重庆出版社', '科幻'),
            (4, 9787536692930, '书架3', '三体', '刘慈欣', '重庆出版社', '科幻')
        ]
        for ret in rets:
            book = Book()
            book_info = BookInfo.query.filter_by(isbn=ret[1]).first()
            if book_info is None:
                book_info = BookInfo()
                book_info.isbn = ret[1]
                book_info.book_title = ret[3]
                book_info.book_author = ret[4]
                book_info.book_publisher = ret[5]
                book_info.book_type = ret[6]
                db.session.add(book_info)
            book.id = ret[0]
            book.book_address = ret[2]
            book.info = book_info
            db.session.add(book)
        db.session.commit()
