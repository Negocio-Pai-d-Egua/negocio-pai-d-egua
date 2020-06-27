from flask import Blueprint, render_template, request, make_response, redirect, url_for
from config.model import Produto


index_bp= Blueprint("index", __name__, template_folder="templates")

@index_bp.route("/")
def home():
    return render_template("index.html")

@index_bp.route("/combinado", methods = ["post"])
def combinado():
    produto_id = int(request.form["prato"])
    produto_query = Produto.query.filter(Produto.id == produto_id).first()
    return render_template("combinado_1.html", combinado=produto_query.nome, preco=produto_query.preco,src=produto_query.image,descricao="(Descrição do produto.)", produto_id=produto_id)

@index_bp.route("/mesa/<m>")
def mesa(m):
    response = make_response(redirect(url_for("index.home")))
    response.set_cookie("mesa", m)
    return response