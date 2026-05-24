from myblog import db

class Adopcion(db.Model):
    __tablename__ = "adopciones"
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    post = db.relationship("Post", backref="adopcion")
    user = db.relationship("User", backref="adopcion")