from flask import Blueprint, render_template, request, current_app, redirect, url_for, make_response
from config.model import Carrinho, Produto
from requests import post
validacao_compra_bp = Blueprint("validacao_compra", __name__, template_folder="templates")


@validacao_compra_bp.route("/validacao_compra",methods= ["post"])
def validacao_compra():
    carrinho= request.cookies.get("carrinho_id")
    produto= request.form["produto_id"] or request.cookies.get("produto_id")
    if carrinho:
        carrinho= Carrinho.query.filter(Carrinho.id==int(carrinho)).first()
        produto= Produto.query.filter(Produto.id==int(produto)).first()
        carrinho.produtos.append(produto)
        current_app.db.session.commit()
        return redirect(url_for("index.home"))
    else:
        carrinho = {"mesa": 11, "totalpreco": 0}
        response=make_response(redirect(url_for("carrinho.create_carrinho",jcarrinho),code=307))
        response.set_cookie("produto_id",produto)
        return response


    return "erro"

@validacao_compra_bp.route("/carrinho")
def carrinho():

    return render_template("carrinho.html")

@validacao_compra_bp.route("/pedido_finalizado", methods= ["post"])
def pedido_finalizado():

    return render_template("pedido_finalizado.html")

@validacao_compra_bp.route("/formulario", methods= ["post"])
def formulario():
    return render_template("formulario.html")