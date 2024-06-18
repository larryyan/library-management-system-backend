from extension import db
from nltk import book


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
    def init_db_books():
        rets = [
            (1, 9787506365437, '书架1', '活着', '余华', '北京作家出版社', '小说'),
            (2, 9787536692930, '书架2', '三体', '刘慈欣', '重庆出版社', '科幻'),
            (3, 9787536692930, '书架1', '三体', '刘慈欣', '重庆出版社', '科幻'),
            (4, 9787536692930, '书架3', '三体', '刘慈欣', '重庆出版社', '科幻'),
            (5, 9787540464083, '书架2', '白夜行', '东野圭吾', '南海出版公司', '悬疑'),
            (6, 9787544270878, '书架1', '百年孤独', '加西亚·马尔克斯', '南海出版公司', '魔幻现实主义'),
            (7, 9787530216781, '书架3', '飘', '玛格丽特·米切尔', '北京十月文艺出版社', '历史小说'),
            (8, 9787020008735, '书架2', '红楼梦', '曹雪芹', '人民文学出版社', '古典小说'),
            (9, 9787108011084, '书架1', '天龙八部', '金庸', '生活·读书·新知三联书店', '武侠小说'),
            (10, 9787544253994, '书架3', '挪威的森林', '村上春树', '上海译文出版社', '爱情小说'),
            (11, 9787530215593, '书架2', '情人', '渡边淳一', '北京十月文艺出版社', '爱情小说'),
            (12, 9787201046693, '书架1', '狼图腾', '姜戎', '天津人民出版社', '生态文学'),
            (13, 9787108009821, '书架3', '福尔摩斯探案集', '柯南·道尔', '生活·读书·新知三联书店', '推理小说'),
            (14, 9787544242516, '书架2', '且听风吟', '村上春树', '上海译文出版社', '爱情小说'),
            (15, 9787532734160, '书架1', '一九八四', '乔治·奥威尔', '上海译文出版社', '反乌托邦'),
            (16, 9787540464094, '书架3', '嫌疑人X的献身', '东野圭吾', '南海出版公司', '推理小说'),
            (17, 9787530209967, '书架2', '万历十五年', '黄仁宇', '生活·读书·新知三联书店', '历史'),
            (18, 9787540455958, '书架1', '三体全集', '刘慈欣', '重庆出版社', '科幻'),
            (19, 9787020042494, '书架3', '平凡的世界', '路遥', '人民文学出版社', '现实主义小说'),
            (20, 9787108010360, '书架2', '射雕英雄传', '金庸', '生活·读书·新知三联书店', '武侠小说')
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


class Borrow(db.Model):
    __tablename__ = 'borrow'
    id = db.Column(db.Integer, primary_key=True)
    reader_id = db.Column(db.ForeignKey('reader.id'))
    book_id = db.Column(db.ForeignKey('books.id'))
    borrow_time = db.Column(db.DateTime, nullable=False)
    return_time = db.Column(db.DateTime, nullable=False)


class Reader(db.Model):
    __tablename__ = 'reader'
    id = db.Column(db.Integer, primary_key=True)
    reader_name = db.Column(db.String(255), nullable=False)
    reader_password = db.Column(db.String(255), nullable=False)
    reader_department = db.Column(db.String(255), nullable=False)
    reader_phone = db.Column(db.String(255), nullable=False)

    @staticmethod
    def init_db_readers():
        rets = [
            (1, '张三', '123456', '计算机学院', '12345678901'),
            (2, '李四', '123456', '计算机学院', '12345678901'),
            (3, '王五', '123456', '计算机学院', '12345678901'),
            (4, '赵六', '123456', '计算机学院', '12345678901')
        ]
        for ret in rets:
            reader = Reader()
            reader.id = ret[0]
            reader.reader_name = ret[1]
            reader.reader_password = ret[2]
            reader.reader_department = ret[3]
            reader.reader_phone = ret[4]
            db.session.add(reader)
        db.session.commit()


def init_db():
    Reader.init_db_readers()
    Book.init_db_books()