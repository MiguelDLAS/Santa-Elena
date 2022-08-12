from exfabrica import DataTime


class Post(db.Model) :
    __tablename__ = 'Posts'
    id = db.colum(db.Integer, primary_key=True)
    author= db.colum(db.Integer, db.ForeignKey('users.id'),nullable=false)
    title = db.column(db.string(100))
    body = db.column(bd.text)
    create = db.column(db.DateTime, nullable=false, default=dateTime.utcnow)


    def __init__(self, author, title, body) -> none:
        self.author = username
        self.title = title
        self.body = body

    def __repr__(self) -> str:
        return f'Post: {self.title}'
        