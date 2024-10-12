from flask import Flask
from api.routes import api

# inicializa o flask
app = Flask(__name__)

# as rotas ficam acessíveis a partir de /api
app.register_blueprint(api,url_prefix='/api')

# para rodar localmente
if __name__ == '__main__':
  app.run(debug=True)