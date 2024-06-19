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
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.ForeignKey('book_info.isbn'), nullable=False)
    book_address = db.Column(db.String(255), nullable=False)
    info = db.relationship('BookInfo', backref='info', cascade='all, delete', uselist=False)

    @staticmethod
    def init_db_books():
        rets = [
            (1, 9787506365437, '书架1', '活着', '余华', '北京作家出版社', '文学'),
            (2, 9787536692930, '书架2', '三体', '刘慈欣', '重庆出版社', '科幻'),
            (3, 9787536692930, '书架1', '三体', '刘慈欣', '重庆出版社', '科幻'),
            (4, 9787536692930, '书架3', '三体', '刘慈欣', '重庆出版社', '科幻'),
            (5, 9787540464083, '书架2', '白夜行', '东野圭吾', '南海出版社', '悬疑'),
            (6, 9787544270878, '书架1', '百年孤独', '加西亚·马尔克斯', '南海出版社', '文学'),
            (7, 9787530216781, '书架3', '飘', '玛格丽特·米切尔', '北京十月文艺出版社', '文学'),
            (8, 9787020008735, '书架2', '红楼梦', '曹雪芹', '人民文学出版社', '文学'),
            (9, 9787108011084, '书架1', '天龙八部', '金庸', '生活·读书·新知三联书店', '文学'),
            (10, 9787544253994, '书架3', '挪威的森林', '村上春树', '上海译文出版社', '文学'),
            (11, 9787530215593, '书架2', '情人', '渡边淳一', '北京十月文艺出版社', '文学'),
            (12, 9787201046693, '书架1', '狼图腾', '姜戎', '天津人民出版社', '文学'),
            (13, 9787108009821, '书架3', '福尔摩斯探案集', '柯南·道尔', '生活·读书·新知三联书店', '推理'),
            (14, 9787544242516, '书架2', '且听风吟', '村上春树', '上海译文出版社', '文学'),
            (15, 9787532734160, '书架1', '一九八四', '乔治·奥威尔', '上海译文出版社', '文学'),
            (16, 9787540464094, '书架3', '嫌疑人X的献身', '东野圭吾', '南海出版社', '推理'),
            (17, 9787530209967, '书架2', '万历十五年', '黄仁宇', '生活·读书·新知三联书店', '历史'),
            (18, 9787540455958, '书架1', '三体全集', '刘慈欣', '重庆出版社', '科幻'),
            (19, 9787020042494, '书架3', '平凡的世界', '路遥', '人民文学出版社', '文学'),
            (20, 9787108010360, '书架2', '射雕英雄传', '金庸', '生活·读书·新知三联书店', '文学'),
            (21, 9787115275790, '书架1', 'C++primer中文版', 'Stanley B. Lippman', '人民邮电出版社', '计算机'),
            (22, 9787111128069, '书架3', 'Java编程思想', 'Bruce Eckel', '机械工业出版社', '计算机'),
            (23, 9787115249494, '书架2', '深入理解计算机系统', 'Randal E.Bryant', '机械工业出版社', '计算机'),
            (24, 9787115221704, '书架1', '计算机网络', 'James F.Kurose', '机械工业出版社', '计算机'),
            (25, 9787302423287, '书架3', '数据库系统概念', 'Abraham Silberschatz', '机械工业出版社', '计算机'),
            (26, 9787115473578, '书架2', 'Python编程从入门到实践', 'Eric Matthes', '人民邮电出版社', '计算机'),
            (27, 9787111558422, '书架1', '重构-改善既有代码的设计', 'Martin Fowler', '人民邮电出版社', '计算机'),
            (28, 9787115324429, '书架3', '算法导论', 'Thomas H.Cormen', '机械工业出版社', '计算机')
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