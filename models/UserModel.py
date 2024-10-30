from config import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)

    # foreign key ke tabel category
    level_id = db.Column(db.Integer, db.ForeignKey('level.id_level'), nullable=False)

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username':self.username,
            'password': self.password,
            'full_name': self.full_name,
            'status': self.status,
            'level_id' : self.level_id
        }