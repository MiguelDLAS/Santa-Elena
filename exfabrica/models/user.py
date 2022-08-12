from exfabrica import db


class User(db.model) :
    __tablename__ = 'users'
    id = db.colum(db.Integer, primary_key=True)
    username = db.column(db.string(50))
    password = db.column(bd.text)

    def __init__(self, username, password) -> none:
        self.username = username
        self.password = password

    def __repr__(self) -> str:
        return f'User: {self.username}'
        