from ext import db
from datetime import datetime

class Vencimento(db.Model):
    __tablename__ = 'vencimentos'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), unique=True, nullable=False)
    data_vencimento = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, user_id, data_vencimento):
        self.user_id = user_id
        self.data_vencimento = data_vencimento
