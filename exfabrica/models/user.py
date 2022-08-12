from exfabrica import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.column(db.Integer, primary_key=True)
    username = db.column(db.string(50))
    password = db.column(bd.Text)

    def __init__(self, username, password) -> none:
        self.username = username
        self.password = password

    def __repr__(self) -> str:
        return f'User: {self.username}'
        