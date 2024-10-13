from ext import db
from datetime import datetime

# Modelo Vencimento para armazenar a data de vencimento de cada usuário
class Vencimento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), unique=True, nullable=False)  # Identificador único do usuário
    data_vencimento = db.Column(db.Date, nullable=False)  # Data de vencimento do usuário

    def __repr__(self):
        return f"<Vencimento {self.user_id} - {self.data_vencimento.strftime('%d/%m/%Y')}>"
