from flask import Blueprint, render_template, request, current_app, make_response
from config.model import Produto, Carrinho, Pedidos
from config.serealizer import ProdutoSchema, CarrinhoSchema


carrinho_bp= Blueprint("carrinho", __name__, template_folder="templates")


@carrinho_bp.route("/create_carrinho", methods= ["post"])
def create_carrinho():
    cs= CarrinhoSchema()
    carrinho= request.json
    print(type(carrinho))
    '''pedido_query = Pedidos.query.filter(Pedidos.id == 1).first()
    carrinho= cs.load(carrinho)
    current_app.db.session.add(carrinho)
    pedido_query.pedidos.append(carrinho)
    current_app.db.session.commit()
    response=make_response(cs.jsonify(carrinho))
    response.set_cookie("carrinho_id",str(carrinho.id))'''
    return "ok" \
           ""

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

@carrinho_bp.route("/delete_carrinho")
def delete_carrinho():
    id = request.args.get('id')
    cs = CarrinhoSchema(many=True)
    Carrinho.query.filter(Carrinho.id == id).delete()
    current_app.db.session.commit()
    return ...