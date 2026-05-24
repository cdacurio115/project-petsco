from datetime import datetime
from myblog import db

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    autor = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.String(50))
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    image = db.Column(db.String(200), nullable=True)

    def __init__(self, author, title, body, image=None):
        self.autor = author
        self.title = title
        self.body = body
        self.image = image

    def __repr__(self):
        return f"Post: {self.title}"