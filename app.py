from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.routes import api

# inicializa o flask
app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://vencimentos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

# Blueprint da API
app.register_blueprint(api, url_prefix='/api')

# as rotas ficam acessíveis a partir de /api
app.register_blueprint(api,url_prefix='/api')

# para rodar localmente
if __name__ == '__main__':
  app.run(debug=True)