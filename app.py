from flask import Flask
from ext import db
from api.routes import api

# inicializa o flask
app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vencimentos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db.init_app(app)

# Blueprint da API
app.register_blueprint(api, url_prefix='/api')

# para rodar localmente
if __name__ == '__main__':
  with app.app_context():
    db.create_all()
  app.run(debug=True)