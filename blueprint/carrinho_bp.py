from flask import Blueprint, render_template, request, current_app, make_response, redirect, url_for
from config.model import Produto, Carrinho
from config.serealizer import ProdutoSchema, CarrinhoSchema
from blueprint.produto_bp import remover_produto
import json

carrinho_bp= Blueprint("carrinho", __name__, template_folder="templates")


@carrinho_bp.route("/create_carrinho", methods= ["post"])
def create_carrinho():
    cs = CarrinhoSchema()
    carrinho =request.args.get("carrinho")
    carrinho = eval(carrinho)
    carrinho = cs.load(carrinho)
    current_app.db.session.add(carrinho)
    current_app.db.session.commit()
    response=make_response(redirect(url_for("validacao_compra.validacao_compra"), code=307))
    response.set_cookie("carrinho_id", str(carrinho.id))
    return response

@carrinho_bp.route("/read_carrinho")
def read_carrinho():
    cs=CarrinhoSchema(many=True)
    result= Carrinho.query.all()
    return cs.jsonify(result)

@carrinho_bp.route("/update_carrinho")
def update_carrinho():
    id= request.args.get('id')
    cs=CarrinhoSchema(many=True)
    query=Carrinho.query.filter(Carrinho.id==id)
    query.update(request.json)
    current_app.db.session.commit()
    return ...

@carrinho_bp.route("/delete_carrinho/<id>", methods=["get"])
def delete_carrinho(id):
    id = int(id)
    print(id)
    cs = CarrinhoSchema(many=True)
    Carrinho.query.filter(Carrinho.id == id).delete()
    current_app.db.session.commit()
    return "OK"

@carrinho_bp.route("/mostrar_pedido")
def mostrar_pedido():
    carrinho = CarrinhoSchema(many = True)
    result = Carrinho.query.all()
    carrinhos = {}
    for c in result:
        nome = "Mesa " + str(c.mesa)
        carrinhos[nome] = {"pedidos":[], "total":c.totalpreco, "situacao": c.situacao}
        for p in c.produtos:
            total = float(p.preco)*p.quantidade
            pedido = {"nome": p.nome, "quantidade":p.quantidade, "preco": p.preco, "total": total}
            carrinhos[nome]["pedidos"].append(pedido)

    return render_template("gerenciamento.html", carrinhos=carrinhos)

@carrinho_bp.route("/limpar_carrinho/<id>")
def limpar_carrinho(id):
    carrinho = Carrinho.query.filter(Carrinho.id == int(id)).first()
    for p in carrinho.produtos:
        remover_produto(p.id)
    carrinho.totalpreco = "0"
    carrinho.situacao = "Pendente"
    current_app.db.session.commit()
    return redirect(url_for("carrinho.mostrar_pedido"))