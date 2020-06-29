from flask import Blueprint, render_template, request, redirect, url_for, make_response
from config.model import Produto, Carrinho



index_bp= Blueprint("index", __name__, template_folder="templates")

@index_bp.route("/")
def home():
    if request.cookies.get("mesa"):
        carrinho= request.cookies.get("mesa")
        carrinho= Carrinho.query.filter(Carrinho.id==int(carrinho))
        return render_template("index.html",situacao=carrinho.situacao)
    else:
        return redirect(url_for("index.selecionar_mesa"))

@index_bp.route("/combinado",methods= ["post"])
def combinado():
    produto_id = int(request.form["prato"])
    produto_query = Produto.query.filter(Produto.id == produto_id).first()
    return render_template("combinado_1.html",combinado=produto_query.nome, preco=produto_query.preco,src=produto_query.image,descricao="kkkkkkk",produto_id=produto_id)

@index_bp.route("/salvando_cookie", methods= ["post"])
def salvando_cookie():
    mesa = request.form.to_dict()
    response = make_response(redirect(url_for("index.home")))
    response.set_cookie("mesa", mesa["mesa"])
    print(mesa)
    return response

@index_bp.route("/selecionar_mesa")
def selecionar_mesa():
    return render_template("formulario.html")