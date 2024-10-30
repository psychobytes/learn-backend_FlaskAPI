from config import db

class Level(db.Model):
    id_level = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    #relasi dengan tabel book (one-to-many)
    user = db.relationship('User', backref='level', lazy=True)

    def to_dict(self):
        return {
            'id_level': self.id_level,
            'name': self.name
        }