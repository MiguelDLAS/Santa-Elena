from exfabrica import db


class Post(db.model) :
    __tablename__ = 'Posts'
    id = db.colum(db.Integer, primary_key=True)
    author= db.colum(db.Integer, db.Foreigkey('users.id'),nullable=false)
    title = db.column(db.string(100))
    body = db.column(bd.text)
    create = db.column(db.DataTime, nullable=false, default=datetime.utcnow)


    def __init__(self, author, title, body) -> none:
        self.author = username
        self.title = title
        self.body = body

    def __repr__(self) -> str:
        return f'User: {self.title}'
        