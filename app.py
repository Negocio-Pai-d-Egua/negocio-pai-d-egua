import os
from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
from config.model import configure as config_db
from flask_migrate import Migrate
from config.serealizer import configure as config_ma
from blueprint.index_bp import index_bp
from blueprint.carrinho_bp import carrinho_bp
from blueprint.validacao_compra_bp import validacao_compra_bp
from blueprint.produto_bp import  produto_bp
from blueprint.pedidos_bp import pedidos_bp

app = Flask(__name__)

cors = CORS(app, resource={r"/*": {"origins": "*"}})

#@app.route("/", methods=['GET'])

#def main():
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host="0.0.0.0", port=port)

DB_URL = 'postgresql+psycopg2://{user}:{passw}@{port}/{db}'.format(user="postgres", passw="paidegua;", port="localhost", db="postgres")

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

app.config['SECRET_KEY'] = 'secret'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #silence the deprecation warning

config_db(app)
config_ma(app)
Migrate(app, app.db)
app.register_blueprint(index_bp)
app.register_blueprint(carrinho_bp)
app.register_blueprint(validacao_compra_bp)
app.register_blueprint(produto_bp)
app.register_blueprint(pedidos_bp)

if __name__ == "__main__":
    app.run(port=5000)