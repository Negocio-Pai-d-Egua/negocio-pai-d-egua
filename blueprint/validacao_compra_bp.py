from flask import Blueprint, render_template, request, current_app, redirect, url_for, make_response
from config.model import Carrinho, Produto
from config.serealizer import CarrinhoSchema
from blueprint.produto_bp import criar_produto
from requests import post
validacao_compra_bp = Blueprint("validacao_compra", __name__, template_folder="templates")


@validacao_compra_bp.route("/validacao_compra",methods= ["post"])
def validacao_compra():
    carrinho= request.cookies.get("mesa")
    produto= request.form["produto_id"] or request.cookies.get("produto_id")
    if carrinho:
        carrinho= Carrinho.query.filter(Carrinho.id==int(carrinho)).first()
        produto= Produto.query.filter(Produto.id==int(produto)).first()
        for p in carrinho.produtos:
            if produto.nome == p.nome:
                p.quantidade += 1
                preco_total = float(carrinho.totalpreco) + float(p.preco)
                carrinho.totalpreco = str(preco_total)
                current_app.db.session.commit()
                return redirect(url_for("index.home"))
        novo_produto = {"nome": produto.nome, "preco": produto.preco, "quantidade": 1, "image": produto.image}
        id_novoproduto = criar_produto(novo_produto)
        produto= Produto.query.filter(Produto.id==id_novoproduto).first()
        preco_total = float(carrinho.totalpreco) + float(produto.preco)
        carrinho.totalpreco = str(preco_total)
        carrinho.produtos.append(produto)
        current_app.db.session.commit()
        return redirect(url_for("index.home"))

    else:
        response = make_response(render_template("formulario.html"))
        response.set_cookie("produto_id", produto)
        return response


    return "erro"

@validacao_compra_bp.route("/carrinho")
def carrinho():
    carrinho = request.cookies.get("mesa")
    if carrinho:
        cs = CarrinhoSchema()
        carrinho = Carrinho.query.filter(Carrinho.id == int(carrinho)).first()
        send_carr = []
        quantidade = 0
        for produto in carrinho.produtos:
            quantidade += 1
            send_carr.append({"nome": produto.nome, "preco": produto.preco, "quantidade": produto.quantidade})
        return render_template("carrinho.html", carrinho=send_carr, total=carrinho.totalpreco)
    else:
        return render_template("carrinho.html")
    return {"Error":"Algum problema inesperado ocorreu."}

@validacao_compra_bp.route("/pedido_finalizado", methods= ["post"])
def pedido_finalizado():
    carrinho = request.cookies.get("mesa")
    carrinho = Carrinho.query.filter(Carrinho.id == int(carrinho)).first()
    carrinho.situacao = "Finalizado"
    current_app.db.session.commit()
    return render_template("pedido_finalizado.html")

@validacao_compra_bp.route("/formulario", methods= ["post"])
def formulario():
    return render_template("pedido_finalizado.html")

@validacao_compra_bp.route("/salvando_cookie", methods= ["post"])
def salvando_cookie():
    mesa = request.form.to_dict()
    response = make_response(redirect(url_for("carrinho.validacao_compra"), code=307))
    response.set_cookie("mesa", mesa["mesa"])
    print(mesa)
    return response
