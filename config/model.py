import click
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
db= SQLAlchemy()
def configure(app):
    db.init_app(app)
    app.db= db


class Carrinho(db.Model):
    __tablename__ = 'carrinho'
    id=db.Column(db.Integer, primary_key=True)
    mesa=db.Column(db.Integer, nullable=False)
    totalpreco= db.Column(db.String(200), nullable=False)
    produtos=db.relationship("Produto", backref="carrinho", lazy="select")


class Produto(db.Model):
    __tablename__= 'produto'
    id = db.Column(db.Integer, primary_key=True)
    nome=db.Column(db.String(200), nullable=False)
    preco= db.Column(db.String(200), nullable=False)
    quantidade= db.Column(db.Integer, nullable=False)
    image= db.Column(db.String(200), nullable=False)
    carrinho_id= db.Column(db.Integer, db.ForeignKey("carrinho.id"))

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()